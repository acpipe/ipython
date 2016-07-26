#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Date: 2016/7/26
# Author: Acceml

import random
import string

import mysql.connector


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
    cnx = mysql.connector.connect(user='cloud', password='cloud',
                                  host='172.31.1.162',
                                  database='cloud')
    query = "SELECT * from cloud.account"
    curA = cnx.cursor(buffered=True)
    curA.execute("DROP TABLE IF EXISTS rkeys")
    curA.execute("CREATE TABLE rkeys(\
                      key_value CHAR(40) NOT NULL\
                      )")

    for i in generate__promote_code():
        print(i)
        curA.execute("INSERT INTO rkeys(key_value)VALUES('%s')" % i)

    cnx.commit()
    cnx.close


