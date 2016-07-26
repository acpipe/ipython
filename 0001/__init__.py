#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Date: 2016/7/26
# Author: Acceml
import random
import string

if __name__ == '__main__':
    f = open('promote_code.txt', 'wb')
    for i in range(200):
        chars = string.letters + string.digits
        print(chars)
        # gen 20 bit code
        s = [random.choice(chars) for i in range(20)]
        # join list to a string.
        f.write(''.join(s) + '\n')
    f.close()
