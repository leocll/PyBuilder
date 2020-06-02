# -*- coding: utf-8 -*-
# @Time    : 2020-05-29 19:03
# @Author  : leocll
# @Email   : leocll@qq.com
# @File    : main.py


if __name__ == '__main__':
    import os
    build_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(os.path.dirname(build_dir), 'src')
    from PyBuilder import run
    run(name='example1', src_dir=src_dir, build_dir=build_dir)
    pass