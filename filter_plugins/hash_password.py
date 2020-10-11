#!/usr/bin/python
import crypt


def hash_password(password):
    return crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))


class FilterModule(object):
    def filters(self):
        return {
            'hash_password': hash_password,
        }
