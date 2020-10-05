#!/usr/bin/zsh

# install stuff
pacman -Sy git ansible --noconfirm

# clone repos
git clone https://github.com/rhwendt/archer.git

# install galaxy collection
ansible-galaxy collection install community.general

# get ansible-aur
git clone https://github.com/kewlfft/ansible-aur.git ~/.ansible/plugins/modules/aur

# run playbook
cd archer && ansible-playbook archer.yml --tags init

