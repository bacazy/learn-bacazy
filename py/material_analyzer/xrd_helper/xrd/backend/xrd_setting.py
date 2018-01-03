# -*- coding: utf-8 -*-
import os

import xrd.utils as utils

setting_path = r'./.xrd/setting.xrd'


class XrdSetting:
    def __init__(self):
        if os.path.exists(setting_path):
            self.props = utils.load(setting_path)
        else:
            self.props = {}

    def getAttr(self, k, default=None):
        if self.props.__contains__(k):
            return self.props.get(k)
        else:
            return default

    def setAttr(self, k, v):
        self.props[k] = v

    def save(self):
        if not os.path.exists(os.path.dirname(setting_path)):
            os.mkdir(os.path.dirname(setting_path))
        utils.dump(setting_path, self.props)
