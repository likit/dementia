import os, urllib, sys, time, json

from PySide.QtGui import *
from PySide.QtWebKit import *
from PySide.QtCore import *

from app import create_app

class WebApp(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    def setApplication(self, app, setup_callback):
        self.application = app
        self.setup_callback = setup_callback

    def run(self):
        self.setup_callback()
        self.application.run(use_debugger=True,
                debug=True, use_reloader=False, port=5000)


def main():
    global web, env

    # Init flask server
    webappThread = WebApp()
    def setup_callback():
        pass

    application = create_app('default')
    webappThread.setApplication(application, setup_callback)
    webappThread.start()

    app = QApplication(sys.argv)


    # Setup webkit
    web = QWebView()
    web.load(QUrl('http://localhost:5000'))
    web.resize(992, 800)
    web.setWindowTitle('Thai Elderly Database')
    web.show()
    app.exec_()


if __name__=='__main__':
    main()
