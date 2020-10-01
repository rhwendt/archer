#!/usr/bin/bash

# update repos
pacman -Sy

# install stuff
pacman -S git ansible --noconfirm

# clone repos
git clone https://github.com/rhwendt/archer.git && cd archer
