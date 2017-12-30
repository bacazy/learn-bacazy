# -*- coding: utf-8 -*-
from xrd.backend.base import XrdMisc


class XrdPattern(XrdMisc):
    def __init__(self, pid, pattern):
        super().__init__()
        self.pid = pid
        self.pattern = pattern
