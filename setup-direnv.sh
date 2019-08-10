#!/bin/bash

if [ "$EUID" -ne 0 ]
then echo -e "\e[31mPlease run as root\e[0m"
    exit
fi

declare -l releasePlatform=""

case "$(uname -s)" in
  Darwin)
    echo 'Mac OS X'
    releasePlatform=darwin-amd64
    ;;
  Linux)
    echo 'Linux'
    releasePlatform=linux-amd64
    ;;
  *)
    echo 'Not supported OS'
    exit 0
    ;;
esac

wget https://github.com/direnv/direnv/releases/latest/download/direnv.$releasePlatform -O /usr/local/bin/direnv
chmod +x /usr/local/bin/direnv

direnv allow

echo -e '\e[93mAdd following to your to .bashrc:\n\neval "$(direnv hook bash)"\e[0m'
