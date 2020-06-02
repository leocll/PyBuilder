# -*- coding: utf-8 -*-
# @Time    : 2020-05-29 18:40
# @Author  : leocll
# @Email   : leocll@qq.com
# @File    : file1.py

from . import path4package
test_file = path4package('test.txt')

def test():
    print(__file__)

if __name__ == '__main__':
    pass