# -*- coding: utf-8 -*-
# @Time    : 2020-05-29 18:36
# @Author  : leocll
# @Email   : leocll@qq.com
# @File    : main.py

import os
import lib1
import lib2

if __name__ == '__main__':
    print('example1')
    lib1.test()
    lib2.test()
    print('===============')
    print("'%s' %s" % (lib1.test_file, '存在' if os.path.exists(lib1.test_file) else '不存在'))
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(cur_dir, 'txt', 'test.txt')
    print("'%s' %s" % (file, '存在' if os.path.exists(file) else '不存在'))
    file = lib2.test_file   # os.path.join(cur_dir, 'lib2', 'test.txt')
    print("'%s' %s" % (file, '存在' if os.path.exists(file) else '不存在'))
    file = lib2.test_file2  # os.path.join(cur_dir, 'lib2', 'txt', 'test.txt')
    print("'%s' %s" % (file, '存在' if os.path.exists(file) else '不存在'))
    pass