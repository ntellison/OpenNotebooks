##################################################
# ellison.nt@gmail.com #
##################################################
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


        self.menu_file = menubar.addMenu("File")
        self.menu_edit = menubar.addMenu("Edit")
        self.menu_format = menubar.addMenu("Format")
        self.menu_help = menubar.addMenu("Help")
        #self.menu_view = menubar.addMenu("Export")


        # menubar file menu

        self.menu_file_action = QAction("New File", MainWindow)
        self.menu_file.addAction(self.menu_file_action)

        self.new_notebook_action = QAction("New Notebook", MainWindow)
        self.menu_file.addAction(self.new_notebook_action)

        self.open_file_action = QAction("Open an existing file", MainWindow)
        self.menu_file.addAction(self.open_file_action)

        self.save_file_action = QAction("Save File", MainWindow)
        self.menu_file.addAction(self.save_file_action)

        # menubar edit menu

        self.undo_edit_action = QAction("Undo", MainWindow)
        self.menu_edit.addAction(self.undo_edit_action)

        self.redo_edit_action = QAction("Redo", MainWindow)
        self.menu_edit.addAction(self.redo_edit_action)

        self.copy_edit_action = QAction("Copy", MainWindow)
        self.menu_edit.addAction(self.copy_edit_action)

        self.cut_edit_action = QAction("Cut", MainWindow)
        self.menu_edit.addAction(self.cut_edit_action)

        self.paste_edit_action = QAction("Paste", MainWindow)
        self.menu_edit.addAction(self.paste_edit_action)

        self.image_edit_action = QAction("Insert an Image", MainWindow)
        self.menu_edit.addAction(self.image_edit_action)

        self.table_edit_action = QAction("Insert a Table", MainWindow)
        self.menu_edit.addAction(self.table_edit_action)

        self.time_edit_action = QAction("Insert the current Time", MainWindow)
        self.menu_edit.addAction(self.time_edit_action)

        self.date_edit_action = QAction("Insert the current Date", MainWindow)
        self.menu_edit.addAction(self.date_edit_action)


        # menubar format menu

        self.fontcolor_format_action = QAction("Choose font color", MainWindow)
        self.menu_format.addAction(self.fontcolor_format_action)

        self.fontbgcolor_format_action = QAction("Choose font Background Color", MainWindow)
        self.menu_format.addAction(self.fontbgcolor_format_action)

        self.font_format_action = QAction("Choose font", MainWindow)
        self.menu_format.addAction(self.font_format_action)

        self.leftalign_format_action = QAction("Align Text Left", MainWindow)
        self.menu_format.addAction(self.leftalign_format_action)

        self.centeralign_format_action = QAction("Align Text Center", MainWindow)
        self.menu_format.addAction(self.centeralign_format_action)

        self.rightalign_format_action = QAction("Align Text Right", MainWindow)
        self.menu_format.addAction(self.rightalign_format_action)

        self.alignjustify_format_action = QAction("Align Text Justify", MainWindow)
        self.menu_format.addAction(self.alignjustify_format_action)


        # menubar export menu




        self.toolbar = QToolBar(MainWindow)
        MainWindow.addToolBar(self.toolbar)



        self.addnew = QAction(QIcon("icons/notebookgrey.png"), "Add New Nobebook", MainWindow)

        self.addnew.setShortcut('Ctrl+N')
        
        self.toolbar.addAction(self.addnew)

        self.addtab = QAction(QIcon("icons/tabtest"), "Add New Tab", MainWindow)

        self.addtab.setShortcut('Ctrl+T')
        
        self.toolbar.addAction(self.addtab)

        self.toolbar.addSeparator()

        self.saveAction = QAction(QIcon("icons/save.png"), "Save Current Note File", MainWindow)

        self.saveAction.setShortcut('Ctrl+S')

        self.toolbar.addAction(self.saveAction)

        self.newFile = QAction(QIcon("icons/new.png"), "Create New Note File", MainWindow)

        self.newFile.setShortcut('Ctrl+Shift+N')
        
        self.toolbar.addAction(self.newFile)

        self.openAction = QAction(QIcon("icons/open.png"), "open notes file", MainWindow)

        self.openAction.setShortcut('Ctrl+O')
        
        self.toolbar.addAction(self.openAction)

        self.toolbar.addSeparator()

        self.undoAction = QAction(QIcon("icons/undo.png"), "undo", MainWindow)

        self.undoAction.setShortcut('Ctrl+Z')
        
        self.toolbar.addAction(self.undoAction)

        self.redoAction = QAction(QIcon("icons/redo.png"), "redo", MainWindow)

        self.redoAction.setShortcut('Ctrl+Alt+Z')
        
        self.toolbar.addAction(self.redoAction)        



        self.printcfg = QAction(QIcon("icons/pdf.png"), "print", MainWindow)
        
        self.toolbar.addAction(self.printcfg)



        self.toolbar.addSeparator()    


        self.copyAction = QAction(QIcon("icons/copy.png"), "copy text", MainWindow)

        self.copyAction.setShortcut('Ctrl+C')
        
        self.toolbar.addAction(self.copyAction)

        self.pasteAction = QAction(QIcon("icons/paste.png"), "paste text", MainWindow)

        self.pasteAction.setShortcut('Ctrl+V')
        
        self.toolbar.addAction(self.pasteAction)

        self.cutAction = QAction(QIcon("icons/cut.png"), "cut text", MainWindow)

        self.cutAction.setShortcut('Ctrl+X')
        
        self.toolbar.addAction(self.cutAction)


        self.toolbar.addSeparator()


        self.leftAlign = QAction(QIcon("icons/alignleft.png"), "align left", MainWindow)
        
        self.toolbar.addAction(self.leftAlign)

        self.rightAlign = QAction(QIcon("icons/alignright.png"), "align right", MainWindow)
        
        self.toolbar.addAction(self.rightAlign)

        self.centerAlign = QAction(QIcon("icons/center.png"), "align center", MainWindow)
        
        self.toolbar.addAction(self.centerAlign)

        self.justifyAlign = QAction(QIcon("icons/justify.png"), "align justify", MainWindow)
        
        self.toolbar.addAction(self.justifyAlign)


        self.toolbar.addSeparator()


        self.dateAction = QAction(QIcon("icons/calendar.png"), "insert date", MainWindow)

        self.dateAction.setShortcut('Ctrl+Alt+D')
        
        self.toolbar.addAction(self.dateAction)

        self.timeAction = QAction(QIcon("icons/clock.png"), "insert time", MainWindow)

        self.timeAction.setShortcut('Ctrl+Alt+T')
        
        self.toolbar.addAction(self.timeAction)



        self.toolbar.addSeparator()


        self.bulletAction = QAction(QIcon("icons/bullets.png"), "insert bulleted list", MainWindow)

        self.bulletAction.setShortcut('Ctrl+B')
        
        self.toolbar.addAction(self.bulletAction)

        self.numberAction = QAction(QIcon("icons/numbers.png"), "insert numbered list", MainWindow)

        self.numberAction.setShortcut('Alt+N')
        
        self.toolbar.addAction(self.numberAction)


        self.toolbar.addSeparator()



        self.tableAction = QAction(QIcon("icons/table.png"), "insert table", MainWindow)

        self.tableAction.setShortcut('Ctrl+Shift+T')
        
        self.toolbar.addAction(self.tableAction)

        self.imageAction = QAction(QIcon("icons/image.png"), "insert image", MainWindow)

        self.imageAction.setShortcut('Ctrl+Alt+I')
        
        self.toolbar.addAction(self.imageAction)


        self.toolbar.addSeparator()



        self.fontcolorAction = QAction(QIcon("icons/fontcolor.png"), "Select font color", MainWindow)

        self.fontcolorAction.setShortcut('Ctrl+Shift+C')
        
        self.toolbar.addAction(self.fontcolorAction)

        self.fontBackgroundAction = QAction(QIcon("icons/highlight.png"), "Select font background color", MainWindow)

        self.fontBackgroundAction.setShortcut('Ctrl+Alt+C')
        
        self.toolbar.addAction(self.fontBackgroundAction)

        self.fontAction = QAction(QIcon("icons/text.png"), "Choose Font", MainWindow)

        self.fontAction.setShortcut('Ctrl+F')
        
        self.toolbar.addAction(self.fontAction)

        self.HRAction = QAction(QIcon("icons/hr.png"), "Insert Horizontal Rule", MainWindow)

        self.HRAction.setShortcut('Ctrl+L')

        self.toolbar.addAction(self.HRAction)

        # start markdown section of toolbar

        self.toolbar.addSeparator()

        self.markdownEditToggle = QAction(QIcon("icons/hr.png"), "Toggle Markdown Modes", MainWindow)

        self.toolbar.addAction(self.markdownEditToggle)

        
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
