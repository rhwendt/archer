#!/usr/bin/python


def get_rootfs_uuid(mounts):
    # root partition in chroot env is /mnt
    for dev in mounts:
        if dev["mount"] == "/mnt":
            return dev["uuid"]


class FilterModule(object):
    def filters(self):
        return {
            'rootfs_uuid': get_rootfs_uuid,
        }
