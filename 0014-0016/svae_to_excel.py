#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Date: 2016/7/27
# Author: Acceml
"""
将JSON信息存入excel中
"""
import xlsxwriter, json


def json2xls_num_start_list_value(file_name, xls_name):
    table = xlsxwriter.Workbook(xls_name)
    sheet = table.add_worksheet('sheet1')

    with open(file_name, 'r') as f:
        data = json.load(f)
        for i in range(len(data)):
            row = data[str(i + 1)]
            sheet.write(i, 0, str(i + 1))
            print(row)
            for j in range(len(row)):
                sheet.write(i, j + 1, row[j])
    table.close()


def json2xls_num_start_string_value(file_name, xls_name):
    table = xlsxwriter.Workbook(xls_name)
    sheet = table.add_worksheet('sheet1')
    with open(file_name, 'r') as f:
        data = json.load(f)
        for i in range(len(data)):
            row = data[str(i + 1)]
            sheet.write(i, 0, str(i + 1))
            sheet.write(i, 1, row)


def json2xls_list_value(file_name, xls_name):
    table = xlsxwriter.Workbook(xls_name)
    sheet = table.add_worksheet('sheet1')
    with open(file_name, 'r') as f:
        data = json.load(f)
        for i in range(len(data)):
            for j in range(len(data[0])):
                sheet.write(i, j, data[i][j])


if __name__ == '__main__':
    json2xls_num_start_list_value('student.txt', 'student.xls')
    json2xls_num_start_string_value('city.txt', 'city.xls')
    json2xls_list_value('numbers.txt', 'numbers.xls')
