# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTreeWidgetItem

from xrd.backend.base import Xrd
from xrd.backend.xrd_pattern import XrdPattern
from xrd.backend.xrd_project import XrdProject


def getSpecifyIcon(model):
    icon = 'assets/'
    if isinstance(model, XrdProject):
        icon += 'prj.png'
    elif isinstance(model, Xrd):
        icon += 'folder'
    elif isinstance(model, XrdPattern):
        icon += 'database.png'
    else:
        icon += 'page.png'
    return QIcon(icon)


class XrdProjectItem(QTreeWidgetItem):
    def __init__(self, item, parent=None, **kwargs):
        super().__init__(parent)
        self.model = item
        self.setText(0, self.model.label)
        self.setIcon(0, getSpecifyIcon(self.model))
        if not isinstance(self.model, XrdProject):
            self.setFlags(Qt.ItemIsUserCheckable)
        if isinstance(self.model, XrdProject):
            for xrd in self.model.xrds:
                self.addChild(XrdProjectItem(xrd, self))
        elif isinstance(self.model, Xrd):
            for action in self.model.log:
                self.addChild(XrdProjectItem(action, self))
