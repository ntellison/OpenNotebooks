from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #{================================

        app.aboutToQuit.connect(self.closeEvent)

        #}================================

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle('Demo')

    #{================================

    def closeEvent(self):
        reply = QMessageBox.question(MainWindow, 'Message',
                                    "Are you sure to quit?", QMessageBox.Yes |
                                    QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            print('okeh')
            #shutil.rmtree(self.recentLoad)
            #event.accept()
            #sys.exit()
            

        else:
            print('cancelled')
            # maybesave function?
            
            #self.save()
            #event.ignore()



    # def closeEvent(self):
    #     #Your desired functionality here
    #     print('Close button pressed')
    #     import sys
    #     sys.exit(0)

    #}================================


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())