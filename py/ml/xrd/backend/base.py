# -*- coding: utf-8 -*-
import numpy as np


class Duplicated(Exception):
    def __init__(self, cls=None, target=None):
        super().__init__(str(cls) + " " + str(target) + " is duplicated")


class Action:
    def __init__(self, action, params):
        self.action = action
        self.label = action
        self.params = params


class XrdMisc:
    def __init__(self):
        self.name = None
        self.label = None
        self.selected = False
        self.expand = False
        self.props = {}
        self.log = []

    def config(self, callback=None, **kwargs):
        for k, v in kwargs.items():
            self.props[k] = v
        if callback is not None:
            callback(kwargs)

    def getType(self):
        return type(self)

    def get_prop(self, k, default=None):
        if self.props.__contains__(k):
            return self.props[k]
        return default

    def set_prop(self, k, v):
        self.props[k] = v

    def push_log(self, action, **kwargs):
        self.log.append(Action(action, kwargs))

    def pop_log(self):
        if len(self.log) > 0:
            self.log.pop()


class Xrd(XrdMisc):
    def __init__(self):
        super().__init__()
        self.theta = None
        self.intensity = None
        self.fname = ''
        self.patterns = []

    def add_pattern(self, pattern):
        if self.patterns.__contains__(pattern.pid):
            raise Duplicated(cls='xrd pattern', target=pattern.pid)
        self.patterns[pattern['pid']] = pattern

    def remove_pattern(self, pid):
        if self.patterns.__contains__(pid):
            del self.patterns[pid]

    def load(self, fname):
        f_data = np.loadtxt(fname=fname, dtype=float, skiprows=1)
        self.fname = fname
        self.theta = f_data[:, 0]
        self.intensity = f_data[:, 1]
