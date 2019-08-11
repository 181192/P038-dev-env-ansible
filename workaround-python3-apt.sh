#!/bin/bash

# python3-apt package not available through PyPi, only via apt-get.
# apt-get installs globally and python virtual environment is not using global libraries.
# This script copies the python3-apt sources to the virtual environment pythin libraries.

set -e

python_version=`python --version 2>&1 | awk '{print $2}'`
echo -e "\e[93mPython version $python_version is installed at $(which python)\e[0m"

cwd=$(pwd)

mkdir -p .tmp

cd .tmp
echo -e "\e[93mDownloading python3-apt sources\e[0m"
apt-get download python3-apt
dpkg -x python3-apt*.deb python3-apt

cp -r python3-apt/usr/lib/python3/dist-packages/* ../.direnv/python-$python_version/lib/python3.7/site-packages

cd ../.direnv/python-$python_version/lib/python3.7/site-packages

mv apt_pkg.cpython*.so apt_pkg.so
mv apt_inst.cpython*.so apt_inst.so

echo -e "\e[93mCleaning up files\e[0m"
rm -rf $cwd/.tmp

echo -e "\e[32mDone\e[0m"