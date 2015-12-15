# -*- coding: utf-8 -*-
import time
import sys, time
from PySide import QtGui

class MainWindow(QtGui.QMainWindow):
    '''Main window class'''
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle("Main Window")
        self.setGeometry(300, 250, 400, 300)
        self.status_label = QtGui.QLabel('Showing Progress')
        # self.progress_bar = QProgressBar()
        # self.progress_bar.setMinimum(0)
        # self.progress_bar.setMaximum(100)

        self.workspace = QtGui.QMdiArea()
        self.setCentralWidget(self.workspace)

    def create_status_bar(self):
        self.status_bar = QtGui.QStatusBar()
        # self.progress_bar.setValue(0)
        self.status_bar.addWidget(self.status_label, 1)
        # self.status_bar.addWidget(self.progress_bar, 2)
        self.status_bar.showMessage(u'สถานะ: พร้อม', 2000)
        self.setStatusBar(self.status_bar)

    def setup_components(self):
        self.create_actions()
        self.create_menus()
        self.file_menu.addAction(self.new_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.edit_action)

    def new_file(self):
        form = QtGui.QWidget()
        formLayout = QtGui.QFormLayout()
        labelUsername = QtGui.QLabel("Username")
        txtUsername = QtGui.QLineEdit()
        labelPassword = QtGui.QLabel("Password")
        txtPassword = QtGui.QLineEdit()
        formLayout.addRow(labelUsername, txtUsername)
        formLayout.addRow(labelPassword, txtPassword)
        form.setLayout(formLayout)
        self.workspace.addSubWindow(form)
        form.show()

    def edit_file(self):
        self.workspace.closeActiveSubWindow()

    def create_actions(self):
        self.new_action = QtGui.QAction('&New', self, shortcut=QtGui.QKeySequence.New,
                statusTip="Create a new file", triggered=self.new_file)
        self.edit_action = QtGui.QAction('E&dit', self,
                                    statusTip="Edit the application",
                                    triggered=self.edit_file)

    def create_menus(self):
        self.file_menu = self.menuBar().addMenu("&File")

    def show_progress(self):
        while(self.progress_bar.value() < self.progress_bar.maximum()):
            self.progress_bar.setValue(self.progress_bar.value() + 10)
            time.sleep(1)
        self.status_label.setText('Ready')

if __name__=='__main__':
    try:
        myApp = QtGui.QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.setup_components()
        mainWindow.create_status_bar()
        mainWindow.show()
        # mainWindow.show_progress()
        mainWindow.new_file()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print('Name Error:', sys.exc_info()[1])
    except SystemExit:
        print('Closing Window...')
    except Exception:
        print(sys.exc_info()[1])
