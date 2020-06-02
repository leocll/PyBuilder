# -*- coding: utf-8 -*-
# @Time    : 2020-06-01 13:56
# @Author  : leocll
# @Email   : leocll@qq.com
# @File    : build_hook.py

import sys
import typing
from PyBuilder.data import BuildData

def _hook_implement(target, *args, **kwargs):
    print('Hook: %s' % sys._getframe().f_back.f_code.co_name)
    return target

def hook_data(data: BuildData):
    _hook_implement(data)

def hook_excludes(target: typing.List[str], data: BuildData) -> typing.List[str]:
    return _hook_implement(target, data)

def hook_ignores(target: typing.List[str], data: BuildData) -> typing.List[str]:
    return _hook_implement(target, data)

def hook_build_lib_path(target: typing.List[str], data: BuildData) -> typing.List[str]:
    return _hook_implement(target, data)

def hook_build_data(target: typing.List[typing.Tuple[str, str]], data: BuildData) -> typing.List[typing.Tuple[str, str]]:
    return _hook_implement(target, data)

def hook_build_imports(target: typing.List[str], data: BuildData) -> typing.List[str]:
    return _hook_implement(target, data)

def hook_pre_compile(data: BuildData):
    _hook_implement(data)
    
def hook_compiled(data: BuildData):
    _hook_implement(data)

def hook_pre_build(data: BuildData):
    _hook_implement(data)

def hook_built(data: BuildData):
    _hook_implement(data)

if __name__ == '__main__':
    pass