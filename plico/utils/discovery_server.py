import json
import time
import socket
from dataclasses import dataclass

DISCOVER_PORT = 9999
DISCOVER_COMMAND = 'DISCOVER'
BROADCAST_IP = '255.255.255.255'

@dataclass
class LocalServerInfo():
    '''Description of a plico server running locally'''
    name: str
    port: int
    deviceclass: str


@dataclass
class ServerInfo():
    '''Description of a remote plico server'''
    name: str
    host: str
    port: int
    deviceclass: str


class DiscoveryServer():
    '''UDP discovery server.

    Initialize with a dict containing the discovery info. As a minimun,
    it must contain a "name" key with the resource name.
    '''
    def __init__(self, local_server_info_getter):
        assert callable(local_server_info_getter)
        self._local_server_info_getter = local_server_info_getter
        self._time_to_die = False

    def _myip(self):
        return socket.gethostbyname(socket.gethostname())

    def run(self):
        '''Loop serving discovery requests.

        This function is intended to be started as a
        separate thread. Use the self.die() method to stop.
        '''
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
                local_server_info = self._local_server_info_getter()
                assert isinstance(local_server_info, LocalServerInfo), \
                    'server_info must be an instance of the LocalServerInfo dataclass'
                data = ServerInfo(host=self._myip(), **local_server_info.__dict__)
                if data.deviceclass == '':
                    # device class not set yet, do not answer broadcast
                    continue
                print('Sending:', data)
                sock.sendto(json.dumps(data.__dict__).encode(), addr)

    def die(self):
        '''Stop the server loop'''
        self._time_to_die = True


class DiscoveryClient():
    '''UDP discovery client'''

    def __init__(self):
        pass

    def run(self, name=None, timeout_in_seconds=2):
        '''
        Broadcast a discovery request and wait for server replies
        for up to <timeout_in_seconds>. If *name* is set,
        will return the server info for that specific name, otherwise
        it will return a list of discovered servers.
        Each server info is a ServerInfo instance.
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
                server_info = ServerInfo(**json.loads(data.decode()))
                discovered_servers.append(server_info)
                if name is not None:
                    if server_info.name == name:
                        return server_info
            except socket.timeout:
                pass
            if time.time() - start_time > timeout_in_seconds:
                if name is None and len(discovered_servers) > 0:
                    return discovered_servers
                else:
                    raise TimeoutError(f'No server with name {name} found')
