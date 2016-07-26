#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Date: 2016/7/26
# Author: Acceml
if __name__ == '__main__':
    words = ['cat', 'window']
    # list
    classmates = ('Michael', 'Bob', 'Tracy')
    # tuple
    for w in words:
        print(w, len(w))
    for i in range(len(words)):
        print(i, words[i])
    d = {'A': 1, 'B': 2}
    # dict
    print d['A']
    """
    a note example

    """
    #set
    s = set(words)

