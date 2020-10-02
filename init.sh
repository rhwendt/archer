#!/usr/bin/zsh

# update repos
pacman -Sy

# install stuff
pacman -S git ansible --noconfirm

# clone repos
git clone https://github.com/rhwendt/archer.git

# change to archer dir
cd archer

# install galaxy collection
ansible-galaxy collection install community.general

# run playbook
ansible-playbook archer.yml --tags init

