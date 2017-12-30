# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QTreeWidget, QMenu, QAction, QInputDialog

from xrd.backend.xrd_prj_item import XrdProjectItem


class ProjectView(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setHeaderLabels(['Project'])
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_right_click)
        self.setMouseTracking(True)
        self.itemSelectionChanged.connect(self.on_item_select)
        self.create_actions()
        self.pop_menu = self.create_pop_menu()
        self.currentProject = None

    def refresh(self):
        self.clear()
        if self.currentProject is not None:
            self.addTopLevelItem(self.create_project_tree())

    def create_project_tree(self):
        prj = XrdProjectItem(self.currentProject, self)
        return prj

    def create_actions(self):
        self.action_import_xrd = self.createAction('Import Xrd', self.on_import_xrd)
        self.action_rename = self.createAction('Rename', self.on_rename)

    def on_rename(self):
        cur = self.currentItem()
        if cur is not None:
            dlg, accept = QInputDialog.getText(self, 'rename', 'please input')
            print(dlg)

    def on_import_xrd(self):
        print('ac')

    def createAction(self, name, callback, icon=None, shortcut=None, tip=None):
        if icon is None:
            action = QAction(name, self)
        else:
            action = QAction(QIcon(icon), name, self)
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setStatusTip(tip)
        action.triggered.connect(callback)
        return action

    def create_pop_menu(self):
        pop_menu = QMenu()
        pop_menu.addAction(self.action_import_xrd)
        pop_menu.addAction(self.action_rename)
        return pop_menu

    def on_right_click(self, data):
        current = self.currentItem()
        self.action_import_xrd.setDisabled(current is None)
        self.action_rename.setDisabled(current is None)
        self.pop_menu.exec(QCursor.pos())

    def on_item_select(self):
        print('item select')
