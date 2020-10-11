#!/usr/bin/python


def generate_pac(package_list, pacstrap=False):
    if pacstrap:
        command = "pacstrap /mnt"
    else:
        # bit of a hack
        command = "arch-chroot /mnt pacman -Sy --noconfirm"

    for package in package_list:
        command += f" {package}"

    return command


class FilterModule(object):
    def filters(self):
        return {
            'pacman': generate_pac,
        }
