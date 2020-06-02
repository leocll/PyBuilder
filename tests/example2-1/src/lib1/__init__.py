# -*- coding: utf-8 -*-
# @Time    : 2020-05-29 18:39
# @Author  : leocll
# @Email   : leocll@qq.com
# @File    : __init__.py.py

from config import path4root as _path4root
def path4package(*fields: str) -> str:
    return _path4root('lib2', *fields)

from .file1 import test, test_file

if __name__ == '__main__':
    pass