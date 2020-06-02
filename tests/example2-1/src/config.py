# -*- coding: utf-8 -*-
# @Time    : 2020-06-01 15:01
# @Author  : leocll
# @Email   : leocll@qq.com
# @File    : config.py

import sys as _sys
import os as _os

if hasattr(_sys, '_MEIPASS'):
    SRC_ROOT = getattr(_sys, '_MEIPASS', _os.path.abspath(_os.path.dirname(__file__)))  # 根目录
    IS_BUNDLE = True
else:
    SRC_ROOT = _os.path.abspath(_os.path.dirname(__file__))                             # 根目录
    IS_BUNDLE = False

def path4root(*fields: str) -> str:
    return _os.path.join(SRC_ROOT, *fields)

if __name__ == '__main__':
    pass