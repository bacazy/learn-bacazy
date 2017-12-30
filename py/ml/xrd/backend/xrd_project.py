# -*- coding: utf-8 -*-
import xrd.utils as utils
from xrd.backend.base import XrdMisc, Xrd


class XrdProject(XrdMisc):
    def __init__(self):
        super().__init__()
        self.xrds = []
        self.location = None
        self.last_modify = utils.currentTime()
        self.saved = False

    def import_xrd(self, fname):
        xrd = Xrd()
        xrd.load(fname)
        self.xrds.append(xrd)
        return xrd

    def save(self):
        utils.dump(self.location, self)

    def setLocation(self, fname):
        self.location = fname

    def init(self):
        pass
