#!/usr/bin/zsh

# set the timezone
TIMEZONE=$(tzselect)
echo "+ setting the timezone to $TIMEZONE"
ln -sf /usr/share/zoneinfo/"$TIMEZONE" /etc/localtime

# install galaxy collection
ansible-galaxy collection install community.general

read -sp "Please enter new root password: " root_password
read -sp "Please enter new username: " new_username
read -sp "Please enter new username password: " new_username_password

# run playbook
ansible-playbook archer.yml --tags post --extra-vars "root_password=$root_password new_username=$new_username new_username_password=$new_username_password"
