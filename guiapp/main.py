import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setWindowTitle('Log In')
        self.setMinimumWidth(300)

        labelUsername = QLabel("Username")
        self.txtUsername = QLineEdit()
        labelPassword = QLabel("Password")
        self.txtPassword = QLineEdit()
        self.login_button = QPushButton('Ok', self)

        self.formLayout = QFormLayout()
        self.formLayout.addRow(labelUsername, self.txtUsername)
        self.formLayout.addRow(labelPassword, self.txtPassword)
        self.formLayout.addRow(self.login_button)

        self.setLayout(self.formLayout)


class MainWindow(QMainWindow):
    """ Main window class
    """
    def __init__(self):
        """ Constructor function
        """
        QMainWindow.__init__(self)
        self.setWindowTitle("Thai Elderly Information System")
        self.setMinimumWidth(800)

        self.statusBar = QStatusBar()
        self.statusBar.showMessage('Ready', 2000)
        self.setStatusBar(self.statusBar)
        self.setupComponents()
        self.MdiArea = QMdiArea()
        self.setCentralWidget(self.MdiArea)

    def setupComponents(self):
        """ Setup status bar, central widget, menu bar
        """
        self.createActions()
        self.createMenus()
        self.formMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.exitFileAction)
        self.loginMenu.addAction(self.loginAction)

    # Slots called when the menu actions are triggered
    def newForm(self):
        pass

    def exitFile(self):
        self.close()

    def create_login_form(self):
        print('Building a form..')
        form = Form()
        self.MdiArea.addSubWindow(form)
        form.show()
        return form

    def createActions(self):
        """ Function to create actions for menu
        """
        self.newAction = QAction('&New',
                self, statusTip="New form",
                triggered=self.newForm)
        self.exitFileAction = QAction('&Exit',
                self, statusTip="Exit program",
                triggered=self.exitFile)
        self.loginAction = QAction('&Login',
                self, statusTip="Login",
                triggered=self.login)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu('&File')
        self.formMenu = self.menuBar().addMenu('F&orm')
        self.loginMenu = self.menuBar().addMenu('&Login')

    def activeMdiChild(self):
        activeSubWindow = self.MdiArea.activeSubWindow()
        if activeSubWindow:
            return activeSubWindow.widget()
        return None

    def login(self):
        self.form = self.create_login_form()
        self.form.login_button.clicked.connect(self.hello)

    def hello(self):
        print('Name: ', self.form.txtUsername.text())
        print('Password: ', self.form.txtPassword.text())
        self.form.parentWidget().close()


if __name__=='__main__':
    myApp = QApplication(sys.argv)
    myWidget = MainWindow()
    myWidget.show()
    myApp.exec_()
