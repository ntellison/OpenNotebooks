import os
import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QApplication, QMainWindow, QFormLayout, QLineEdit, QTabWidget, QWidget, QAction, QPushButton,
                            QLabel, QVBoxLayout, QPlainTextEdit, QStackedWidget, QComboBox, QListWidget, QMenu, QAction, QGroupBox, QDialogButtonBox, QGraphicsScene, QCheckBox)
from PyQt5 import QtCore
from PyQt5.QtCore import QEvent, Qt
from PyQt5 import QtGui, QtWidgets, QtCore

import sip

from xml.etree.ElementTree import ElementTree
import xml.etree.ElementTree as ET

#import dicttoxml
from dicttoxml import dicttoxml



# here is a change made comment


class Notes(object):
    # def __init__(self):
    #     super(Notes, self).__init__()
    #     #QMainWindow.__init__(self)


        # self.list_icons_dict = {}
        # self.tabwidget_icons_dict = {}

        #self.init_ui()
        # self.initMenubar()
        # self.initToolbar()


    def setupUi(self, MainWindow):



        menubar = MainWindow.menuBar()


        menu_file = menubar.addMenu("File")
        menu_edit = menubar.addMenu("Edit")
        menu_view = menubar.addMenu("View")
        menu_view = menubar.addMenu("Export")
        




        # self.toolbar = QToolBar(MainWindow)
        self.toolbar = QToolBar(MainWindow)
        MainWindow.addToolBar(self.toolbar)
        self.addnew = QAction()
        self.addnew.triggered.connect(self.itemMenu)         
        self.toolbar.addAction(self.addnew) 


        
        central_widget = QWidget()

        self.splitter = QSplitter(central_widget)
        self.splitter.setOrientation(Qt.Horizontal)
        # self.splitter.addWidget(self.listc)        
        # self.splitter.addWidget(self.listFrame)        
        # self.splitter.addWidget(self.stack)               
        #self.splitter.addWidget(self.stackFrame)

        #self.splitter.setMinimumWidth(10)
        self.splitter.setStretchFactor(1,0)

        self.listc = QListWidget(self.splitter)
        self.listc.setObjectName("List")
        self.listc.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listc.setAcceptDrops(True)
        self.listc.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listc.setDragEnabled(True)
        self.listc.itemClicked.connect(self.list_clicked)



        self.stack = QStackedWidget(self.splitter)
        self.stack.setObjectName("Stack")
        self.stack.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.stack.customContextMenuRequested.connect(self.tabMenu)

        self.listFrame = QFrame()
        self.stackFrame = QFrame() #maybe delete this


        #self.splitter.setSizes([100,500])
        #self.splitter.setStretchFactor(1,100)
        # self.splitter.setStretchFactor(0,9)



####################################################################################################################




        self.boxlayout = QHBoxLayout()        
        central_widget.setLayout(self.boxlayout)
        MainWindow.setCentralWidget(central_widget)

        self.boxlayout.addWidget(self.splitter)


        #self.vlayout = QVBoxLayout()


        




        # self.boxlayout.addWidget(self.splitter)
        # self.boxlayout.addWidget(self.listc)
                
        # self.boxlayout.addWidget(self.stack)


        # self.boxlayout.addLayout(self.vlayout)
        # #self.vlayout.addLayout(self.boxlayout)



        


        # self.setLayout(self.vlayout)



