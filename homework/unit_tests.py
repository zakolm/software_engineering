#!/usr/bin/env python

import os
from main import *

# Error codes
OK = 0
NOT_OK = -1
FILE_EMPTY = -2
EOF = -3
FILE_NE = -4
STRING_COR = -5
STRING_INCOR = -6

def test_SumNum():
    err_cnt = 0

    x_s = SumNum(56)
    if x_s != 11:
        err_cnt += 1
        print('test_SumNum: sum num of 56 not 11')
        
    x_s = SumNum(-33)
    if x_s != 6:
        err_cnt += 1
        print('test_SumNum: sum num of -33 not 6')
        
    x_s = SumNum(0)
    if x_s != 0:
        err_cnt += 1
        print('test_SumNum: sum num of 0 not 0')

    if err_cnt != 0:
        print('test_SumNum: {:d}'.format(err_cnt))
    else:
        print('test_SumNum: OK')

def test_TypeSum():
    err_cnt = 0

    x_t = TypeSum(11)
    if x_t:
        err_cnt += 1
        print('test_TypeSum: type sum of 11 not unevent')

    x_t = TypeSum(6)
    if not x_t:
        err_cnt += 1
        print('test_TypeSum: type sum of 6 not event')

    x_t = TypeSum(0)
    if not x_t:
        err_cnt += 1
        print('test_TypeSum: type sum of 0 not event')

    if err_cnt != 0:
        print('test_TypeSum: {:d}'.format(err_cnt))
    else:
        print('test_TypeSum: OK')

def test_TransformEvenNum():
    err_cnt = 0
        
    x_n = TransformEvenNum(66)
    if x_n != 1000010:
        err_cnt += 1
        print('test_TransformEvenNum: transform num of 66 not 1000010')
                
    x_n = TransformEvenNum(0)
    if x_n != 0:
        err_cnt += 1
        print('test_TransformEvenNum: transform num of 0 not 0')
                
    x_n = TransformEvenNum(-33)
    if x_n != 11011111:
        err_cnt += 1
        print('test_TransformEvenNum: transform num of -33 not 11011111')
        
    x_n = TransformEvenNum(6)
    if x_n != 110:
        err_cnt += 1
        print('test_TransformEvenNum: transform num of 6 not 110')
        
    x_n = TransformEvenNum(-6)
    if x_n != 11111010:
        err_cnt += 1
        print('test_TransformEvenNum: transform num of -6 not 11111010')
    
    x_n = TransformEvenNum(127)
    if x_n != 1111111:
        err_cnt += 1
        print('test_TransformEvenNum: transform num of 127 not 1111111')

    if err_cnt != 0:
        print('test_TransformEvenNum: {:d}'.format(err_cnt))
    else:
        print('test_TransformEvenNum: OK')

def test_TransformUnevenNum():
    err_cnt = 0

    x_n = TransformUnevenNum(56)
    if x_n != 65:
        err_cnt += 1
        print('test_TransformUnevenNum: transform num of 56 not 65')
                
    x_n = TransformUnevenNum(-27)
    if x_n != -72:
        err_cnt += 1
        print('test_TransformUnevenNum: transform num of -27 not -72')
        
    x_n = TransformUnevenNum(-128)
    if x_n != -821:
        err_cnt += 1
        print('test_TransformUnevenNum: transform num of -128 not -821')

    x_n = TransformUnevenNum(10)
    if x_n != 1:
        err_cnt += 1
        print('test_TransformUnevenNum: transform num of 10 not 1')

    if err_cnt != 0:
        print('test_TransformUnevenNum: {:d}'.format(err_cnt))
    else:
        print('test_TransformUnevenNum: OK')

def main():
    test_ReadString()
    test_SumNum()
    test_TypeSum()
    test_TransformEvenNum()
    test_TransformUnevenNum()
        
    return 0

if __name__ == '__main__':
    main()
