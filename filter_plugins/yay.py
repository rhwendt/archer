#!/usr/bin/python


def generate_yay(package_list, user):
    command = f"arch-chroot /mnt runuser -l {user} -c 'yay -Sy --noconfirm"

    for package in package_list:
        command += f" {package}"
    command += "'"

    return command


class FilterModule(object):
    def filters(self):
        return {
            'yay': generate_yay,
        }
