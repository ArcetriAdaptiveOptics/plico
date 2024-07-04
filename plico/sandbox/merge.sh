#!/bin/bash

OLDGIT=git
NEWGIT=git.2.45.2
OLDREPOS="plico plico_motor plico_motor_server pysilico pysilico_server plico_dm plico_dm_server plico_dm_characterization plico_interferometer plico_interferometer_server"
#OLDREPOS="pysilico plico_motor"
NEWREPO=plico2
URLPREFIX=https://github.com/ArcetriAdaptiveOptics
BRANCHES="discovery multiaxis cblue"




mkdir $NEWREPO
cd $NEWREPO
git init .
echo "Empty readme" > README.md
git add README.md
git commit -m "First commit"
git branch -m main

cd ..
for REPO in $OLDREPOS
do
    $OLDGIT clone $URLPREFIX/$REPO
    cd $REPO
    git filter-repo --to-subdirectory-filter $REPO
    git branch -m master main
    pwd
    cd ../$NEWREPO
    git remote add $REPO ../$REPO
    git fetch $REPO --no-tags
    cd ..
done
cd $NEWREPO

# Merge all masters
git checkout main
for REPO in $OLDREPOS
do
    EDITOR=true git merge --allow-unrelated-histories $REPO/main
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



