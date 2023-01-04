import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QMessageBox
from PyQt5.QtGui import QIcon
from MainWindow import Ui_MainWindow
from pg import w
from side import listen_etas




class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_get.clicked.connect(self.showinfo)
        self.ui.btn_scrape.clicked.connect(self.start)
        self.ui.btn_stop1.clicked.connect(self.stop1)
        self.count = 0
        self.URL = ""



    def showinfo(self):
        self.count += 1        
        print("COUNT", self.count)
        print(w)

    def start(self):
        listen_etas.start()
        self.ui.btn_scrape.setEnabled(False)
        self.ui.btn_stop1.setEnabled(True)
    
    def stop1(self):
        
        listen_etas.join()
        self.ui.btn_scrape.setEnabled(True)
        self.ui.btn_stop1.setEnabled(False)

    def resetURL(self):
        self.ui.text1.setText("")



def app():
    app = QtWidgets.QApplication(sys.argv)
    win = App()    
    win.show()
    sys.exit(app.exec_())



app()    











