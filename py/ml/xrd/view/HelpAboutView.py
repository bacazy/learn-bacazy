from PyQt5.QtWidgets import QDialog, QMessageBox


class HelpAboutView(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('About')
        self.setText("under GPLv3\n if any questions, please contact gc_zhangcheng@126.com")
        self.setContentsMargins(30, 30, 30, 30)
