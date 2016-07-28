#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Date: 2016/7/28
# Author: Acceml
if __name__ == '__main__':
    l = []
    with open('filtered_words.txt', 'r') as f:
        for each_line in f:
            l.append(each_line.split('\n')[0])
    while 1:
        user = raw_input('input a word:')
        if user in l:
            print('Freedom')
        else:
            print('Human Rights')