#!/usr/bin/python


def get_rootfs_uuid(mounts):
    for dev in mounts:
        if dev["mount"] == "/":
            return dev["uuid"]


class FilterModule(object):
    def filters(self):
        return {
            'rootfs_uuid': get_rootfs_uuid,
        }
