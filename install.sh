#!/bin/bash

git clone https://github.com/Telecominfraproject/oopt-gnpy.git

git remote add staging https://github.com/Telecominfraproject/oopt-gnpy.git

git remote

git fetch staging

git branch -r

git checkout -b staging staging/phase-1

sudo apt-get install python3-pip

pip3 install numpy

pip3 install scipy

pip3 install matplotlib

sudo apt-get install python3-tk
