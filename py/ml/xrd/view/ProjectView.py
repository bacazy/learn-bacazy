# -*- coding: utf-8 -*-
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QTreeView


class ProjectView(QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Project Structure'])
        self.setModel(self.model)
        self.redraw(["As", "Db"])

    def redraw(self, prj):
        for p in prj:
            item = QStandardItem(p)
            for i in range(10):
                item.appendRow(QStandardItem("Sub " + str(i)))
            self.model.appendRow(item)

