# -*- coding: utf-8 -*-
# @Time    : 2020-05-29 18:40
# @Author  : leocll
# @Email   : leocll@qq.com
# @File    : file1.py

import os
test_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.txt')

def test():
    print(__file__)

if __name__ == '__main__':
    pass