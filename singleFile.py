import os
import sys
import subprocess

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage, QTextTable , QTextTableFormat, QTextListFormat, QFont
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFormLayout, QLineEdit, QTabWidget, QWidget, QAction, QPushButton,
                            QLabel, QVBoxLayout, QSpinBox, QPlainTextEdit, QStackedWidget, QComboBox, QListWidget, QMenu, QAction, QGroupBox, QDialogButtonBox, QGraphicsScene, QCheckBox, QMessageBox, QColorDialog)
from PyQt5 import QtCore
from PyQt5.QtCore import QEvent, Qt, QSize, QSettings, QDate, QTime
from PyQt5 import QtGui, QtWidgets, QtCore

import sip
import shutil


from xml.etree.ElementTree import ElementTree
import xml.etree.ElementTree as ET

#import dicttoxml
from dicttoxml import dicttoxml






class Notes(object):
    def __init__(self):
        super(Notes).__init__()
        
    #     super(Notes, self).__init__()
    #     #QMainWindow.__init__(self)
        #MainWindow.installEventFilter(MainWindow)
              

        self.list_icons_dict = {}
        self.tabwidget_icons_dict = {}

        self.listchanges = []
        self.tabchanges = []
        
        

        #self.noteSettings = QSettings('settings/noteapp.ini', QSettings.IniFormat)

        self.setupUi(MainWindow)
        self.load()

        #self.init_ui()
        # self.initMenubar()
        # self.initToolbar()
        


    def closeEvent(self, event):

        
        
        print('fuuuucccckkkkk')

        reply = QMessageBox.question(self, 'Message',
                                    "Are you sure to quit?", QMessageBox.Yes |
                                    QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            print('okeh')
            shutil.rmtree(self.recentLoad)
            sys.exit()
            event.accept()

        else:
            print('cancelled')
            # maybesave function?
            
            #self.save()
            event.ignore()






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
        




        # self.toolbar = QToolBar(MainWindow)
        self.toolbar = QToolBar(MainWindow)
        MainWindow.addToolBar(self.toolbar)

        self.addnew = QAction(QIcon("icons/notebook.png"), "Add New Nobebook", MainWindow)
        self.addnew.triggered.connect(self.itemMenu)         
        self.toolbar.addAction(self.addnew)

        self.newFile = QAction(QIcon("icons/new.png"), "Create New Note File", MainWindow)
        self.newFile.triggered.connect(self.newWindow)
        self.toolbar.addAction(self.newFile)

        self.printcfg = QAction(QIcon("icons/print.png"), "print", MainWindow)
        #self.printcfg.triggered.connect(self.print)
        self.toolbar.addAction(self.printcfg)

        self.openAction = QAction(QIcon("icons/open.png"), "open notes file", MainWindow)
        #self.openAction.triggered.connect(self.open)
        self.toolbar.addAction(self.openAction)

        self.copyAction = QAction(QIcon("icons/copy.png"), "copy text", MainWindow)
        self.copyAction.triggered.connect(self.copy)
        self.toolbar.addAction(self.copyAction)

        self.pasteAction = QAction(QIcon("icons/paste.png"), "paste text", MainWindow)
        self.pasteAction.triggered.connect(self.paste)
        self.toolbar.addAction(self.pasteAction)

        self.cutAction = QAction(QIcon("icons/paste.png"), "paste text", MainWindow)
        self.cutAction.triggered.connect(self.cut)
        self.toolbar.addAction(self.cutAction)

        self.undoAction = QAction(QIcon("icons/undo.png"), "undo", MainWindow)
        self.undoAction.triggered.connect(self.undo)
        self.toolbar.addAction(self.undoAction)

        self.redoAction = QAction(QIcon("icons/redo.png"), "redo", MainWindow)
        self.redoAction.triggered.connect(self.redo)
        self.toolbar.addAction(self.redoAction)

        self.leftAlign = QAction(QIcon("icons/align-left.png"), "align left", MainWindow)
        self.leftAlign.triggered.connect(self.textAlignLeft)
        self.toolbar.addAction(self.leftAlign)

        self.rightAlign = QAction(QIcon("icons/align-right.png"), "align right", MainWindow)
        self.rightAlign.triggered.connect(self.textAlignRight)
        self.toolbar.addAction(self.rightAlign)

        self.centerAlign = QAction(QIcon("icons/align-center.png"), "align center", MainWindow)
        self.centerAlign.triggered.connect(self.textAlignCenter)
        self.toolbar.addAction(self.centerAlign)

        self.justifyAlign = QAction(QIcon("icons/align-justify.png"), "align justify", MainWindow)
        self.justifyAlign.triggered.connect(self.textAlignJustify)
        self.toolbar.addAction(self.justifyAlign)

        self.dateAction = QAction(QIcon("icons/calender.png"), "insert date", MainWindow)
        self.dateAction.triggered.connect(self.date)
        self.toolbar.addAction(self.dateAction)

        self.timeAction = QAction(QIcon("icons/time.png"), "insert time", MainWindow)
        self.timeAction.triggered.connect(self.time)
        self.toolbar.addAction(self.timeAction)

        self.tableAction = QAction(QIcon("icons/table.png"), "insert table", MainWindow)
        self.tableAction.triggered.connect(self.tableDialog)
        self.toolbar.addAction(self.tableAction)

        self.bulletAction = QAction(QIcon("icons/bullet.png"), "insert bulleted list", MainWindow)
        self.bulletAction.triggered.connect(self.listBullets)
        self.toolbar.addAction(self.bulletAction)

        self.numberAction = QAction(QIcon("icons/number.png"), "insert numbered list", MainWindow)
        self.numberAction.triggered.connect(self.listNumbered)
        self.toolbar.addAction(self.numberAction)

        self.imageAction = QAction(QIcon("icons/image.png"), "insert image", MainWindow)
        self.imageAction.triggered.connect(self.insertimage)
        self.toolbar.addAction(self.imageAction)

        self.fontcolorAction = QAction(QIcon("icons/font-color.png"), "Select font color", MainWindow)
        self.fontcolorAction.triggered.connect(self.fontColorSelect)
        self.toolbar.addAction(self.fontcolorAction)

        self.fontBackgroundAction = QAction(QIcon("icons/highlight.png"), "Select font background color", MainWindow)
        self.fontBackgroundAction.triggered.connect(self.fontBackground)
        self.toolbar.addAction(self.fontBackgroundAction)

        self.fontAction = QAction(QIcon("icons/font.png"), "Choose Font", MainWindow)
        self.fontAction.triggered.connect(self.selectFont)
        self.toolbar.addAction(self.fontAction)


        
        self.central_widget = QWidget(MainWindow)
        

        self.splitter = QSplitter(self.central_widget)
        self.splitter.setOrientation(Qt.Horizontal)
        # self.splitter.addWidget(self.listc)        
        # self.splitter.addWidget(self.listFrame)        
        # self.splitter.addWidget(self.stack)               
        #self.splitter.addWidget(self.stackFrame)

        #self.splitter.setMinimumWidth(10)
        self.splitter.setStretchFactor(0,25)
        self.splitter.setStretchFactor(1,75)




        self.listc = QListWidget(self.splitter)
        self.listc.setObjectName("List")
        self.listc.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listc.customContextMenuRequested.connect(self.listMenu)
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

        self.splitter.addWidget(self.listc)
        self.splitter.addWidget(self.stack)

        self.splitter.setSizes([50, 650])
        # self.splitter.setStretchFactor(0,25)
        # self.splitter.setStretchFactor(1,9)

####################################################################################################################




        self.boxlayout = QHBoxLayout()        
        self.central_widget.setLayout(self.boxlayout)
        MainWindow.setCentralWidget(self.central_widget)

        self.boxlayout.addWidget(self.splitter)

        
        #application.aboutToQuit.connect(self.closeEvent)




        #self.load()



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


#################################################################################################################################

    # def newFile(self):

    #     self.newFileDialog = QDialog()

    #     self.layout_newFile = QFormLayout()

    #     self.label_newFileDialog = QLabel("File Save Location:")

    #     self.le_newFileFilepath = QLineEdit().setReadOnly(True)

    #     self.btn_newFileDestination = QPushButton('Save Location')
    #     self.btn_newFileDestination.clicked.connect(self.noteSave)

    #     self.label_filePass = QLabel("Password :")

    #     self.filePass = QLineEdit()
    #     self.filePass.setEchoMode(QLineEdit.Password)

    #     self.btn_newFileSave = QPushButton("Create File")
    #     #self.btn_newFileSave.clicked.connect(self.createFile)

    #     self.newFileDialog.setLayout(self.layout_newFile)
    #     self.layout_newFile.addRow(self.label_newFileDialog, self.le_newFileFilepath)
    #     #self.layout_newFile.addRow(self.le_newFileFilepath)
    #     self.layout_newFile.addRow(self.btn_newFileDestination)
    #     self.layout_newFile.addRow(self.label_filePass, self.filePass)
    #     self.layout_newFile.addRow(self.btn_newFileSave)

    #     self.newFileDialog.show()






    # def noteSave(self):

    #     noteLocation = QFileDialog.getSaveFileName(self, 'Save File')[0]

    #     self.le_newFileFilepath.setText(str(noteLocation))




    # def createFile(self):

    #     pass
    

#################################################################################################################################

    # def closeEvent(self):
    #     #Your desired functionality here
    #     print('Close button pressed')
    #     import sys
    #     sys.exit(0)





        
        

        


    # def closeEvent(self, event):
    #     print("JFC")
    #     # this actually needs to be in a on close method
    #     mssg = QMessageBox.question(MainWindow, 'Close Window', 'Are you sure you want to exit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)


    #     if mssg == QMessageBox.Yes:
    #         event.accept()            
    #         print('CLOSE EVENT TRIGGERED')
    #         shutil.rmtree(self.saveFile)        

    #     else:
    #         event.ignore()






    # for g in range(self.stack.count()):
    # self.q = self.stack.widget(g)
    # tabwidgetName = ET.SubElement(root, 'tabwid_name')
    # tabwidgetName.text = self.q.objectName()
    # for p in range(self.q.count()):
    #     self.tabtext = self.q.tabText(p)
    #     #self.tabicon = self.q.tabIcon(p)
    #     self.ticon = self.tabwidget_icons_dict[self.tabtext]
    #     self.tabcontents = self.q.widget(p).objectName()+


    # self.item = self.listc.currentItem()
    # self.curr_tab_wid = self.stack.findChild(QTabWidget, self.item.text())
    # self.curr_tab = self.curr_tab_wid.currentIndex()
    # self.curr_tab_wid.setTabText(self.curr_tab, tabRename)






    def currentEdit(self):

        self.stack_currWid = self.stack.currentWidget()
        self.tab_currWid = self.stack_currWid.currentWidget()
        self.tab_currWid = self.tab_currWid
        #self.activeEdit = self.tab_currWid.findChild(QTabWidget, self.tab_currWid.text())
        self.activeEdit = self.tab_currWid
        #print(self.activeEdit)
        return self.activeEdit

        # for t in range(self.stack.count()):
        #     self.activeTE = self.stack.widget(t)

        






    def tableDialog(self):

        self.table_dialog = QDialog(MainWindow)

        self.tablediag_layout = QFormLayout()

        self.lbl_rows = QLabel('Rows :')
        self.lbl_cols = QLabel('Cols :')
        self.lbl_spacing = QLabel('Spacing :')
        self.lbl_padding = QLabel('Padding :')


        self.sb_rows = QSpinBox()
        self.sb_cols = QSpinBox()
        self.sb_spacing = QSpinBox()
        self.sb_padding = QSpinBox()

        self.btn_insert = QPushButton('Insert Table')
        self.btn_insert.clicked.connect(self.table)

        self.table_dialog.setLayout(self.tablediag_layout)
        self.tablediag_layout.addRow(self.lbl_rows, self.sb_rows)
        self.tablediag_layout.addRow(self.lbl_cols, self.sb_cols)
        self.tablediag_layout.addRow(self.lbl_spacing, self.sb_spacing)
        self.tablediag_layout.addRow(self.lbl_padding, self.sb_padding)
        self.tablediag_layout.addRow(self.btn_insert)

        self.table_dialog.show()




    def table(self):
        
        self.tableRows = self.sb_rows.text()
        self.tableCols = self.sb_cols.text()
        self.tableSpacing = self.sb_spacing.text()
        self.tablePadding = self.sb_padding.text()

        tableFormatting = QTextTableFormat()
        tableFormatting.setCellPadding(int(self.tablePadding))
        tableFormatting.setCellSpacing(int(self.tableSpacing))

        cursor = self.currentEdit().textCursor()

        table = cursor.insertTable(int(self.tableRows), int(self.tableCols), tableFormatting)
        # table.QTextTableFormat.setCellPadding(int(self.tablePadding))
        # table.QTextTableFormat.setCellSpacing(int(self.tableSpacing))




    def copy(self):
        cursor = self.currentEdit().textCursor()
        txtSelected = cursor.selectedText()
        self.copyTxt = txtSelected


    def paste(self):
        self.currentEdit().append(self.copyTxt)


    def cut(self):
        self.currentEdit().cut()



    def fontColorSelect(self):
        color = QColorDialog.getColor()

        self.currentEdit().setTextColor(color)


    def undo(self):
        self.currentEdit().undo()

    def redo(self):
        self.currentEdit().redo()

    def textAlignLeft(self):
        print('left')
        self.currentEdit().setAlignment(Qt.AlignLeft)

    def textAlignRight(self):
        self.currentEdit().setAlignment(Qt.AlignRight)

    def textAlignCenter(self):
        print('center')
        self.currentEdit().setAlignment(Qt.AlignCenter)

    def textAlignJustify(self):
        self.currentEdit().setAlignment(Qt.AlignJustify)

    def date(self):
        currentDate = QDate.currentDate()
        cursor = self.currentEdit().textCursor()
        # setText method erases all the content in the textedit and replaces it with just the date
        # insert at cursor
        cursor.insertText(currentDate.toString(Qt.DefaultLocaleLongDate))
        #self.currentEdit().setText(currentDate.toString(Qt.DefaultLocaleLongDate))


    def time(self):
        currentTime = QTime.currentTime()
        cursor = self.currentEdit().textCursor()

        cursor.insertText(currentTime.toString(Qt.DefaultLocaleLongDate))


    def listBullets(self):

        cursor = self.currentEdit().textCursor()

        cursor.insertList(QTextListFormat.ListDisc)



    def listNumbered(self):

        cursor = self.currentEdit().textCursor()

        cursor.insertList(QTextListFormat.ListDecimal)



    def insertimage(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Insert image',".","Images (*.png *.xpm *.jpg *.bmp *.gif)")

        filename = str(filename[0])
        fext = os.path.splitext(filename)[1]
        print('extension :', fext)
        fbase = os.path.basename(filename)
        print('filename :',os.path.basename(filename))

        

        if not os.path.exists(r'{}'.format(self.recentLoad) + r'/res'):
            print(r'{}'.format(self.recentLoad) + r'/res')
            os.makedirs(r'{}'.format(self.recentLoad) + r'/res')
        
        shutil.copyfile(r'{}'.format(filename), r'{}'.format(self.recentLoad) + r'/res/{}'.format(fbase))
        # need to feed the copyfile copy in res directory to the qimage()
        img = QImage(filename)

        if img.isNull():
            imgErrorMessage = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                            "Image load error",
                            "Could not load image file!, Please make sure the file is an image format",
                            QtWidgets.QMessageBox.Ok,
                            self)
            popup.show()
        else:
            cursor = self.currentEdit().textCursor()
            cursor.insertImage(img, filename)





    def selectFont(self):

        font, ok = QFontDialog.getFont()

        if ok:
            self.currentEdit().setCurrentFont(font)


    def fontBackground(self):

        backgroundColor = QColorDialog.getColor()

        self.currentEdit().setTextBackgroundColor(backgroundColor)



    def newWindow(self):

        #MainWindow.show()
        #return

        #self.setupUi(MainWindow)
        self.createFile()
        











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

        fname = QFileDialog.getOpenFileName(MainWindow, 'Open File', 'images\icons')
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
            self.ico = QIcon()
            self.defaultListIcon = 'icons/notebook.png'
            self.ico.addPixmap(QPixmap(self.defaultListIcon))
            
            item = QListWidgetItem()
            item.setIcon(self.ico)
            item_text = self.le_item.text()
            item.setText(item_text)
            self.listc.addItem(item)
            self.tab_widget = QTabWidget()
            self.tab_widget.setMovable(True)
            self.tab_widget.setObjectName(item_text)
            self.stack.addWidget(self.tab_widget)

            self.list_icons_dict[item_text] = self.defaultListIcon


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

            self.list_icons_dict[str(item_text)] = str(self.item_filename)
            print("List Icon Dict :", self.list_icons_dict)
            #self.tabwidget_icons_dict[self.tab_widget.objectName()] = #nested dict here (tabnames:filepath)

            #print('list icons:','\n' ,self.list_icons_dict.items())
            #print(self.tabwidget_icons_dict.items())

        else:
            self.item_msg_box = QMessageBox(self, 'Message', 'Please Enter a title for ListItem', QMessageBox.Ok)
            self.item_dialog.close()

        self.item_dialog.close()


    # def checktoggle(self):
    #     self.btn_icon.setEnabled(True)

    def chooseTabIcon(self):
        fname = QFileDialog.getOpenFileName(MainWindow, 'Open File', 'images\icons')
        fname = str(fname[0])
        self.tabicon_filename = fname
        self.le_tab_path.setText(fname)



    def tab_ok(self):

        self.check_tab_icon = self.combo_tab.isChecked()

        if self.check_tab_icon == False and self.le_text.text() != False:

            self.ico = QIcon()
            self.ico.addPixmap(QPixmap('icons/folder.png'), QIcon.Normal, QIcon.On)

            self.newTabName = self.le_text.text()            
            self.item = self.listc.currentItem()
            self.curr_tab_wid = self.stack.findChild(QTabWidget, self.item.text())
            self.newtabname_textedit = QTextEdit()
            self.newtabname_textedit.setObjectName(str(self.newTabName))
            self.curr_tab_wid.addTab(self.newtabname_textedit, self.ico ,self.newTabName)
            #self.curr_tab_wid.addTab(QTextEdit(), self.ico, self.newTabName)

            self.tabwidget_icons_dict['tabwidget'] = {self.curr_tab_wid.objectName()}
            self.tabwidget_icons_dict.update({self.newTabName:'icons/folder.png'})

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




    def programcfg(self):
        if os.path.exists('settings/programSettings.xml'):
            xmlSettings_currpath = ET.parse('settings/programSettings.xml').getroot()
            for p in xmlSettings_currpath.findall('recentfilepath'):
                self.currfile = p.text

        return self.currfile






    def tabMenu(self, event):
        self.tabContextMenu = QMenu()

        addTab = self.tabContextMenu.addAction('Add New Tab')
        deleteTab = self.tabContextMenu.addAction('Delete Tab')
        renameTab = self.tabContextMenu.addAction('Rename Tab')

        action = self.tabContextMenu.exec_(self.stack.mapToGlobal(event))

        if action == addTab:
            self.tabContents()
        if action == deleteTab:
            self.item = self.listc.currentItem()
            self.curr_tab_wid = self.stack.findChild(QTabWidget, self.item.text())
            self.curr_tab = self.curr_tab_wid.currentIndex()
            self.curr_tab_wid.removeTab(self.curr_tab)

            self.tabchanges.append(self.programcfg() + '/' + self.curr_tab.text)
            print(self.programcfg() + '/' + self.curr_tab.text)

        if action ==renameTab:
            tabRename, ok = QInputDialog.getText(self.tab_widget, 'Input Dialog', 'Enter new tab name')
            if ok:
                self.item = self.listc.currentItem()
                self.curr_tab_wid = self.stack.findChild(QTabWidget, self.item.text())
                self.curr_tab = self.curr_tab_wid.currentIndex()
                self.curr_tab_wid.setTabText(self.curr_tab, tabRename)








    def listMenu(self, event):
        self.contextMenu = QMenu()

        addListItem = self.contextMenu.addAction('Add List Item')
        deleteListItem = self.contextMenu.addAction('Delete List Item')
        renameListItem = self.contextMenu.addAction('Rename List Item')
        save = self.contextMenu.addAction('Save')


        action = self.contextMenu.exec_(self.listc.mapToGlobal(event))

        if action == addListItem:
            self.itemMenu()
        elif action == deleteListItem:
            
            self.fpath = self.listc.currentItem().text()
            #print(self.programcfg() + self.fpath)
            self.item = self.listc.currentItem()
            self.y = self.listc.takeItem(self.listc.row(self.item))#pops the list item out
            #self.r = self.stacked_widget.removeWidget(self.tab_widget.currentWidget())
            self.r = self.stack.findChild(QTabWidget, self.item.text())
            sip.delete(self.r)

            #add file to list [] to be deleted on the next Save?
            self.listchanges.append(self.programcfg() + '/' + self.fpath)


        elif action == renameListItem:
            newItemName, ok = QInputDialog.getText(self.listc, 'Input Dialog','List Item Name:')
            if ok:
                self.item = self.listc.currentItem()
                self.curr_item = self.stack.findChild(QTabWidget, self.item.text())
                self.curr_item.setObjectName(newItemName)
                self.item.setText(newItemName)
                # update the key with the new list item name in the list_icons_dict
        elif action == save:
            print(self.list_icons_dict)
            self.save()
            # self.print()





    def passwordmenu(self):

        self.passdialog = QDialog(MainWindow)

        self.passlayout = QFormLayout()

        self.passlbl = QLabel("Password :")

        self.passle = QLineEdit()

        self.passbtnbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        self.passbtnbox.accepted.connect(self.passaccept)
        self.passbtnbox.rejected.connect(self.passdialogclose)

        self.passdialog.setLayout(self.passlayout)
        self.passlayout.addRow(self.passlbl)
        self.passlayout.addRow(self.passle)
        self.passlayout.addRow(self.passbtnbox)

        self.passdialog.show()


    def passdialogclose(self):
        self.passdialog.close()


    def passaccept(self):

        self.notepassword = self.passle.text
        self.pw = self.passle.text
        self.passdialog.close()
        #
        # self.saveFile = QFileDialog.getSaveFileName(MainWindow, 'Save File')[0] 

        #return self.notepassword







    def print(self):

        lo = MainWindow.pos()
        lem = lo.x()
        lul = lo.y()
        lol = self.listc.width()
        lool = self.listc.height()

        print(lo, type(str(lem)), lul, lol, lool)

        print(self.activeTE)


        # #self.tabwidget_icons_dict['tabwidget'] = self.curr_tab_wid.objectName() #nested dict here (tabnames:filepath)
        # for i in self.stacked_widget.findChildren(QTabWidget):

        #     #self.tabwidget_icons_dict['tabwidget'] = i.objectName()
        #     #self.tabwidget_icons_dict['tabwidget'] = {}
        #     for j in range(i.count()):
        #         self.tabname = i.tabText(j)
        #         self.tabwidget_icons_dict[i.objectName()] = {}
        #         #self.tabwidget_icons_dict['tabwidget'][i.objectName()] = self.dict
        #         #self.tabwidget_icons_dict[i.objectName()] = self.dict
        #         #self.tabwidget_icons_dict[i.objectName()][self.tabname] = self.tab_ico
        #         #self.tabwidget_icons_dict[i.objectName()] = {self.tabname:self.tab_ico}
        #         #self.tabwidget_icons_dict[i.objectName()] = self.widget[self.tabname] = self.tab_ico
        #         #self.tabwidget_icons_dict[self.tabname] = self.tab_ico
        #         #self.tabwidget_icons_dict[self.newTabName] = self.tab_ico
        # print(self.tabwidget_icons_dict.items())


    def uichanges(self):

        # if the list is empty
        if not self.listchanges:
            pass
        else:
            for h in self.listchanges:
                print(h)
                shutil.rmtree(h)

        if not self.tabchanges:
            pass
        else:
            for g in self.tabchanges:
                print(g)
                os.remove(g)




    def programconfig(self, path):

        self.mww = MainWindow.width()
        self.mwh = MainWindow.height()
        self.mwx = MainWindow.x()
        self.mwy = MainWindow.y()  
        
        if not os.path.exists('settings'):
            os.makedirs('settings')

        settings_root = ET.Element('programSettings')
        settings_tree = ElementTree(settings_root)

        recentFilePath = ET.SubElement(settings_root, 'recentfilepath')
        recentFilePath.text = path

        mainw = ET.SubElement(settings_root, 'mainwindowsize')
        mainw.text = 'mainwindowsize'        
        mainw.set('x', str(self.mwx))
        mainw.set('y', str(self.mwy))
        mainw.set('width', str(self.mww))
        mainw.set('height', str(self.mwh))
        #mainw.set('position', str(self.mw))


        listsize = ET.SubElement(settings_root, 'listsize')
        listsize.text = 'listcoords'        
        listsize.set('width', str(self.listc.width()))
        listsize.set('height', str(self.listc.height()))


        stacksize = ET.SubElement(settings_root, 'stacksize')
        stacksize.text = 'stackcoords'        
        stacksize.set('width', str(self.stack.width()))
        stacksize.set('height', str(self.stack.height()))




        settings_tree.write(open('settings/programSettings.xml', 'wb'))





    def createFile(self):

        self.creatediaglog = QDialog()

        self.createfylelayy = QFormLayout()

        self.createbtn = QPushButton('Choose File')
        self.createbtn.clicked.connect(self.createclicked)


        self.createle = QLineEdit()

        self.cb_pass = QCheckBox()
        self.cb_pass.stateChanged.connect(self.cbpasstoggle)

        self.createPasslbl = QLabel('Enter Password')

        self.le_pass = QLineEdit()
        self.le_pass.setReadOnly(True)

        createfile_btnbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        createfile_btnbox.accepted.connect(self.createok)
        createfile_btnbox.rejected.connect(self.createcancel)

        self.creatediaglog.setLayout(self.createfylelayy)
        self.createfylelayy.addRow(self.createbtn)
        self.createfylelayy.addRow(self.createle)
        self.createfylelayy.addRow(self.createPasslbl)
        self.createfylelayy.addRow(self.cb_pass, self.le_pass)
        self.createfylelayy.addRow(createfile_btnbox)

        self.creatediaglog.exec()


    def cbpasstoggle(self):

        self.le_pass.setReadOnly(False)


    def createclicked(self):

        f = QFileDialog.getSaveFileName(MainWindow, 'Save File')[0]
        
        self.createle.setText(f)


    def createok(self):

        self.saveFile = self.createle.text()
        self.pw = self.le_pass.text()

        if self.pw != "":

            if not os.path.exists(self.saveFile):
                
                self.savefile_fn = os.path.split(self.saveFile)
                self.savefile_fnh = self.savefile_fn[0]
                self.savefile_fnt = self.savefile_fn[1]
                #self.savefile_fn = '_{}'.format(self.savefile_fn[1])
                os.makedirs(self.savefile_fnh + '/_{}'.format(self.savefile_fnt))
                self.saveFile = self.savefile_fnh + '/_{}'.format(self.savefile_fnt)

                print(self.saveFile)

        else:
            if not os.path.exists(self.saveFile):
                os.makedirs(self.saveFile)
                

        root = ET.Element('programElements')
        tree = ElementTree(root)

        tree.write(open(self.saveFile + '/config.xml', 'wb'))

        xml = ET.parse('settings/programSettings.xml')

        y = xml.find('recentfilepath')
        y.text = str(self.saveFile)

        xml.write(open('settings/programSettings.xml', 'wb'))

        #self.save()

        self.loadfile = self.saveFile



        self.creatediaglog.close()

        




    def createcancel(self):

        self.creatediaglog.close()



#### function for 7z extraction ####

    def extractfile(self, pw, fp):

        if '_' in '{}'.format(fp):
            # need a window here for user to enter password and feed string into the 7z subprocess below
            print('Encrypted 7z')
            self.loadpass()
            print(self.user_pass)
            subprocess.run([r'7z\7-Zip\7z.exe', 'x', '-p{}'.format(pw), '{}.7z'.format(fp), '-o{}'.format(fp)], shell=False)
        else:
            print('file is regular 7z')
            subprocess.run([r'7z\7-Zip\7z.exe', 'x', '{}'.format(fp)], shell=False)




#### function for 7z add ####

    def storefile(self, pw, fp):

        if '_' in fp:

            print(pw)
            print(fp)

            subprocess.run([r'7z\7-Zip\7z.exe', 'a', '-p{}'.format(pw) , '{}'.format(fp), '-o{}'.format(fp)], shell=False)

        else:
            subprocess.run([r'7z\7-Zip\7z.exe', 'a', '{}'.format(fp), '{}'.format(fp)], shell=False)








# can have function that just checks for file and gets a save location if no recent file found.
# or... can just wrap the content of the below save function in one big try/except block


    def save(self):



        self.uichanges()

                
        xmlSettings_save = ET.parse('settings/programSettings.xml')
        #xmlSettings_save.getroot()
        for p in xmlSettings_save.findall('recentfilepath'):
            rfp = p.text
            print(rfp)
        if 'none' in rfp:
            self.createFile()
            
            
            #self.saveFile = QFileDialog.getSaveFileName(MainWindow, 'Save File')[0]
            #self.passwordmenu()
            
        else:
            self.saveFile = p.text                


                    




            # try:
            #     #f = open('settings/programSettings.xml', 'r')
            #     xmlSettings_save = ET.parse('settings/programSettings.xml')
            #     xmlSettings_save.getroot()
            #     for p in xmlSettings_save.findall('recentfilepath'):
            #         rfp = p.text
            #         print(rfp)
            #     if 'none' in rfp:
            #         self.createFile()
            #         continue
            #         #self.saveFile = QFileDialog.getSaveFileName(MainWindow, 'Save File')[0]
            #         #self.passwordmenu()
            #     else:
            #         self.saveFile = p.text
            # except FileNotFoundError:
            #     print("file not found")


                # except FileNotFoundError:
                #     print("file not found")
                #     self.passwordmenu()

                # finally:
                #     self.passwordmenu()            
                    #saveFile = QFileDialog.getSaveFileName(MainWindow, 'Save File')[0]            
                    #f.close()






                # if os.path.exists('settings/programSettings.xml'):
                #     xmlSettings_save = ET.parse('settings/programSettings.xml')
                #     xmlSettings_save.getroot()
                #     for p in xmlSettings_save.findall('recentfilepath'):
                #         saveFile = p.text
                        
                # else:
                #     ### need to add an additional dialog to see if the user wants to add a password ####
                #     self.passwordmenu()
                #     saveFile = QFileDialog.getSaveFileName(MainWindow, 'Save File')[0]
                    
                    



            root = ET.Element('programElements')
            tree = ElementTree(root)

            

            for i in range(self.listc.count()):
                self.x = self.listc.item(i).text()
                #self.y = self.lb.item(i).icon()
                listitem = ET.SubElement(root, 'listitem')
                print(self.list_icons_dict)
                licon = self.list_icons_dict[self.x]
                listitem.set('item_icon', licon)
                listitem.text = self.x
            for g in range(self.stack.count()):
                self.q = self.stack.widget(g)
                tabwidgetName = ET.SubElement(root, 'tabwid_name')
                tabwidgetName.text = self.q.objectName()
                for p in range(self.q.count()):
                    self.tabtext = self.q.tabText(p)
                    #self.tabicon = self.q.tabIcon(p)
                    self.ticon = self.tabwidget_icons_dict[self.tabtext]
                    self.tabcontents = self.q.widget(p).objectName()

                    # self.savefile_fn = os.path.split(self.saveFile)
                    # self.savefile_fn = '_{}'.format(self.savefile_fn[1])
                    # self.saveFile = self.saveFile + '\{}'.format(self.savefile_fn)

                    # if not os.path.exists(self.saveFile + '\{}'.format(tabwidgetName.text)):
                    #     os.makedirs(self.saveFile + '\{}'.format(self.savefile_fn) + '\{}'.format(tabwidgetName.text))


                    # if not os.path.exists(r'C:\Users\User\source\repos\TestNoteApplication\TestNoteApplication\NoteFinal\Notes\{}'.format(tabwidgetName.text)):
                    #     os.makedirs(r'C:\Users\User\source\repos\TestNoteApplication\TestNoteApplication\NoteFinal\Notes\{}'.format(tabwidgetName.text))

                    

                    if not os.path.exists(self.saveFile + '/{}'.format(tabwidgetName.text) + '/{}/'.format(self.tabcontents)):
                        os.makedirs(self.saveFile + '/{}'.format(tabwidgetName.text) + '/{}/'.format(self.tabcontents))
                        print(self.saveFile + '/{}'.format(tabwidgetName.text) + '/{}/'.format(self.tabcontents))

                    with open(r'{}'.format(self.saveFile) + r'/{}'.format(tabwidgetName.text) + r'/{}/{}.html'.format(self.tabcontents, self.tabcontents), 'w') as file:
                        file.write(self.q.widget(p).toHtml())
                    file.close()


                    # with open (r'C:\Users\User\source\repos\TestNoteApplication\TestNoteApplication\NoteFinal\Notes\{}\{}.html'.format(tabwidgetName.text, self.tabcontents) , 'w') as file:
                    #     file.write(self.q.widget(p).toHtml())
                    # file.close()

                    #self.tabcontents = type(self.q.widget(p))
                    tabName = ET.SubElement(tabwidgetName, 'tabName')
                    tabName.set('content', str(self.tabcontents))
                    tabName.set('tabIcon', self.ticon)
                    tabName.text = self.tabtext
                    #self.tabwidget_icons_dict[tabwidgetName.text] = self.tabtext, self.tabwidget_icons_dict[#nested dict here (tabnames:filepath)
                    #self.tabwidget_icons_dict[self.tabtext] =

            # if not os.path.exists(self.saveFile):
            #     os.makedirs(self.saveFile)

            tree.write(open(self.saveFile + '/config.xml', 'wb'))

            #self.pw = self.passwordmenu()

            # self.savefile_fn = os.path.split(self.saveFile)
            # self.savefile_fn = '_{}'.format(self.savefile_fn[1])
            # print('filename :', self.savefile_fn)
            print('savefilepath :', self.saveFile)


            if '_' in self.saveFile:

                

                print(self.pw)
                print(self.savefile_fnt)
                # used to add all files in the working directory with the -o flag and when i deleted it, it worked the way it should
                subprocess.run([r'7z\7-Zip\7z.exe', 'a', '-p{}'.format(self.pw) , '{}'.format(self.saveFile), '{}'.format(self.saveFile)], shell=False) 

            else:
                subprocess.run([r'7z\7-Zip\7z.exe', 'a', '{}'.format(self.saveFile), '{}'.format(self.saveFile)], shell=False)





            # if self.pw != "":

            #     print(self.pw)

            #     subprocess.run([r'7z\7-Zip\7z.exe', 'a', '-p{}'.format(self.pw) , '{}'.format(self.saveFile), '-o{}'.format(self.savefile_fn)], shell=False)

            # else:
            #     subprocess.run([r'7z\7-Zip\7z.exe', 'a', '{}'.format(self.saveFile), '{}'.format(self.saveFile)], shell=False)


            self.programconfig(self.saveFile)
            




            #self.passwordmenu()

            #self.createFile()



        #list_xml = dicttoxml(self.list_icons_dict, custom_root='listicons')
        #tab_xml = dicttoxml(self.tabwidget_icons_dict, custom_root='tabicons')
        #xml = xml.decode()






        # if not os.path.exists('settings'):
        #     os.makedirs('settings')

        # settings_root = ET.Element('programSettings')
        # settings_tree = ElementTree(settings_root)

        # recentFilePath = ET.SubElement(settings_root, 'recentFilePath')
        # recentFilePath.text = self.saveFile

        # mainw = ET.SubElement(settings_root, 'mainwindowSize')
        # mainw.set('x', MainWindow.x())
        # mainw.set('y', MainWindow.y())
        # mainw.text = MainWindow.pos()

        # listsize = ET.SubElement(settings_root, 'listSize')
        # listsize.set('width', self.listc.width())
        # listsize.set('height', self.listc.height())
        # listsize.text = 'listcoords'

        # stacksize = ET.SubElement(settings_root, 'stackSize')
        # stacksize.set('width', self.stack.width())
        # stacksize.set('height', self.stack.height())
        # stacksize.text = 'stackcoords'


        # #settings_root.set('recentFilePath', self.saveFile)



        # settings_tree.write(open('settings/programSettings.xml', 'wb'))









        # self.noteSettings.beginGroup("programSettings")
        # self.noteSettings.setValue('recentFilePath', self.saveFile.text())
        # self.noteSettings.endGroup()
        # self.noteSettings.sycn()
        
















    def loadpass(self):

        self.enterpass = QDialog()

        self.loadpass_layout = QFormLayout()

        self.lp_lbl = QLabel('Enter Password :')

        self.lp_le = QLineEdit()

        lp_btnbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        lp_btnbox.accepted.connect(self.lp_ok)
        lp_btnbox.rejected.connect(self.lp_cancel)

        self.enterpass.setLayout(self.loadpass_layout)
        self.loadpass_layout.addRow(self.lp_lbl)
        self.loadpass_layout.addRow(self.lp_le)
        self.loadpass_layout.addRow(lp_btnbox)

        self.enterpass.exec()




    def lp_ok(self):

        self.user_pass = self.lp_le.text()

        self.enterpass.close()


    def lp_cancel(self):

        self.enterpass.close()

    

    def loadChoiceDialog(self):

        self.choice_dialog = QDialog()

        self.choice_layout = QFormLayout()

        self.lbl_choice = QLabel('Cannot find any recently opened files. Would you like to open an existing Note file or create a new Note file?')

        self.btn_choiceOpen = QPushButton('Open Note File')
        self.btn_choiceOpen.clicked.connect(self.openNote)

        self.btn_choiceNew = QPushButton('Create a new Note File')
        self.btn_choiceNew.clicked.connect(self.createNote)

        self.choice_dialog.setLayout(self.choice_layout)
        self.choice_layout.addRow(self.lbl_choice)
        self.choice_layout.addRow(self.btn_choiceOpen, self.btn_choiceNew)

        self.choice_dialog.exec() # .show() wont show only exec() seems to work


    def openNote(self):
        self.noteFileOpen = QFileDialog.getOpenFileName(MainWindow, 'Open File')
        print('notefileopen :', self.noteFileOpen)
        self.loadfile = str(self.noteFileOpen[0])
        #self.loadfile = os.path.splitext(str(self.noteFileOpen))
        print('loadfile :', self.loadfile)
        self.choice_dialog.close()

    def createNote(self):
        self.createFile()

        self.choice_dialog.close()






    def load(self):




        # try:
        #     filename = ET.parse('config.xml').getroot()
        #     #ico_fname = ET.parse('icons.xml').getroot()
        # except:
        #     msg_box = QMessageBox.question(MainWindow, 'Message', 'No existing file. Would you like to make a new Notes File?', QMessageBox.Ok)
        #     if msg_box == QMessageBox.Ok:
        #         sys.exit()


        #loadfile was self.recentLoad

        if os.path.exists('settings/programSettings.xml'):
            self.xmlSettingsLoad = ET.parse('settings/programSettings.xml')
            #self.xmlSettingsLoad.getroot()

            for o in self.xmlSettingsLoad.findall('recentfilepath'):
                recent = o.text
                
                if 'none' in recent:
                    # new dialog -- Cannot find any recently opened files. Would you like to open an existing Note file or create a new Note file?
                    
                    self.loadChoiceDialog()
                    #self.newWindow()
                    #self.loadfile = self.noteFileOpen
                    #MainWindow.show()
                    #return
                    

                else:
                    self.loadfile = o.text
                    print('recentload :',self.loadfile)
                        #MainWindow.show()
            


            #self.xmlSettingsTree = ElementTree(self.xmlSettings)
            #self.recentLoad = self.xmlSettingsTree.findtext('recentFilePath').text()



        #could put a symbol or underscore in the filename of the 7z file to indicate it does have encryption

        #self.rl_head = os.path.split(str(self.loadfile[0]))
        self.rl_head = self.loadfile
        print('rl_head :', self.rl_head)
        if '_' in '{}'.format(self.loadfile):
            # need a window here for user to enter password and feed string into the 7z subprocess below
            print('Encrypted 7z')
            self.loadpass()
            print(self.user_pass)
            subprocess.run([r'7z\7-Zip\7z.exe', 'x', '-p{}'.format(self.user_pass), '{}.7z'.format(self.loadfile), '-o{}'.format(self.loadfile)], shell=False)
        else:
            print('file is regular 7z')
            subprocess.run([r'7z\7-Zip\7z.exe', 'x', '{}.7z'.format(self.loadfile)], shell=False)

        # print('splittext :', str(os.path.splitext(self.loadfile)[0]))
        # if not os.path.exists(r'{}'.format(os.path.splitext(self.loadfile)[0])):
        #     #os.makedirs(r'{}'.format(self.recentLoad))
        #     print('NO EXIST')
            
        # else:
        #     print('THIS PATH EXISTS')

        #replace 'config.xml' with the filepath from the programSettings.xml
        # filename = ET.parse(self.recentLoad + '/config.xml').getroot()
        
        #filename = ET.parse(r'{}{}'.format(os.path.basename(self.loadfile[0]), r'/config.xml')).getroot()
        print('splittext :', str(os.path.splitext(self.loadfile)[0]))
        filename = ET.parse(r'{}{}'.format(os.path.splitext(self.loadfile)[0], r'/config.xml')).getroot()
        for listitem in filename.findall('listitem'):
            #self.lb.addItem(listitem.text)
            item = QListWidgetItem()
            icon = listitem.get('item_icon')
            self.ico = QIcon(icon)
            item.setIcon(self.ico)
            item.setText(listitem.text)
            self.listc.addItem(item)

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
            self.stack.addWidget(self.tab_widget)
            for tabname in tabwidget.iter('tabName'):
                self.id = self.stack.findChild(QTabWidget, tabwidget.text)
                self.tab_icon = tabname.get('tabIcon')
                self.tabico = QIcon(self.tab_icon)
                self.tabwidget_icons_dict[tabname.text] = self.tab_icon
                content = tabname.get('content')
                print('THIS SHIT :' ,r'{}/{}/{}/{}.html'.format(os.path.splitext(self.loadfile)[0] , self.tab_widget.objectName(), content, content))
                if os.path.exists(r'{}\{}'.format(os.path.splitext(self.loadfile)[0] ,self.tab_widget.objectName())):
                    


                    tE = QTextEdit()
                    tE.setObjectName(content)
                    
                    with open(r'{}/{}/{}/{}.html'.format(os.path.splitext(self.loadfile)[0] , self.tab_widget.objectName(), content, content), 'r') as file:
                        tE.setText(file.read())
                    file.close()
                    self.id.addTab(tE, self.tabico, tabname.text)

                else:
                    msg_box = QMessageBox()
                    msg_box.setText("Error when loading file")
                    msg_box.setWindowTitle("File Error")
                    msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg_box.exec()



        if os.path.isfile('settings/programSettings.xml'):

            self.recentconfig = ET.parse('settings/programSettings.xml').getroot()

        for i in self.recentconfig.findall('mainwindowsize'):
            self.mws_x = i.get('x')
            self.mws_y = i.get('y')
            self.mw_width = i.get('width')
            self.mw_height = i.get('height')
            
            print(self.mws_x, self.mws_y)


        MainWindow.setGeometry(int(self.mws_x), int(self.mws_y), int(self.mw_width), int(self.mw_height))

        for ls in self.recentconfig.findall('listsize'):

            self.list_width = ls.get('width')
            

        for ss in self.recentconfig.findall('stacksize'):

            self.ssize = ss.get('width')


        self.splitter.setSizes([int(self.list_width), int(self.ssize)])







        #self.programconfig(self.recentLoad)



        #MainWindow.setFixedSize()


        # self.noteSettings.beginGroup("programSettings")
        # self.noteSettings.setValue('recentFilePath', str(self.recent))
        # self.noteSettings.endGroup()
        # self.noteSettings.sync()

                





                # if 'QTextEdit' in str(content):
                #     self.id.addTab(QTextEdit(), self.tabico, tabname.text)
                # elif 'QGraphicsView' in str(content):
                #     self.id.addTab(QGraphicsView(), self.tabico, tabname.text)
                # elif 'QWidget' in str(content):
                #     self.id.addTab(QWidget(), self.tabico ,tabname.text)





# def main():
#     application = QApplication(sys.argv)

#     # window
#     MainWindow = QMainWindow()
#     ui = Notes()
#     ui.setupUi(MainWindow)
#     #ui.setWindowTitle('Notes')
#     #ui.resize(1280, 720)
#     #ui.show()
#     MainWindow.show()
    
    
#     sys.exit(application.exec_())


# if __name__ == "__main__":
#     main()






if __name__ == "__main__":

    application = QApplication(sys.argv)

    # window
    MainWindow = QMainWindow()
    ui = Notes()
    #ui.setupUi(MainWindow)
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




