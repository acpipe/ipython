#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Date: 2016/7/27
# Author: Acceml

if __name__ == '__main__':
    l = []
    with open('filtered_words.txt', 'r') as f:
        for each_line in f:
            l.append(each_line.split('\n'))
    print(l)