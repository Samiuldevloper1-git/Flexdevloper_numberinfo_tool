#!/bin/bash

clear

echo "Installing Flex Developer Tool..."

pkg update -y
pkg install python -y

pip install -r requirements.txt

python tool.py
