#!/bin/bash

sudo apt-get update

#installs pip3, should make it check first
sudo apt install python3-pip --fix-missing -y

#installs python dependencies

  #telegram
  pip3 install python-telegram-bot --upgrade

  #beautiful soup
  pip3 install bs4 --upgrade

  #lxml
  pip3 install lxml --upgrade

  #youtube_dl
  pip3 install youtube_dl --upgrade

#installs ffprobe
sudo apt-get install ffmpeg -y
