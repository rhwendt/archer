#!/usr/bin/zsh

# set the timezone
TIMEZONE=$(tzselect)
echo "+ setting the timezone to $TIMEZONE"
ln -sf /usr/share/zoneinfo/"$TIMEZONE" /etc/localtime

# install galaxy collection
ansible-galaxy collection install community.general

# run playbook
ansible-playbook archer.yml --tags post
