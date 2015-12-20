import sys
from PySide.QtCore import *
from PySide.QtGui import *

class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setWindowTitle('Main Form')
        self.setMinimumWidth(400)
        add_date_btn = QPushButton('Collect Date')
        vbox = QVBoxLayout()
        vbox.addWidget(add_date_btn)
        self.setLayout(vbox)

        add_date_btn.clicked.connect(self.open_date_dialog)

    def open_date_dialog(self):
        print("Opening date dialog ...")


class LoginForm(QWidget):
    def __init__(self):
        super(LoginForm, self).__init__()
        self.setWindowTitle('Log In')
        self.setMinimumWidth(300)

        label_username = QLabel("Username")
        self.text_username = QLineEdit()
        label_password = QLabel("Password")
        self.text_password = QLineEdit()
        self.login_button = QPushButton('Ok', self)

        self.form_layout = QFormLayout()
        self.form_layout.addRow(label_username, self.text_username)
        self.form_layout.addRow(label_password, self.text_password)
        self.form_layout.addRow(self.login_button)

        self.setLayout(self.form_layout)


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
        self.setup_components()
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

    def setup_components(self):
        """ Setup status bar, central widget, menu bar
        """
        self.create_actions()
        self.create_menus()
        self.form_menu.addAction(self.newform_act)
        self.file_menu.addAction(self.exit_act)
        self.login_menu.addAction(self.login_act)

    # Slots called when the menu actions are triggered
    def new_form(self):
        print('Creating a form..')
        self.form = MainForm()
        self.form.show()

    def exit(self):
        self.close()

    def create_login_form(self):
        print('Building a form..')
        login_form = LoginForm()
        self.mdi_area.addSubWindow(login_form)
        login_form.show()
        return login_form

    def create_actions(self):
        """ Function to create actions for menu
        """
        self.newform_act = QAction('&New',
                self, statusTip="New form",
                triggered=self.new_form)
        self.exit_act = QAction('&Exit',
                self, statusTip="Exit program",
                triggered=self.exit)
        self.login_act = QAction('&Login',
                self, statusTip="Login",
                triggered=self.login)

    def create_menus(self):
        self.file_menu = self.menuBar().addMenu('&File')
        self.form_menu = self.menuBar().addMenu('F&orm')
        self.login_menu = self.menuBar().addMenu('&Login')

    def activeMdiChild(self):
        activeSubWindow = self.mdi_area.activeSubWindow()
        if activeSubWindow:
            return activeSubWindow.widget()
        return None

    def login(self):
        self.login_form = self.create_login_form()
        self.login_form.login_button.clicked.connect(self.hello)

    def hello(self):
        print('Name: ', self.login_form.text_username.text())
        print('Password: ', self.login_form.text_password.text())
        self.login_form.parentWidget().close()


if __name__=='__main__':
    qapp = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    qapp.exec_()
