# -*- coding: utf-8 -*-
import numpy as np


def add(target, *args):
    if len(args) == 1:
        return target + args[0]
    else:
        raise Exception('one arg is expected')


def minus(target, *args):
    if len(args) == 1:
        return target - args[0]
    else:
        raise Exception('one arg is expected')


def multiply(target, *args):
    if len(args) == 1:
        return target * args[0]
    else:
        raise Exception('one arg is expected')


def div(target, *args):
    if len(args) == 1:
        return target / args[0]
    else:
        raise Exception('one arg is expected')


def linspace(target, *args):
    if len(args) == 2:
        return np.linspace(args[0], args[1])
    if len(args) == 3:
        return np.linspace(args[0], args[1], args[2])
    else:
        raise Exception('two or three arg is expected')


def log(target, *args):
    if len(args) == 0:
        return np.log(target)
    else:
        raise Exception('no arg is expected')


def sin(target, *args):
    if len(args) == 0:
        return np.sin(target)
    else:
        raise Exception('no arg is expected')


def cos(target, *args):
    if len(args) == 0:
        return np.cos(target)
    else:
        raise Exception('no arg is expected')


def skip(target, *args):
    t = []
    i = 0
    if len(args) == 1:
        for e in target:
            if i % args[0] == 0:
                t.append(e)
            i = i + 1
    else:
        raise Exception('one arg is expected')


op = {
    'add': add,
    'minus': minus,
    'multiply': multiply,
    'div': div,
    'linspace': linspace,
    'log': log,
    'sin': sin,
    'cos': cos,
    'skip': skip
}


def pipeline_callback(target, callback, *args):
    if target is None:
        raise Exception('target is undefined')
    if not callable(callback):
        raise Exception('method is undefined')
    target = callback(target, args)
    return target


def pipeline(target, pipe_str: str):
    pipeline_target_local__ = target
    _local = locals()
    pipe_str = pipe_str.strip()
    bra_index = pipe_str.index('(')
    if bra_index < 0:
        raise Exception('invoke error')
    method_name = pipe_str[0:bra_index].strip()
    ket_index = pipe_str.rindex(')')
    if ket_index < 0:
        raise Exception('invoke error')
    args = pipe_str[bra_index + 1:ket_index]
    exec(str('r = pipeline_callback(pipeline_target_local__ ,' + method_name + ',' + args + ')'), globals(), _local)
    return _local['r']
