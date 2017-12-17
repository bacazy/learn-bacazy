# -*- coding: utf-8 -*-
import numpy as np


class Action:
    def __init__(self, action, params):
        self.action = action
        self.params = params


class XrdMisc:
    def __init__(self):
        self.props = {}
        self.log = []

    def config(self, callback=None, **kwargs):
        for k, v in kwargs.items():
            self.props[k] = v
        if callback is not None:
            callback(kwargs)

    def get_prop(self, k):
        return self.props[k]

    def push_log(self, action, **kwargs):
        self.log.append(Action(action, kwargs))

    def pop_log(self):
        if len(self.log) > 0:
            self.log.pop()


class XrdPattern(XrdMisc):
    def __init__(self, pid, pattern):
        super().__init__()
        self.pid = pid
        self.pattern = pattern


class Duplicated(Exception):
    def __init__(self, cls=None, target=None):
        super().__init__(str(cls) + " " + str(target) + " is duplicated")


class Xrd(XrdMisc):
    def __init__(self):
        super().__init__()
        self.theta = None
        self.intensity = None
        self.fname = ''
        self.patterns = []
        self.name=''

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


class XrdProject(XrdMisc):
    def __init__(self):
        super().__init__()
        self.xrds = []

    def load(self, fname):
        pass


    def import_xrd(self, fname):
        xrd = Xrd()
        xrd.load(fname)
        self.xrds.append(xrd)
        return xrd

