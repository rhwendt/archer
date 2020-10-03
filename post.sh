#!/usr/bin/zsh

# set the timezone
TIMEZONE=$(tzselect)
echo "+ setting the timezone to $TIMEZONE"
ln -sf /usr/share/zoneinfo/"$TIMEZONE" /etc/localtime

# install ansible-aur in new system
git clone https://github.com/kewlfft/ansible-aur.git ~/.ansible/plugins/modules/aur

# run playbook
ansible-playbook archer.yml --tags post
