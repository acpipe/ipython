#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Date: 2016/7/26
# Author: Acceml

class Student(object):
    # do not need specific __name
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))


if __name__ == '__main__':
    a = Student('huming', 100)
    a.print_score()
