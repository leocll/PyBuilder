# -*- coding: utf-8 -*-
# @Time    : 2020-05-29 18:36
# @Author  : leocll
# @Email   : leocll@qq.com
# @File    : main.py

import os
import lib1
import lib2
from config import path4root

if __name__ == '__main__':
    print('example1')
    lib1.test()
    lib2.test()
    print('===============')
    print("'%s' %s" % (lib1.test_file, '存在' if os.path.exists(lib1.test_file) else '不存在'))
    file = path4root('txt', 'test.txt')
    print("'%s' %s" % (file, '存在' if os.path.exists(file) else '不存在'))
    file = lib2.test_file
    print("'%s' %s" % (file, '存在' if os.path.exists(file) else '不存在'))
    file = lib2.test_file2
    print("'%s' %s" % (file, '存在' if os.path.exists(file) else '不存在'))
    pass