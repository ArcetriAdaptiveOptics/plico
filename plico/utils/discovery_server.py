import json
import time
import socket

DISCOVER_PORT = 9999
DISCOVER_COMMAND = 'DISCOVER'
BROADCAST_IP = '255.255.255.255'


class DiscoveryServer():
    '''UDP discovery server.

    Initialize with a dict containing the discovery info. As a minimun,
    it must contain a "name" key with the resource name.
    '''
    def __init__(self, data_dict):
        if not 'name' in data_dict:
            raise ValueError('Data dictionary must contain a "name" keyword for discovery')
        self._data = data_dict
        self._data['host'] = self._myip()
        self._time_to_die = False
    
    def _myip(self):
        return socket.gethostbyname(socket.gethostname())
    
    def run(self):
        '''Loop forever serving discovery requests'''
        print('Running, data:', self._data)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        sock.bind(('', DISCOVER_PORT))   # Listen for broadcasts
        while not self._time_to_die:
            try:
                data, addr = sock.recvfrom(1024,socket.MSG_DONTWAIT)
            except BlockingIOError:
                time.sleep(1)
                continue
            if DISCOVER_COMMAND in data.decode():
                response = json.dumps(self._data)
                sock.sendto(response.encode(), addr)

    def die(self):
        self._time_to_die = True


class DiscoveryClient():
    '''UDP discovery client'''

    def __init__(self):
        pass

    def run(self, name=None, timeout_in_seconds=10):
        '''
        Broadcast a discovery request and wait for server replies
        for up to <timeout_in_seconds>. If name is set,
        will return the server info for that specific name, otherwise
        it will return a list of discovered servers.
        ''' 
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.settimeout(timeout_in_seconds)

        message = DISCOVER_COMMAND
        sock.sendto(message.encode(), (BROADCAST_IP, DISCOVER_PORT))

        # Collect responses from servers
        discovered_servers = []
        start_time = time.time()

        while True:
            try:
                data, addr = sock.recvfrom(1024)
                server_info = json.loads(data.decode())
                discovered_servers.append(server_info)
                if name is not None:
                    if server_info['name'] == name:
                        return server_info
            except socket.timeout:
                pass
            if time.time() - start_time > timeout_in_seconds:
                if name is None and len(discovered_servers) > 0:
                    return discovered_servers
                else:
                    raise TimeoutError

