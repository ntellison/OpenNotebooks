import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QAction, QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGraphicsScene,
                             QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QListWidget, QMainWindow, QMenu, QPlainTextEdit,
                             QPushButton, QStackedWidget, QTabWidget,
                             QVBoxLayout, QWidget, QSplitter)


from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QApplication, QMainWindow, QFormLayout, QLineEdit, QTabWidget, QWidget, QAction, QPushButton,
                            QLabel, QVBoxLayout, QPlainTextEdit, QStackedWidget, QComboBox, QListWidget, QMenu, QAction, QGroupBox, QDialogButtonBox, QGraphicsScene)
from PyQt5 import QtCore
from PyQt5.QtCore import QEvent
from PyQt5 import QtGui, QtWidgets, QtCore



class BaseWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)


    
        self.init_ui()
        # self.initMenubar()
        # self.initToolbar()

    

    def initMenubar(self):

        menubar = self.menuBar()


        menu_file = menubar.addMenu("File")
        menu_edit = menubar.addMenu("Edit")
        menu_view = menubar.addMenu("View")
        menu_view = menubar.addMenu("Export")
        


    def initToolbar(self):


        self.toolbar = self.addToolBar("Toolbar")

        self.addNoteAction = QAction(self)

        self.toolbar.addAction(self.addNoteAction)
        



    def init_ui(self):

        self.listc = QListWidget()
        self.listc.setObjectName("List")
        self.listc.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listc.setAcceptDrops(True)
        self.listc.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listc.setDragEnabled(True)



        self.stack = QStackedWidget()
        self.stack.setObjectName("Stack")

        self.listFrame = QFrame()
        self.stackFrame = QFrame() #maybe delete this



        self.splitter = QSplitter(Qt.Horizontal)
        #self.splitter.addWidget(self.listFrame)
        self.splitter.addWidget(self.listc)        
        self.splitter.addWidget(self.stackFrame)
        self.splitter.addWidget(self.stack)


        self.splitter.setStretchFactor(1,1)

        

        self.initMenubar()
        self.initToolbar()

        self.centralWidget = QWidget()

        self.setCentralWidget(self.centralWidget)

        self.layout = QHBoxLayout()        
        self.centralWidget.setLayout(self.layout)

        # self.layout.addWidget(self.list)
        # self.layout.addWidget(self.stack)
        self.layout.addWidget(self.splitter)



        self.show()  








# def main():
#     app = QApplication(sys.argv)

#     main = BaseWindow()
#     main.show()

#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()
