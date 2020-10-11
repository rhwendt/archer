#!/usr/bin/zsh

# install stuff
pacman -Sy git ansible --noconfirm

# clone repos
git clone https://github.com/rhwendt/archer.git

# install galaxy collection
ansible-galaxy collection install community.general

# configure users
cd archer && python scripts/configure_users.py

# run playbook
ansible-playbook archer.yml

