# -*- coding: utf-8 -*-
# @Time    : 2020-05-29 18:39
# @Author  : leocll
# @Email   : leocll@qq.com
# @File    : __init__.py.py

import os

test_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.txt')
test_file2 = os.path.join(os.path.dirname(os.path.dirname(test_file)), 'txt', 'test.txt')

def test():
    print('lib2')
    print(__file__)

if __name__ == '__main__':
    pass