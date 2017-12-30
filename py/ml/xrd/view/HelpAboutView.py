# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog

from xrd.view.ui import help_about


class HelpAboutView(QDialog, help_about.Ui_Dialog):
    def __init__(self, parent=None):
        super(HelpAboutView, self).__init__(parent)
        self.setupUi(self)
