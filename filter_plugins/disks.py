#!/usr/bin/python


def get_disks(d):
    i = 0
    output = []
    for k in d.keys():
        if 'loop' in k:
            continue
        disk_num = i
        device = f"/dev/{k}"
        size = d[k]["size"]
        model = d[k]["model"]
        output.append(f"Disk: {disk_num}")
        output.append(f"Device: {device}")
        output.append(f"Size: {size}")
        output.append(f"Model: {model}")
        output.append("")
        i += 1
    return output


class FilterModule(object):
    def filters(self):
        return {
            'disks': get_disks,
        }
