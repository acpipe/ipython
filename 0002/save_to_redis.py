#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Date: 2016/7/26
# Author: Acceml
import random
import string

import redis, uuid


def generate__promote_code():
    l = []
    for fuck in range(10):
        chars = string.letters + string.digits
        # gen 20 bit code
        s = [random.choice(chars) for j in range(20)]
        # join list to a string.
        l.append(''.join(s))
    return l


if __name__ == '__main__':
    r = redis.StrictRedis(host='172.31.1.151', port=6379)
    i = 0
    l = generate__promote_code()
    for fuck in l:
        r.set('promote_code' + str(i), fuck)
        i += 1
    for j in range(10):
        print r.get('promote_code' + str(j))
