import os
import sys
from basewindow import BaseWindow
from basewindow import *

from xml.etree.ElementTree import ElementTree
import xml.etree.ElementTree as ET
from dicttoxml import dicttoxml

import sip

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



class Notes(BaseWindow):
    def __init__(self, parent=BaseWindow):
        super().__init__(parent)

        self.launch = BaseWindow(self)
        self.launch.show()

        #icon dictionaries
        self.list_icons_dict = {}
        self.tabwidget_icons_dict = {}



        self.addNoteAction.triggered.connect(self.itemMenu)





        self.BaseWindow.listc.itemClicked.connect(self.list_clicked)

        self.stack.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.stack.customContextMenuRequested.connect(self.tabMenu)







    def list_clicked(self):
        self.item = self.list.currentItem()
        self.index = self.list.currentIndex()

        self.x = self.stack.findChild(QTabWidget, self.item.text())
        self.stack.setCurrentWidget(self.x)

    def tabContents(self):
        self.dialog = QDialog()

        self.layout = QFormLayout()

        # content_type = ['RichText', 'Canvas']
        # self.cb = QComboBox()
        # self.cb.addItems(content_type)

        self.label = QLabel("Enter tab name here:")

        self.le_text = QLineEdit()

        self.btn_icon = QPushButton('Choose Icon')
        self.btn_icon.clicked.connect(self.tab_ok)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.tab_ok)
        buttonBox.rejected.connect(self.cancel)

        self.dialog.setLayout(self.layout)
        self.layout.addRow(self.label)
        self.layout.addRow(self.le_text)
        self.layout.addRow(self.cb)
        self.layout.addRow(self.btn_icon)
        self.layout.addRow(buttonBox)

        self.dialog.show()


    def itemMenu(self):
        self.item_dialog = QDialog()

        self.layout_item = QFormLayout()

        inst_label = QLabel("Enter Your Category Item:")

        self.le_item = QLineEdit()

        btn_listIcon = QPushButton('Choose Icon')
        btn_listIcon.clicked.connect(self.item_ok)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.item_ok)
        buttonBox.rejected.connect(self.cancel)

        self.item_dialog.setLayout(self.layout_item)
        self.layout_item.addRow(inst_label)
        self.layout_item.addRow(self.le_item)
        self.layout_item.addRow(btn_listIcon)
        self.layout_item.addRow(buttonBox)

        self.item_dialog.show()


    def item_ok(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'images\icons')
        fname = str(fname[0])


        #print(fname)

        if fname != False:

            self.ico = QIcon()
            #self.ico.setObjectName('pug')
            self.ico_path = fname
            #print(self.ico.objectName())
            self.ico.addPixmap(QPixmap(fname))
            item = QListWidgetItem()
            item.setIcon(self.ico)
            item_text = self.le_item.text()
            item.setText(item_text)
            self.list.addItem(item)
            self.tab_widget = QTabWidget()
            self.tab_widget.setMovable(True)
            #self.tab_widget.addTab(QWidget(), self.default_icon, item_text)
            self.tab_widget.setObjectName(item_text)
            self.stack_widget.addWidget(self.tab_widget)

            self.list_icons_dict[item_text] = fname
            print(self.list_icons_dict)
            #self.tabwidget_icons_dict[self.tab_widget.objectName()] = #nested dict here (tabnames:filepath)

            #print('list icons:','\n' ,self.list_icons_dict.items())
            #print(self.tabwidget_icons_dict.items())

        self.item_dialog.close()

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)

        addListItem = contextMenu.addAction('Add List Item')
        deleteListItem = contextMenu.addAction('Delete List Item')
        renameListItem = contextMenu.addAction('Rename List Item')
        save = contextMenu.addAction('Save')


        action = contextMenu.exec_(self.listc.mapToGlobal(event.pos()))

        if action == addListItem:
            self.itemMenu()
        elif action == deleteListItem:
            self.item = self.list.currentItem()
            self.y = self.list.takeItem(self.lb.row(self.item))#pops the list item out
            #self.r = self.stacked_widget.removeWidget(self.tab_widget.currentWidget())
            self.r = self.stack.findChild(QTabWidget, self.item.text())
            sip.delete(self.r)
        elif action == renameListItem:
            newItemName, ok = QInputDialog.getText(self.lb, 'Input Dialog','List Item Name:')
            if ok:
                self.item = self.list.currentItem()
                self.curr_item = self.stack.findChild(QTabWidget, self.item.text())
                self.curr_item.setObjectName(newItemName)
                self.item.setText(newItemName)
        elif action == save:
            print("okaaayyyyyyyydyfydfydfydfydfy")
            # self.save()
            # self.print()



def main():
    app = QApplication(sys.argv)

    main = BaseWindow()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()