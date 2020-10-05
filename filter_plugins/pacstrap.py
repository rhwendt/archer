#!/usr/bin/python


def generate_pacstrap(packages_list):
    command = "pacstrap /mnt"
    for package in packages_list:
        command += f" {package}"

    return command


class FilterModule(object):
    def filters(self):
        return {
            'pacstrap': generate_pacstrap,
        }
