import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QMainWindow, QToolBar, QSplitter, QFrame, QHBoxLayout, QAbstractItemView, QWidget, QAction, QStackedWidget, QListWidget)



class Notes(object):
    def __init__(self):
        super(Notes).__init__()


    def setupUi(self, MainWindow):

        menubar = MainWindow.menuBar()


        menu_file = menubar.addMenu("File")
        menu_edit = menubar.addMenu("Edit")
        menu_view = menubar.addMenu("View")
        menu_view = menubar.addMenu("Export")

        menu_file_action = QAction("New File", MainWindow)
        menu_file.addAction(menu_file_action)
        #menu_file_action.triggered.connect(self.newFile)
        #menu_file.addAction(self.newFile)
        



        self.toolbar = QToolBar(MainWindow)
        MainWindow.addToolBar(self.toolbar)

        self.addnew = QAction(QIcon("icons/notebook.png"), "Add New Nobebook", MainWindow)
        
        self.toolbar.addAction(self.addnew)

        self.newFile = QAction(QIcon("icons/new.png"), "Create New Note File", MainWindow)
        
        self.toolbar.addAction(self.newFile)

        self.printcfg = QAction(QIcon("icons/print.png"), "print", MainWindow)
        
        self.toolbar.addAction(self.printcfg)

        self.openAction = QAction(QIcon("icons/open.png"), "open notes file", MainWindow)
        
        self.toolbar.addAction(self.openAction)

        self.copyAction = QAction(QIcon("icons/copy.png"), "copy text", MainWindow)
        
        self.toolbar.addAction(self.copyAction)

        self.pasteAction = QAction(QIcon("icons/paste.png"), "paste text", MainWindow)
        
        self.toolbar.addAction(self.pasteAction)

        self.cutAction = QAction(QIcon("icons/paste.png"), "paste text", MainWindow)
        
        self.toolbar.addAction(self.cutAction)

        self.undoAction = QAction(QIcon("icons/undo.png"), "undo", MainWindow)
        
        self.toolbar.addAction(self.undoAction)

        self.redoAction = QAction(QIcon("icons/redo.png"), "redo", MainWindow)
        
        self.toolbar.addAction(self.redoAction)

        self.leftAlign = QAction(QIcon("icons/align-left.png"), "align left", MainWindow)
        
        self.toolbar.addAction(self.leftAlign)

        self.rightAlign = QAction(QIcon("icons/align-right.png"), "align right", MainWindow)
        
        self.toolbar.addAction(self.rightAlign)

        self.centerAlign = QAction(QIcon("icons/align-center.png"), "align center", MainWindow)
        
        self.toolbar.addAction(self.centerAlign)

        self.justifyAlign = QAction(QIcon("icons/align-justify.png"), "align justify", MainWindow)
        
        self.toolbar.addAction(self.justifyAlign)

        self.dateAction = QAction(QIcon("icons/calender.png"), "insert date", MainWindow)
        
        self.toolbar.addAction(self.dateAction)

        self.timeAction = QAction(QIcon("icons/time.png"), "insert time", MainWindow)
        
        self.toolbar.addAction(self.timeAction)

        self.tableAction = QAction(QIcon("icons/table.png"), "insert table", MainWindow)
        
        self.toolbar.addAction(self.tableAction)

        self.bulletAction = QAction(QIcon("icons/bullet.png"), "insert bulleted list", MainWindow)
        
        self.toolbar.addAction(self.bulletAction)

        self.numberAction = QAction(QIcon("icons/number.png"), "insert numbered list", MainWindow)
        
        self.toolbar.addAction(self.numberAction)

        self.imageAction = QAction(QIcon("icons/image.png"), "insert image", MainWindow)
        
        self.toolbar.addAction(self.imageAction)

        self.fontcolorAction = QAction(QIcon("icons/font-color.png"), "Select font color", MainWindow)
        
        self.toolbar.addAction(self.fontcolorAction)

        self.fontBackgroundAction = QAction(QIcon("icons/highlight.png"), "Select font background color", MainWindow)
        
        self.toolbar.addAction(self.fontBackgroundAction)

        self.fontAction = QAction(QIcon("icons/font.png"), "Choose Font", MainWindow)
        
        self.toolbar.addAction(self.fontAction)


        
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName('central')
        
        

        self.splitter = QSplitter(self.central_widget)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setStretchFactor(0,25)
        self.splitter.setStretchFactor(1,75)




        self.list = QListWidget(self.splitter)
        self.list.setObjectName("List")
        self.list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.list.setAlternatingRowColors(True)
        
        self.list.setAcceptDrops(True)
        self.list.setDragDropMode(QAbstractItemView.InternalMove)
        self.list.setDragEnabled(True)
        



        self.stack = QStackedWidget(self.splitter)
        self.stack.setObjectName("Stack")
        self.stack.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        

        self.listFrame = QFrame()
        self.stackFrame = QFrame() #maybe delete this

        self.splitter.addWidget(self.list)
        self.splitter.addWidget(self.stack)

        self.splitter.setSizes([50, 650])

####################################################################################################################




        self.boxlayout = QHBoxLayout()        
        self.central_widget.setLayout(self.boxlayout)
        MainWindow.setCentralWidget(self.central_widget)

        self.boxlayout.addWidget(self.splitter)
        MainWindow.show()