######################################################################################################################


        #self.central_widget.setLayout(self.boxlayout)


        #self.l.addLayout(self.boxlayout)

        # self.central_layout = QVBoxLayout()


        # self.central_widget.setLayout(self.central_layout)

        # self.centralWidget = QWidget()

        # self.setCentralWidget(self.centralWidget)

        # self.layout = QHBoxLayout()
        # self.layout.addWidget(self.splitter)                
        # self.centralWidget.setLayout(self.layout)

        # self.layout.addWidget(self.listc)
        # self.layout.addWidget(self.stack)



        #self.initMenubar()


    def list_clicked(self):
        self.item = self.listc.currentItem()
        self.index = self.listc.currentIndex()

        self.x = self.stack.findChild(QTabWidget, self.item.text())
        self.stack.setCurrentWidget(self.x)




    def tabContents(self):
        self.dialog = QDialog()

        self.layout_tab = QFormLayout()

        # content_type = ['RichText', 'Canvas']
        # self.cb = QComboBox()
        # self.cb.addItems(content_type)

        self.label = QLabel("Enter tab name here:")

        self.le_text = QLineEdit()

        self.combo_tab = QCheckBox()
        self.combo_tab.stateChanged.connect(self.checkTabToggle)
        

        self.btn_icon = QPushButton('Choose Icon')
        self.btn_icon.clicked.connect(self.chooseTabIcon)
        self.btn_icon.setDisabled(True)

        self.le_tab_path = QLineEdit()
        self.le_tab_path.setReadOnly(True)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.tab_ok)
        buttonBox.rejected.connect(self.cancel)

        self.dialog.setLayout(self.layout_tab)
        self.layout_tab.addRow(self.label)
        self.layout_tab.addRow(self.le_text)
        self.layout_tab.addRow(self.combo_tab)
        #self.layout.addRow(self.cb)
        self.layout_tab.addRow(self.btn_icon)
        self.layout_tab.addRow(self.le_tab_path)
        self.layout_tab.addRow(buttonBox)

        self.dialog.show()

    def itemMenu(self):
        self.item_dialog = QDialog()

        self.layout_item = QFormLayout()

        inst_label = QLabel("Enter Your Category Item:")

        self.le_item = QLineEdit()

        self.check = QCheckBox()
        self.check.stateChanged.connect(self.checktoggle)

        self.btn_listIcon = QPushButton('Choose Icon')
        self.btn_listIcon.setEnabled(False)
        # btn_listIcon.clicked.connect(self.item_ok)
        self.btn_listIcon.clicked.connect(self.chooseListIcon)

        self.le_path = QLineEdit()
        self.le_path.setReadOnly(True)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.item_ok)
        buttonBox.rejected.connect(self.cancel)

        self.item_dialog.setLayout(self.layout_item) ## !!!!!!!!!PROBLEM WAS HERE!!!!!!!!!! was self.layout which was triggering the other main layout
        self.layout_item.addRow(inst_label)
        self.layout_item.addRow(self.le_item)
        self.layout_item.addRow(self.check)
        self.layout_item.addRow(self.btn_listIcon)
        self.layout_item.addRow(self.le_path)
        self.layout_item.addRow(buttonBox)



        self.item_dialog.show()

    def checkTabToggle(self):
        self.btn_icon.setEnabled(True)


    def checktoggle(self):
        self.btn_listIcon.setEnabled(True)

    


    def chooseListIcon(self):

        fname = QFileDialog.getOpenFileName(self, 'Open File', 'images\icons')
        fname = str(fname[0])
        self.item_filename = fname
        #self.le_filename = fname
        self.le_path.setText(fname)



    def item_ok(self):


            # fname = QFileDialog.getOpenFileName(self, 'Open File', 'images\icons')
            # fname = str(fname[0])
        

        #print(fname)
        self.checkInfo = self.check.isChecked()

        if self.checkInfo == False and self.le_item.text() != False:
            item = QListWidgetItem()
            item_text = self.le_item.text()
            item.setText(item_text)
            self.listc.addItem(item)
            self.tab_widget = QTabWidget()
            self.tab_widget.setMovable(True)
            self.tab_widget.setObjectName(item_text)
            self.stack.addWidget(self.tab_widget)


        elif self.checkInfo == True and self.le_item.text() != False:

            self.ico = QIcon()
            #self.ico.setObjectName('pug')
            self.ico_path = self.item_filename
            self.ico_path = self.item_filename
            #print(self.ico.objectName())
            self.ico.addPixmap(QPixmap(self.item_filename))
            item = QListWidgetItem()
            item.setIcon(self.ico)
            item_text = self.le_item.text()
            item.setText(item_text)
            self.listc.addItem(item)
            self.tab_widget = QTabWidget()
            self.tab_widget.setMovable(True)
            #self.tab_widget.addTab(QWidget(), self.default_icon, item_text)
            self.tab_widget.setObjectName(item_text)
            self.stack.addWidget(self.tab_widget)

            self.list_icons_dict[item_text] = self.item_filename
            print(self.list_icons_dict)
            #self.tabwidget_icons_dict[self.tab_widget.objectName()] = #nested dict here (tabnames:filepath)

            #print('list icons:','\n' ,self.list_icons_dict.items())
            #print(self.tabwidget_icons_dict.items())

        else:
            self.item_msg_box = QMessageBox(self, 'Message', 'Please Enter a title for ListItem', QMessageBox.Ok)
            self.item_dialog.close()

        self.item_dialog.close()


    def checktoggle(self):
        self.btn_icon.setEnabled(True)

    def chooseTabIcon(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'images\icons')
        fname = str(fname[0])
        self.tabicon_filename = fname
        self.le_tab_path.setText(fname)



    def tab_ok(self):

        self.check_tab_icon = self.combo_tab.isChecked()

        if self.check_tab_icon == False and self.le_text.text() != False:

            self.newTabName = self.le_text.text()            
            self.item = self.listc.currentItem()
            self.curr_tab_wid = self.stack.findChild(QTabWidget, self.item.text())
            self.curr_tab_wid.addTab(QTextEdit(), self.newTabName)

            self.tabwidget_icons_dict['tabwidget'] = {self.curr_tab_wid.objectName()}
            #self.tabwidget_icons_dict.update({self.newTabName:self.tab_ico})

        elif self.check_tab_icon == True and self.le_text.text() != False:

            # fname = QFileDialog.getOpenFileName(self, 'Open File', 'images\icons')
            # fname = str(fname[0])

            self.tab_ico = self.tabicon_filename


            self.ico = QIcon()
            self.ico.addPixmap(QPixmap(self.tab_ico), QIcon.Normal, QIcon.On)

            self.newTabName = self.le_text.text()            
            self.item = self.listc.currentItem()
            self.curr_tab_wid = self.stack.findChild(QTabWidget, self.item.text())
            self.curr_tab_wid.addTab(QTextEdit(), self.ico, self.newTabName)

            self.tabwidget_icons_dict['tabwidget'] = {self.curr_tab_wid.objectName()}
            self.tabwidget_icons_dict.update({self.newTabName:self.tab_ico})

        else:
            self.tab_msg_box = QMessageBox(self, 'Message', 'Please Enter a title for TAb', QMessageBox.Ok)
            self.dialog.close()

        #self.tab_content = self.cb.currentText()

        # if self.tab_content == 'RichText':
        #     self.curr_tab_wid.addTab(QTextEdit(), self.ico, self.newTabName)
        # elif self.tab_content == 'Canvas':
        #     self.curr_tab_wid.addTab(QGraphicsView(),self.ico, self.newTabName)

        # self.tabwidget_icons_dict['tabwidget'] = {self.curr_tab_wid.objectName()}
        # self.tabwidget_icons_dict.update({self.newTabName:self.tab_ico})
        print(self.tabwidget_icons_dict)
        self.dialog.close()





    def cancel(self):
        self.dialog.close()




    def tabMenu(self, event):
        self.tabContextMenu = QMenu()

        addTab = self.tabContextMenu.addAction('Add New Tab')
        deleteTab = self.tabContextMenu.addAction('Delete Tab')
        renameTab = self.tabContextMenu.addAction('Rename Tab')

        action = self.tabContextMenu.exec_(self.stack.mapToGlobal(event))

        if action == addTab:
            self.tabContents()
        if action == deleteTab:
            self.item = self.lb.currentItem()
            self.curr_tab_wid = self.stacked_widget.findChild(QTabWidget, self.item.text())
            self.curr_tab = self.curr_tab_wid.currentIndex()
            self.curr_tab_wid.removeTab(self.curr_tab)
        if action ==renameTab:
            tabRename, ok = QInputDialog.getText(self.tab_widget, 'Input Dialog', 'Enter new tab name')
            if ok:
                self.item = self.listc.currentItem()
                self.curr_tab_wid = self.stack.findChild(QTabWidget, self.item.text())
                self.curr_tab = self.curr_tab_wid.currentIndex()
                self.curr_tab_wid.setTabText(self.curr_tab, tabRename)








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




    def print(self):
        #self.tabwidget_icons_dict['tabwidget'] = self.curr_tab_wid.objectName() #nested dict here (tabnames:filepath)
        for i in self.stacked_widget.findChildren(QTabWidget):

            #self.tabwidget_icons_dict['tabwidget'] = i.objectName()
            #self.tabwidget_icons_dict['tabwidget'] = {}
            for j in range(i.count()):
                self.tabname = i.tabText(j)
                self.tabwidget_icons_dict[i.objectName()] = {}
                #self.tabwidget_icons_dict['tabwidget'][i.objectName()] = self.dict
                #self.tabwidget_icons_dict[i.objectName()] = self.dict
                #self.tabwidget_icons_dict[i.objectName()][self.tabname] = self.tab_ico
                #self.tabwidget_icons_dict[i.objectName()] = {self.tabname:self.tab_ico}
                #self.tabwidget_icons_dict[i.objectName()] = self.widget[self.tabname] = self.tab_ico
                #self.tabwidget_icons_dict[self.tabname] = self.tab_ico
                #self.tabwidget_icons_dict[self.newTabName] = self.tab_ico
        print(self.tabwidget_icons_dict.items())


    def save(self):
        root = ET.Element('programElements')
        tree = ElementTree(root)


        for i in range(self.lb.count()):
            self.x = self.lb.item(i).text()
            #self.y = self.lb.item(i).icon()
            listitem = ET.SubElement(root, 'listitem')
            print(self.list_icons_dict)
            self.licon = self.list_icons_dict[self.x]
            listitem.set('item_icon', self.licon)
            listitem.text = self.x
        for g in range(self.stacked_widget.count()):
            self.q = self.stacked_widget.widget(g)
            tabwidgetName = ET.SubElement(root, 'tabwid_name')
            tabwidgetName.text = self.q.objectName()
            for p in range(self.q.count()):
                self.tabtext = self.q.tabText(p)
                #self.tabicon = self.q.tabIcon(p)
                self.ticon = self.tabwidget_icons_dict[self.tabtext]
                self.tabcontents = type(self.q.widget(p))
                tabName = ET.SubElement(tabwidgetName, 'tabName')
                tabName.set('content', str(self.tabcontents))
                tabName.set('tabIcon', self.ticon)
                tabName.text = self.tabtext
                #self.tabwidget_icons_dict[tabwidgetName.text] = self.tabtext, self.tabwidget_icons_dict[#nested dict here (tabnames:filepath)
                #self.tabwidget_icons_dict[self.tabtext] =
        tree.write(open('config.xml', 'wb'))
        
        list_xml = dicttoxml(self.list_icons_dict, custom_root='listicons')
        tab_xml = dicttoxml(self.tabwidget_icons_dict, custom_root='tabicons')
        #xml = xml.decode()





    def load(self):
        try:
            filename = ET.parse('config.xml').getroot()
            #ico_fname = ET.parse('icons.xml').getroot()
        except:
            msg_box = QMessageBox.question(self, 'Message', 'No existing file', QMessageBox.Ok)
            if msg_box == QMessageBox.Ok:
                sys.exit()

        for listitem in filename.findall('listitem'):
            #self.lb.addItem(listitem.text)
            item = QListWidgetItem()
            icon = listitem.get('item_icon')
            self.ico = QIcon(icon)
            item.setIcon(self.ico)
            item.setText(listitem.text)
            self.lb.addItem(item)

            self.list_icons_dict[listitem.text] = icon

            #for i in range(self.lb.count()):
            
                #self.lb.item(i).addPixmap(str(icon))
            #self.item = self.lb.item(listitem)
            
            
            #li = self.lb.findChild(self.item(listitem))
            #self.li.setIcon(self.ico)
            #self.item.addPixmap(QPixmap(self.ico))
        for tabwidget in filename.iter('tabwid_name'):
            self.tab_widget = QTabWidget()
            self.tab_widget.setObjectName(tabwidget.text)
            self.tab_widget.setMovable(True)
            self.stacked_widget.addWidget(self.tab_widget)
            for tabname in tabwidget.iter('tabName'):
                self.id = self.stacked_widget.findChild(QTabWidget, tabwidget.text)
                self.tab_icon = tabname.get('tabIcon')
                self.tabico = QIcon(self.tab_icon)
                self.tabwidget_icons_dict[tabname.text] = self.tab_icon
                content = tabname.get('content')
                if 'QTextEdit' in str(content):
                    self.id.addTab(QTextEdit(), self.tabico, tabname.text)
                elif 'QGraphicsView' in str(content):
                    self.id.addTab(QGraphicsView(), self.tabico, tabname.text)
                elif 'QWidget' in str(content):
                    self.id.addTab(QWidget(), self.tabico ,tabname.text)



if __name__ == "__main__":

    application = QApplication(sys.argv)

    # window
    MainWindow = QMainWindow()
    ui = Notes()
    ui.setupUi(MainWindow)
    #ui.setWindowTitle('Notes')
    #ui.resize(1280, 720)
    #ui.show()
    MainWindow.show()

    sys.exit(application.exec_())


# def main():
#     app = QApplication(sys.argv)

#     main = Notes()
#     main.show()

#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()