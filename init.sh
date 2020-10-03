#!/usr/bin/zsh

# update repos
pacman -Sy

# install stuff
pacman -S git ansible --noconfirm

# clone repos
git clone https://github.com/rhwendt/archer.git

# install galaxy collection
ansible-galaxy collection install community.general

# get ansible-aur
git clone https://github.com/kewlfft/ansible-aur.git ~/.ansible/plugins/modules/aur

# run playbook
ansible-playbook archer/archer.yml --tags init

