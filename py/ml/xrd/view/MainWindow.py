# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QGridLayout, QWidget, QMainWindow, QAction, \
    qApp
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

from xrd.view.HelpAboutView import HelpAboutView
from xrd.view.ProjectView import ProjectView


class MainView(QWidget):
    def __init__(self, master=None):
        super().__init__(parent=master)
        layout = QGridLayout()
        self.figure_view = FigureCanvas(Figure(figsize=(10, 6)))
        self.prj_view = ProjectView(parent=self)
        ax = self.figure_view.figure.add_subplot(111)
        ax.plot([1, 23, 44], [23, 45, 65])
        layout.addWidget(self.prj_view, 0, 0)
        layout.addWidget(self.figure_view, 0, 1)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 3)
        self.setLayout(layout)

    def refesh_figure(self):
        pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.statusBar()
        self.createActions()
        self.setWindowTitle('QtXRD')
        self.setWindowIcon(QIcon('../assets/bird.ico'))
        self.mainView = MainView(self)
        self.setCentralWidget(self.mainView)
        self.createMenuBar()
        self.addToolBar(Qt.TopToolBarArea, NavigationToolbar2QT(self.mainView.figure_view, self))
        self.resize(1500, 800)

    def createActions(self):
        self.action_file_import = self.createAction('Import', self.import_data, './assets/import.ico', 'Ctrl+I',
                                                    'import xrd data')
        self.action_file_save = self.createAction('Save', self.save_project, './assets/save.ico', 'Ctrl+S',
                                                  'Save Project')
        self.action_file_open = self.createAction('Open', self.open_project, './assets/prj.ico', 'Ctrl+O', 'Open Project')
        self.action_file_exit = self.createAction('Exit', qApp.quit, 'assets/exit.ico', None, 'Quit')

        self.action_help_about = self.createAction('About', self.on_help_about, None, None, None)

        self.action_help_document = self.createAction('Document', self.on_help_document, 'assets/doc.ico', 'Ctrl+H',
                                                      'document')

        self.action_analysis_calculation = self.createAction('Calculation', self.on_analysis_calculation, None, None,
                                                             None)
        self.action_analysis_filter = self.createAction('Filter', self.on_analysis_filter, None, None, None)

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

    def open_project(self):
        print('open project')

    def import_data(self):
        print('import data')

    def save_project(self):
        print('save project')

    def on_help_about(self):
        msg = HelpAboutView()
        msg.exec()


    def on_help_document(self):
        print('help document')

    def on_analysis_filter(self):
        print('analysis filter')

    def on_analysis_dislocations(self):
        print('analysis dislocations')

    def on_analysis_calculation(self):
        print('analysis calculation')

    def createMenuBar(self):
        file_menu = self.menuBar().addMenu('File')
        file_menu.addAction(self.action_file_open)
        file_menu.addAction(self.action_file_import)
        file_menu.addAction(self.action_file_save)
        file_menu.addSeparator()
        file_menu.addAction(self.action_file_exit)

        analysis_menu = self.menuBar().addMenu('Analysis')
        analysis_menu.addAction(self.action_analysis_calculation)
        analysis_menu.addAction(self.action_analysis_filter)

        help_menu = self.menuBar().addMenu('Help')
        help_menu.addAction(self.action_help_document)
        help_menu.addAction(self.action_help_about)
