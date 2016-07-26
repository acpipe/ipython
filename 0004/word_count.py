#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Date: 16-7-26
# Author: Acceml
if __name__ == '__main__':
    lineNum = 0
    f = open('passage.txt', 'rb')
    for eachLine in f:
        lineNum += len(eachLine.split(' '))
    print(lineNum)
    f.close()