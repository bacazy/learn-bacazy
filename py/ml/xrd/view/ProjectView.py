# -*- coding: utf-8 -*-
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QTreeView

icon_map = {'dir': QIcon('assets/dir.ico'), 'file': QIcon('assets/file.ico')}


class ProjectView(QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # self.item = QStandardItem()
        # self.item.appendColumn()
        # self.model = QStandardItemModel()
        # self.model.appendRow()
