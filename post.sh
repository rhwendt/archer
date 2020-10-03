#!/usr/bin/zsh

# set the timezone
TIMEZONE=$(tzselect)
echo "+ setting the timezone to $TIMEZONE"
ln -sf /usr/share/zoneinfo/"$TIMEZONE" /etc/localtime

# run playbook
ansible-playbook archer.yml --tags post --extra-vars "root_password=$root_password new_username=$new_username new_username_password=$new_username_password"
