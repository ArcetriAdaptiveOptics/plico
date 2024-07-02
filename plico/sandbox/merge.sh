#!/bin/bash

OLDGIT=/usr/bin/git
NEWGIT=git
OLDREPOS="plico plico_motor plico_motor_server pysilico pysilico_server plico_dm plico_dm_server plico_dm_characterization plico_interferometer plico_interferometer_server"
#OLDREPOS="plico plico_motor"
NEWREPO=plico2
URLPREFIX=https://github.com/ArcetriAdaptiveOptics
BRANCHES="discovery multiaxis cblue"




mkdir $NEWREPO
cd $NEWREPO
git init .
echo "Empty readme" > pippo.md
git add pippo.md
git commit -m "First commit"

cd ..
for REPO in $OLDREPOS
do
    $OLDGIT clone $URLPREFIX/$REPO
    cd $REPO
    git branch -m main master
    git filter-repo --to-subdirectory-filter $REPO
    pwd
    cd ../$NEWREPO
    git remote add $REPO ../$REPO
    git fetch $REPO --no-tags
    cd ..
done
cd $NEWREPO

# Merge all masters
git checkout master
for REPO in $OLDREPOS
do
    EDITOR=true git merge --allow-unrelated-histories $REPO/master
done

# Merge all others
for BRANCH in $BRANCHES
do
    git checkout -b $BRANCH
    for REPO in $OLDREPOS
    do
        EDITOR=true git merge --allow-unrelated-histories $REPO/$BRANCH
    done
done

for REPO in $OLDREPOS
do
    git remote remove $REPO
done
cd ..



