# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QGridLayout, QWidget, \
    QMainWindow, QAction, \
    qApp, QFileDialog, QMessageBox
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

from xrd import utils
from xrd.backend.xrd_project import XrdProject
from xrd.backend.xrd_setting import XrdSetting
from xrd.view.HelpAboutView import HelpAboutView
from xrd.view.ProjectView import ProjectView

file_count = 1


def default_name():
    global file_count
    file_count = file_count + 1
    return "Untitiled-" + str(file_count)


class MainView(QWidget):
    def __init__(self, master=None):
        super().__init__(parent=master)
        layout = QGridLayout()
        self.figure_view = FigureCanvas(Figure(figsize=(10, 6)))
        self.prj_view = ProjectView(parent=self)
        ax = self.figure_view.figure.add_subplot(111)
        ax.plot([1, 23, 44], [23, 45, 6])
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
        self.setWindowTitle('QtXRD')
        self.setWindowIcon(QIcon('assets/bird.png'))
        self.statusBar()
        self.createActions()
        self.mainView = MainView(self)
        self.settings = XrdSetting()
        self.setCentralWidget(self.mainView)
        self.createMenuBar()
        self.addToolBar(Qt.TopToolBarArea, NavigationToolbar2QT(self.mainView.figure_view, self))

        self.resize(1500, 800)

    def createActions(self):
        self.action_file_new = self.createAction('New Project', self.on_file_new, None, 'Ctrl+N', None)
        self.action_file_import = self.createAction('Import', self.on_file_import, 'assets/import.png', 'Ctrl+I',
                                                    'import xrd data')
        self.action_file_save = self.createAction('Save', self.on_file_save, 'assets/save.png', 'Ctrl+S',
                                                  'Save Project')
        self.action_file_open = self.createAction('Open', self.on_file_open, 'assets/prj.png', 'Ctrl+O', 'Open Project')
        self.action_file_exit = self.createAction('Exit', qApp.quit, 'assets/exit.png', None, 'Quit')

        self.action_help_about = self.createAction('About', self.on_help_about, None, None, None)

        self.action_help_document = self.createAction('Document', self.on_help_document, 'assets/doc.png', 'Ctrl+H',
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

    def closeEvent(self, e):
        self.settings.save()
        if self.check_on_close():
            e.accept()
        else:
            e.ignore()

    def on_file_new(self):
        dlg = QFileDialog(self)
        dlg.setWindowTitle('Open Project')
        dlg.setAcceptMode(QFileDialog.AcceptSave)
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setNameFilter('XRD Project(*.xrdprj) ;; All Files (*)')
        if dlg.exec() == QFileDialog.Accepted:
            fname = dlg.selectedFiles()[0]
            if not fname.endswith('.xrdprj'):
                fname = fname + ".xrd.prj"
            if self.check_on_close():
                prj = XrdProject()
                prj.location = fname
                prj.label = default_name() + "[" + fname + "]"
                prj.name = prj.label
                self.projectView.currentProject = prj
                self.projectView.refresh()

    def check_on_close(self):
        if self.projectView.currentProject is not None and self.projectView.currentProject.saved is False:
            dlg = QMessageBox(self)
            dlg.setText('This project has been modified.')
            dlg.setInformativeText("Do you want to save your changes?")
            dlg.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            dlg.setDefaultButton(QMessageBox.Save)
            ret = dlg.exec()
            if ret == QMessageBox.Save:
                self.projectView.currentProject.save()
                return True
            elif ret == QMessageBox.Cancel:
                return False
        return True

    def on_file_open(self):
        dlg = QFileDialog(self)
        dlg.setWindowTitle('Open Project')
        dlg.setAcceptMode(QFileDialog.AcceptOpen)
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setNameFilter('XRD Project(*.xrdprj) ;; All Files (*)')
        if dlg.exec() == QFileDialog.Accepted:
            fname = dlg.selectedFiles()[0]
            if not fname.endswith('.xrdprj'):
                fname = fname + '.xrdprj'
            self.open_project(fname)

    @property
    def projectView(self):
        return self.mainView.prj_view

    @property
    def figureView(self):
        return self.mainView.figure_view

    def open_project(self, prj_file):
        if self.projectView.currentProject is not None and self.projectView.currentProject.saved is False:
            dlg = QMessageBox(self)
            dlg.setText('This project has been modified.')
            dlg.setInformativeText("Do you want to save your changes?")
            dlg.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            dlg.setDefaultButton(QMessageBox.Save)
            ret = dlg.exec()
            if ret == QMessageBox.Save:
                self.projectView.currentProject.save()
            elif ret == QMessageBox.Cancel:
                return
        else:
            self.projectView.currentProject = utils.load(prj_file)
            self.projectView.refresh()

    def on_file_import(self):
        print('import data')

    def on_file_save(self):
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
        file_menu.addAction(self.action_file_new)
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
