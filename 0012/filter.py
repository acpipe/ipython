#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Date: 2016/7/28
# Author: Acceml

def get_word(path):
    l = []
    with open(path, 'r') as f:
        for line in f:
            l.append(line.split('\n')[0])
    return l


if __name__ == '__main__':
    l = get_word('filtered_words.txt')
    while True:
        input_word = raw_input('input:')
        for w in l:
            if w in input_word:
                input_word = input_word.replace(w, ''.join('*' for x in range(len(w))))
        print(input_word)
