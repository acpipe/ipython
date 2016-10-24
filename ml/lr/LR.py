#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Date: 2016/9/28
# Author: Acceml
from math import exp

from numpy import mat, shape, ones


def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat


def sigmoid(x):
    return 1.0 / (1 + exp(-x))


def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)  # convert to NumPy matrix
    labelMat = mat(classLabels).transpose()  # convert to NumPy matrix
    m, n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n, 1))
    for k in range(maxCycles):  # heavy on matrix operations
        print(dataMatrix * weights)
        h = sigmoid(dataMatrix * weights)  # matrix mult
        error = (labelMat - h)  # vector subtraction
        weights = weights + alpha * dataMatrix.transpose() * error  # matrix mult
    return weights


if __name__ == '__main__':
    tuple1, tuple2 = loadDataSet()
    print(tuple1)
    print(tuple2)
    gradAscent(tuple1, tuple2)
