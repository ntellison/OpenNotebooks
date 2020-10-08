from notesUi import Notes
import os
import sys
import subprocess

from PyQt5 import Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage, QTextTable , QTextTableFormat, QTextListFormat, QFont
from PyQt5.QtCore import QEvent, Qt, QSize, QSettings, QDate, QTime
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFormLayout, QLineEdit, QTabWidget, QWidget, QPushButton, QListWidgetItem, QTextEdit,
                            QLabel, QVBoxLayout, QSpinBox, QPlainTextEdit, QStackedWidget, QComboBox, QListWidget, QMenu, QGroupBox, QDialogButtonBox,
                            QGraphicsScene, QCheckBox, QMessageBox, QColorDialog, QFileDialog, QDialog, QFontDialog, QInputDialog)

import sip
import shutil

from xml.etree.ElementTree import ElementTree
import xml.etree.ElementTree as ET
from dicttoxml import dicttoxml


global instance
instance = ''


class NotesEditing(Notes):

    def __init__(self):
        super().__init__()

        self.list_icons_dict = {}
        self.tabwidget_icons_dict = {}

        self.listchanges = []
        self.tabchanges = []

        self.status = True

        self.deftabico = 'icons/tabred.png'
        self.defaultListIcon = 'icons/notebookgrey.png'


        self.MainWindow = QMainWindow()
        self.setupUi(self.MainWindow)


        # Menubar

        self.menu_file_action.triggered.connect(self.createFile)
        self.new_notebook_action.triggered.connect(self.itemMenu)
        self.open_file_action.triggered.connect(self.openNote)
        self.save_file_action.triggered.connect(self.save)
        
        self.undo_edit_action.triggered.connect(self.undo)
        self.redo_edit_action.triggered.connect(self.redo)
        self.copy_edit_action.triggered.connect(self.copy)
        self.cut_edit_action.triggered.connect(self.cut)
        self.paste_edit_action.triggered.connect(self.paste)
        self.image_edit_action.triggered.connect(self.insertimage)
        self.table_edit_action.triggered.connect(self.tableDialog)
        self.time_edit_action.triggered.connect(self.time)
        self.date_edit_action.triggered.connect(self.date)

        self.fontcolor_format_action.triggered.connect(self.fontColorSelect)
        self.fontbgcolor_format_action.triggered.connect(self.fontBackground)
        self.font_format_action.triggered.connect(self.selectFont)
        self.leftalign_format_action.triggered.connect(self.textAlignLeft)
        self.centeralign_format_action.triggered.connect(self.textAlignCenter)
        self.rightalign_format_action.triggered.connect(self.textAlignRight)
        self.alignjustify_format_action.triggered.connect(self.textAlignJustify)



        


        # Toolbar

        self.addnew.triggered.connect(self.itemMenu)
        self.addtab.triggered.connect(self.tabContents)
        self.saveAction.triggered.connect(self.save)
        self.newFile.triggered.connect(self.createFile)
        self.printcfg.triggered.connect(self.exportPDF)
        self.openAction.triggered.connect(self.open)
        self.copyAction.triggered.connect(self.copy)
        self.pasteAction.triggered.connect(self.paste)
        self.cutAction.triggered.connect(self.cut)
        self.undoAction.triggered.connect(self.undo)
        self.redoAction.triggered.connect(self.redo)
        self.leftAlign.triggered.connect(self.textAlignLeft)
        self.rightAlign.triggered.connect(self.textAlignRight)
        self.centerAlign.triggered.connect(self.textAlignCenter)
        self.justifyAlign.triggered.connect(self.textAlignJustify)
        self.dateAction.triggered.connect(self.date)
        self.timeAction.triggered.connect(self.time)
        self.tableAction.triggered.connect(self.tableDialog)
        self.bulletAction.triggered.connect(self.listBullets)
        self.numberAction.triggered.connect(self.listNumbered)
        self.imageAction.triggered.connect(self.insertimage)
        self.fontcolorAction.triggered.connect(self.fontColorSelect)
        self.fontBackgroundAction.triggered.connect(self.fontBackground)
        self.fontAction.triggered.connect(self.selectFont)
        self.HRAction.triggered.connect(self.insertHR)






        self.list.customContextMenuRequested.connect(self.listMenu)
        self.list.itemClicked.connect(self.list_clicked)
        self.stack.customContextMenuRequested.connect(self.tabMenu)

        self.MainWindow.closeEvent = self.closeEvent

        self.loadcheck()



    def closeEvent(self, event):

        self.active = QApplication.activeWindow()

        if self.archive != None:


            if self.status:

                split = os.path.splitext(self.archive)[0]

                if os.path.exists(split):

                    shutil.rmtree(split)
                    event.accept()


                else:
                    event.accept()


                self.active.close()

            else:

                reply = QMessageBox.question(self.MainWindow, 'Message',
                                            "It looks like you have some unsaved changes to your notes. Are you sure to quit?", QMessageBox.Yes |
                                            QMessageBox.No | QMessageBox.Save)


                if reply == QMessageBox.Yes:
                    try:
                        
                        split = os.path.splitext(self.archive)[0]
                        if os.path.exists(split):

                            shutil.rmtree(split)
                            event.accept()
                            self.active.close()
                            
                        else:
                            event.accept()

                            self.active.close()

                    except:
                        self.active.close()


                elif reply == QMessageBox.Save:
                    self.save()

                    split = os.path.splitext(self.archive)[0]
                    
                    if os.path.exists(split):

                        shutil.rmtree(split)
                        
                    event.accept()
                    self.active.close()
                    #event.ignore()

                elif reply == QMessageBox.No:
                    event.ignore()




        else:
            self.active.close()




    def currentEdit(self):

        self.stack_currWid = self.stack.currentWidget()
        self.tab_currWid = self.stack_currWid.currentWidget()
        self.tab_currWid = self.tab_currWid
        self.activeEdit = self.tab_currWid
        return self.activeEdit






    def tableDialog(self):

        self.table_dialog = QDialog()

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

        self.currentEdit().setAlignment(Qt.AlignLeft)

    def textAlignRight(self):
        self.currentEdit().setAlignment(Qt.AlignRight)

    def textAlignCenter(self):

        self.currentEdit().setAlignment(Qt.AlignCenter)

    def textAlignJustify(self):
        self.currentEdit().setAlignment(Qt.AlignJustify)

    def date(self):
        currentDate = QDate.currentDate()
        cursor = self.currentEdit().textCursor()
        # insert at cursor
        cursor.insertText(currentDate.toString(Qt.DefaultLocaleLongDate))


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
        filename = QFileDialog.getOpenFileName(self.MainWindow, 'Insert image',".","Images (*.png *.xpm *.jpg *.bmp *.gif)")

        filename = str(filename[0])
        fext = os.path.splitext(filename)[1]

        fbase = os.path.basename(filename)

        if not os.path.exists(r'{}'.format(os.path.splitext(self.loadfile)[0]) + r'/res'):

            os.makedirs(r'{}'.format(os.path.splitext(self.loadfile)[0]) + r'/res')
        
        shutil.copyfile(r'{}'.format(filename), r'{}'.format(os.path.splitext(self.loadfile)[0]) + r'/res/{}'.format(fbase))

        img = QImage(filename)

        if img.isNull():
            imgErrorMessage = QMessageBox(self.MainWindow, QMessageBox.Critical,
                            "Image load error",
                            "Could not load image file., Please make sure the file is an image file. (.png, .jpg, .bmp, .gif)",
                            QMessageBox.Ok,
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




    def open(self):

        self.noteFileOpen = QFileDialog.getOpenFileName(self.MainWindow, 'Open File')[0]

        self.openfile = os.path.splitext(self.noteFileOpen)[0]



        xml = ET.parse('settings/programSettings.xml')

        y = xml.find('recentfilepath')
        y.text = str(self.openfile)

        xml.write(open('settings/programSettings.xml', 'wb'))

        self.win = NotesEditing()


    def insertHR(self):

        c = self.currentEdit().textCursor()

        c.insertHtml("<hr style='color: red'></hr><br>")


    def exportPDF(self):

        savepdf = QFileDialog.getSaveFileName(self.MainWindow, "Export Current Note to PDF", None, "PDF files (.pdf)")

        qprint = QPrinter(QPrinter.HighResolution)
        qprint.setOutputFormat(QPrinter.PdfFormat)
        qprint.setOutputFileName(savepdf[0])

        self.currentEdit().document().print_(qprint)




    def list_clicked(self):
        self.item = self.list.currentItem()
        self.index = self.list.currentIndex()

        self.findSection = self.stack.findChild(QTabWidget, self.item.text())
        self.stack.setCurrentWidget(self.findSection)



    def notebookstatus(self):
        self.status = False



    def tabContents(self):
        self.dialog = QDialog()

        self.layout_tab = QFormLayout()

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
        self.layout_tab.addRow(self.btn_icon)
        self.layout_tab.addRow(self.le_tab_path)
        self.layout_tab.addRow(buttonBox)

        self.dialog.show()

    def itemMenu(self):
        self.item_dialog = QDialog()

        self.layout_item = QFormLayout()

        nbTitle = QLabel("Enter Notebook Title:")

        self.le_item = QLineEdit()

        self.check = QCheckBox()
        self.check.stateChanged.connect(self.checktoggle)

        self.btn_listIcon = QPushButton('Choose Icon')
        self.btn_listIcon.setEnabled(False)
        self.btn_listIcon.clicked.connect(self.chooseListIcon)

        self.le_path = QLineEdit()
        self.le_path.setReadOnly(True)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.item_ok)
        buttonBox.rejected.connect(self.cancel)

        self.item_dialog.setLayout(self.layout_item)
        self.layout_item.addRow(nbTitle)
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

        fname = QFileDialog.getOpenFileName(self.MainWindow, 'Open File', 'images\icons')
        fname = str(fname[0])
        self.item_filename = fname
        self.le_path.setText(fname)



    def item_ok(self):

        self.checkInfo = self.check.isChecked()

        if self.checkInfo == False and self.le_item.text() != False:
            self.ico = QIcon()
            
            self.ico.addPixmap(QPixmap(self.defaultListIcon))
            
            item = QListWidgetItem()
            item.setIcon(self.ico)
            item_text = self.le_item.text()
            item.setText(item_text)
            self.list.addItem(item)
            deftabtitle = 'New Tab'
            self.tab_widget = QTabWidget()
            self.tab_widget.setMovable(True)
            self.tab_widget.setObjectName(item_text)

            self.sectioncontent = QTextEdit()
            self.sectioncontent.textChanged.connect(self.notebookstatus)
            self.tab_widget.addTab(self.sectioncontent, QIcon(self.deftabico), deftabtitle)

            self.stack.addWidget(self.tab_widget)

            self.list_icons_dict[item_text] = self.defaultListIcon

            # update tab icon dict as well since a default "New Tab" is being added.
            self.tabwidget_icons_dict[item_text] = {deftabtitle : self.deftabico}



        elif self.checkInfo == True and self.le_item.text() != False:

            self.ico = QIcon()
            self.ico_path = self.item_filename
            self.ico_path = self.item_filename
            self.ico.addPixmap(QPixmap(self.item_filename))
            item = QListWidgetItem()
            item.setIcon(self.ico)
            item_text = self.le_item.text()
            item.setText(item_text)
            self.list.addItem(item)
            self.tab_widget = QTabWidget()
            self.tab_widget.setMovable(True)
            self.tab_widget.setObjectName(item_text)
            self.stack.addWidget(self.tab_widget)

            self.list_icons_dict.update({item_text : self.ico})


        else:
            self.item_msg_box = QMessageBox(self.MainWindow, 'Message', 'Please Enter a title for Notebook', QMessageBox.Ok)
            self.item_dialog.close()

        self.item_dialog.close()





    def chooseTabIcon(self):
        fname = QFileDialog.getOpenFileName(self.MainWindow, 'Open File', 'images\icons')
        fname = str(fname[0])
        self.tabicon_filename = fname
        self.le_tab_path.setText(fname)



    def tab_ok(self):

        self.check_tab_icon = self.combo_tab.isChecked()

        if self.check_tab_icon == False and self.le_text.text() != False:

            self.newtabicon = QIcon()
            self.newtabicon.addPixmap(QPixmap(self.deftabico), QIcon.Normal, QIcon.On)

            self.newTabName = self.le_text.text()            
            self.item = self.list.currentItem()
            self.curr_tab_wid = self.stack.findChild(QTabWidget, self.item.text())
            self.newtabname_textedit = QTextEdit()

            self.newtabname_textedit.textChanged.connect(self.notebookstatus)

            self.newtabname_textedit.setObjectName(str(self.newTabName))
            self.curr_tab_wid.addTab(self.newtabname_textedit, self.newtabicon ,self.newTabName)

            # below is working
            self.tabwidget_icons_dict[self.item.text()].update({self.newTabName : self.deftabico})


        elif self.check_tab_icon == True and self.le_text.text() != False:



            self.tab_ico = self.tabicon_filename


            self.ico = QIcon()
            self.ico.addPixmap(QPixmap(self.tab_ico), QIcon.Normal, QIcon.On)

            self.newTabName = self.le_text.text()            
            self.item = self.list.currentItem()
            self.curr_tab_wid = self.stack.findChild(QTabWidget, self.item.text())
            self.curr_tab_wid.addTab(QTextEdit(), self.ico, self.newTabName)

            self.tabwidget_icons_dict[self.item.text()].update({{self.newTabName : self.tab_ico}})


        else:
            self.tab_msg_box = QMessageBox(self, 'Message', 'Please Enter a title for TAb', QMessageBox.Ok)
            self.dialog.close()


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

            tabmsgbox = QMessageBox.question(self.MainWindow, 'Warning', 'This Tab will be permanently deleted. Be sure to backup your notes file before continuing. Are you sure that you want to Delete this Tab?', QMessageBox.Ok, QMessageBox.Cancel)

            if tabmsgbox == QMessageBox.Ok:
                self.item = self.list.currentItem()
                self.curr_tab_wid = self.stack.findChild(QTabWidget, self.item.text())
                self.curr_tab = self.curr_tab_wid.currentIndex()

                self.tabchanges.append(self.programcfg() + '/' + self.curr_tab_wid.tabText(self.curr_tab))

                del self.tabwidget_icons_dict[self.item.text()][self.curr_tab_wid.tabText(self.curr_tab)]


                self.curr_tab_wid.removeTab(self.curr_tab)



        if action == renameTab:
            tabRename, ok = QInputDialog.getText(self.tab_widget, 'Input Dialog', 'Enter new tab name')
            if ok:
                self.item = self.list.currentItem()
                self.curr_tab_wid = self.stack.findChild(QTabWidget, self.item.text())
                self.curr_tab = self.curr_tab_wid.currentIndex()


                print('curr_tab :', self.curr_tab_wid.tabText(self.curr_tab))

                self.tabchanges.append(self.programcfg() + '/' + self.item.text() + '/' + self.curr_tab_wid.tabText(self.curr_tab))

                print('tabrename :', tabRename)


                ti = self.tabwidget_icons_dict[self.item.text()].get(self.curr_tab_wid.tabText(self.curr_tab))

                del self.tabwidget_icons_dict[self.item.text()][self.curr_tab_wid.tabText(self.curr_tab)]


                self.tabwidget_icons_dict[self.item.text()].update({tabRename : ti})


                self.curr_tab_wid.setTabText(self.curr_tab, tabRename)





    def listMenu(self, event):
        self.contextMenu = QMenu()

        addListItem = self.contextMenu.addAction('Add New Notebook')
        deleteListItem = self.contextMenu.addAction('Delete Notebook')
        renameListItem = self.contextMenu.addAction('Rename Notebook')
        save = self.contextMenu.addAction('Save')



        action = self.contextMenu.exec_(self.list.mapToGlobal(event))

        if action == addListItem:
            self.itemMenu()
        elif action == deleteListItem:

            listmsgbox = QMessageBox.question(self.MainWindow, 'Warning', 'This notebook will be permanently deleted. Be sure to backup your notes file before continuing. Are you sure that you want to Delete this Notebook?', QMessageBox.Ok, QMessageBox.Cancel)
            
            if listmsgbox == QMessageBox.Ok:

                self.fpath = self.list.currentItem().text()
                self.item = self.list.currentItem()
                self.y = self.list.takeItem(self.list.row(self.item))#pops the list item out

                self.r = self.stack.findChild(QTabWidget, self.item.text())
                sip.delete(self.r)

                
                self.listchanges.append(self.programcfg() + '/' + self.fpath)

                # delete nested dictionary from tabwidgets_icons_dict
                del self.tabwidget_icons_dict[self.fpath]

                del self.list_icons_dict[self.fpath]


        elif action == renameListItem:
            newItemName, ok = QInputDialog.getText(self.list, 'Input Dialog','Notebook Name:')
            if ok:
                self.item = self.list.currentItem()
                self.curr_item = self.stack.findChild(QTabWidget, self.item.text())
                self.curr_item.setObjectName(newItemName)

                self.listchanges.append(self.programcfg() + '/' + self.item.text())

                self.list_icons_dict[newItemName] = self.list_icons_dict.pop(self.item.text())

                print('ListIcons', self.list_icons_dict)

                # update root dict key in tabwidget
                popped = self.tabwidget_icons_dict.pop(self.item.text())
                # create the root dict key with the new listitem name and assign the previously popped nested dict to it
                self.tabwidget_icons_dict[newItemName] = popped


                self.item.setText(newItemName)



        elif action == save:
            self.save()







    def passwordmenu(self):

        self.passdialog = QDialog(self)

        self.passlayout = QFormLayout()

        self.passlbl = QLabel("Password :")

        self.passle = QLineEdit()
        self.passle.setEchoMode(QLineEdit.Password)

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







    def uichanges(self):

        # if the list is empty
        if not self.listchanges:
            pass
        else:
            for h in self.listchanges:
                if os.path.exists(h):
                    shutil.rmtree(h)
                    print('removed')

        if not self.tabchanges:
            pass
        else:
            for g in self.tabchanges:
                shutil.rmtree(g)





    def programconfig(self, path):

        self.mww = self.MainWindow.width()
        self.mwh = self.MainWindow.height()
        self.mwx = self.MainWindow.x()
        self.mwy = self.MainWindow.y()  
        
        if not os.path.exists('settings'):
            os.makedirs('settings')

        settings_root = ET.Element('programSettings')
        settings_tree = ElementTree(settings_root)

        recentFilePath = ET.SubElement(settings_root, 'recentfilepath')
        recentFilePath.text = path

        mainw = ET.SubElement(settings_root, 'selfsize')
        mainw.text = 'selfsize'        
        mainw.set('x', str(self.mwx))
        mainw.set('y', str(self.mwy))
        mainw.set('width', str(self.mww))
        mainw.set('height', str(self.mwh))
        


        listsize = ET.SubElement(settings_root, 'listsize')
        listsize.text = 'listcoords'        
        listsize.set('width', str(self.list.width()))
        listsize.set('height', str(self.list.height()))


        stacksize = ET.SubElement(settings_root, 'stacksize')
        stacksize.text = 'stackcoords'        
        stacksize.set('width', str(self.stack.width()))
        stacksize.set('height', str(self.stack.height()))




        settings_tree.write(open('settings/programSettings.xml', 'wb'))





    def createFile(self):

        self.creatediaglog = QDialog()

        self.createfile_layout = QFormLayout()

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

        self.creatediaglog.setLayout(self.createfile_layout)
        self.createfile_layout.addRow(self.createbtn)
        self.createfile_layout.addRow(self.createle)
        self.createfile_layout.addRow(self.createPasslbl)
        self.createfile_layout.addRow(self.cb_pass, self.le_pass)
        self.createfile_layout.addRow(createfile_btnbox)

        self.creatediaglog.exec()


    def cbpasstoggle(self):

        self.le_pass.setReadOnly(False)


    def createclicked(self):

        f = QFileDialog.getSaveFileName(self.MainWindow, 'Save File')[0]
        
        self.createle.setText(f)


    def createok(self):

        self.saveFile = self.createle.text()
        self.pw = self.le_pass.text()

        global instance
        instance = self.saveFile

        if self.pw != "":

            if not os.path.exists(self.saveFile):
                
                self.savefile_fn = os.path.split(self.saveFile)
                self.savefile_fnh = self.savefile_fn[0]
                self.savefile_fnt = self.savefile_fn[1]
                
                os.makedirs(self.savefile_fnh + '/_{}'.format(self.savefile_fnt))
                self.saveFile = self.savefile_fnh + '/_{}'.format(self.savefile_fnt)


                instance = self.saveFile

                subprocess.run([r'7z\7-Zip\7z.exe', 'a', '-p{}'.format(self.pw) , '{}'.format(self.saveFile), '{}'.format(self.saveFile)], shell=False)


                root = ET.Element('programElements')
                tree = ElementTree(root)

                tree.write(open(self.saveFile + '/config.xml', 'wb'))

                xml = ET.parse('settings/programSettings.xml')

                rfp = xml.find('recentfilepath')
                rfp.text = str(self.saveFile)

                xml.write(open('settings/programSettings.xml', 'wb'))                
                # might have to make the self.notewin a different name than the one below
                self.notewin = NotesEditing()

                
                self.creatediaglog.close()



        else:

            if not os.path.exists(self.saveFile):
                os.makedirs(self.saveFile)
                

            root = ET.Element('programElements')
            tree = ElementTree(root)

            tree.write(open(self.saveFile + '/config.xml', 'wb'))

            xml = ET.parse('settings/programSettings.xml')

            rfp = xml.find('recentfilepath')
            rfp.text = str(self.saveFile)

            xml.write(open('settings/programSettings.xml', 'wb'))

            self.notewin = NotesEditing()

            self.creatediaglog.close()


    def createcancel(self):

        self.creatediaglog.close()



    # def extractfile(self, pw, fp):


    #     if '_' in '{}'.format(fp):

    #         self.loadpass()

    #         # apparently it doesnt need the -o flag.
    #         zippw = subprocess.run([r'7z\7-Zip\7z.exe', 'x', '-p{}'.format(pw), '{}.7z'.format(fp)], shell=False)
    #         print('Return Code :', zippw.returncode)

    #         if zippw.returncode == 0:
    #             pass
    #         else:
    #             box = QMessageBox(self.MainWindow)
    #             box.setText("Wrong Password")
    #             box.setWindowTitle("File Error")
    #             box.exec()
    #             if box == QMessageBox.Ok:
    #                 self.loadpass()

    #     else:
    #         subprocess.run([r'7z\7-Zip\7z.exe', 'x', '{}.7z'.format(fp)], shell=False)



    # def storefile(self, pw, fp):

    #     if '_' in fp:

    #         subprocess.run([r'7z\7-Zip\7z.exe', 'a', '-p{}'.format(pw) , '{}'.format(fp), '-o{}'.format(fp)], shell=False)

    #     else:
    #         subprocess.run([r'7z\7-Zip\7z.exe', 'a', '{}'.format(fp), '{}'.format(fp)], shell=False)



    def save(self):

        self.uichanges()

        self.saveFile = self.archive


        root = ET.Element('programElements')
        tree = ElementTree(root)

        

        for i in range(self.list.count()):
            self.liTxt = self.list.item(i).text()
            listitem = ET.SubElement(root, 'listitem')
            licon = self.list_icons_dict[self.liTxt]
            listitem.set('item_icon', licon)
            listitem.text = self.liTxt
        for g in range(self.stack.count()):
            self.stackTab = self.stack.widget(g)
            tabwidgetName = ET.SubElement(root, 'tabwid_name')
            tabwidgetName.text = self.stackTab.objectName()
            for p in range(self.stackTab.count()):
                self.tabtext = self.stackTab.tabText(p)
                self.ticon = self.tabwidget_icons_dict[self.stackTab.objectName()][self.tabtext]
                self.tabcontents = self.tabtext



                if not os.path.exists(os.path.splitext(self.saveFile)[0] + '/{}'.format(tabwidgetName.text) + '/{}/'.format(self.tabcontents)):
                    os.makedirs(os.path.splitext(self.saveFile)[0] + '/{}'.format(tabwidgetName.text) + '/{}/'.format(self.tabcontents))

                with open(r'{}'.format(os.path.splitext(self.saveFile)[0]) + r'/{}'.format(tabwidgetName.text) + r'/{}/{}.html'.format(self.tabcontents, self.tabcontents), 'w') as file:
                    file.write(self.stackTab.widget(p).toHtml())
                file.close()




                tabName = ET.SubElement(tabwidgetName, 'tabName')
                tabName.set('content', str(self.tabcontents))
                tabName.set('tabIcon', self.ticon)
                tabName.text = self.tabtext

        tree.write(open(self.saveFile + '/config.xml', 'wb'))


        if '_' in self.saveFile:

            # used to add all files in the working directory with the -o flag and when i deleted it, it worked the way it should.....idk
            subprocess.run([r'7z\7-Zip\7z.exe', 'a', '-p{}'.format(self.pw) , '{}'.format(self.saveFile), '{}'.format(self.saveFile)], shell=False) 

        else:
            subprocess.run([r'7z\7-Zip\7z.exe', 'a', '{}'.format(self.saveFile), '{}'.format(self.saveFile)], shell=False)


        self.programconfig(self.saveFile)
        
        self.status = True









    def loadpass(self):

        self.enterpass = QDialog()

        self.loadpass_layout = QFormLayout()

        self.lp_lbl = QLabel('Enter Password :')

        self.lp_le = QLineEdit()
        self.lp_le.setEchoMode(QLineEdit.Password)

        lp_btnbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        lp_btnbox.accepted.connect(self.lp_ok)
        lp_btnbox.rejected.connect(self.lp_cancel)

        self.enterpass.setLayout(self.loadpass_layout)
        self.loadpass_layout.addRow(self.lp_lbl)
        self.loadpass_layout.addRow(self.lp_le)
        self.loadpass_layout.addRow(lp_btnbox)

        self.enterpass.exec()




    def lp_ok(self):

        self.pw = self.lp_le.text()

        self.enterpass.close()


    def lp_cancel(self):

        self.enterpass.close()

        return None

    

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
        self.noteFileOpen = QFileDialog.getOpenFileName(self.MainWindow, 'Open File')[0]

        self.loadfile = os.path.splitext(self.noteFileOpen)[0]

        xml = ET.parse('settings/programSettings.xml')

        y = xml.find('recentfilepath')
        y.text = str(self.loadfile)

        xml.write(open('settings/programSettings.xml', 'wb'))

        self.loadcheck()
        self.choice_dialog.close()



    def createNote(self):
        self.createFile()

        self.choice_dialog.close()



    def loadcheck(self):
        
        if instance == '':

            if os.path.exists('settings/programSettings.xml'):
                self.xmlSettingsLoad = ET.parse('settings/programSettings.xml')
                #self.xmlSettingsLoad.getroot()

                for o in self.xmlSettingsLoad.findall('recentfilepath'):
                    recent = o.text
                    print('RECENT' , recent)
                    
                    if not recent:
                        self.archive = None

                        return

                    elif os.path.exists(str(recent) + '.7z'):
                        self.loadfile = o.text                    
                        # need to extract first
                        self.load(self.loadfile)

                    else:
                        print("cant find the file you are trying to open")
                        self.archive = None
                        return
        
        elif instance:

            self.load(instance)









    def load(self, x):


        self.archive = x


        if '_' in '{}'.format(self.archive):
            
            while True:

                self.loadpass()

                if self.pw != '':

                    # apparently it doesnt need the -o switch...
                    zippw = subprocess.run([r'7z\7-Zip\7z.exe', 'x', '-p{}'.format(self.pw), '{}.7z'.format(self.archive)], shell=False)

                    if zippw.returncode == 0:
                        break
                    else:
                        box = QMessageBox(self.MainWindow)
                        box.setText("Wrong Password")
                        box.setWindowTitle("File Error")
                        box.exec()
                else:
                    return False

        else:
            subprocess.run([r'7z\7-Zip\7z.exe', 'x', '{}.7z'.format(self.archive)], shell=False)




        filename = ET.parse(r'{}{}'.format(os.path.splitext(self.archive)[0], r'/config.xml')).getroot()

        for listitem in filename.findall('listitem'):
            
            item = QListWidgetItem()
            icon = listitem.get('item_icon')
            self.ico = QIcon(icon)
            item.setIcon(self.ico)
            item.setText(listitem.text)
            self.list.addItem(item)

            self.list_icons_dict[listitem.text] = icon


        for tabwidget in filename.iter('tabwid_name'):
            self.tab_widget = QTabWidget()
            self.tab_widget.setObjectName(tabwidget.text)
            self.tab_widget.setMovable(True)
            self.stack.addWidget(self.tab_widget)
            self.tabwidget_icons_dict[tabwidget.text] = {}
            for tabname in tabwidget.iter('tabName'):
                self.id = self.stack.findChild(QTabWidget, tabwidget.text)
                self.tab_icon = tabname.get('tabIcon')
                self.tabico = QIcon(self.tab_icon)
                self.tabwidget_icons_dict[tabwidget.text].update({tabname.text : self.tab_icon})
                content = tabname.get('content')



                if os.path.exists(r'{}\{}'.format(os.path.splitext(self.loadfile)[0] ,self.tab_widget.objectName())):
                    


                    tE = QTextEdit()
                    tE.setObjectName(content)
                    tE.textChanged.connect(self.notebookstatus)
                    
                    with open(r'{}/{}/{}/{}.html'.format(os.path.splitext(x)[0] , self.tab_widget.objectName(), content, content), 'r') as file:
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
        
        for i in self.recentconfig.findall('selfsize'):
            self.mws_x = i.get('x')
            self.mws_y = i.get('y')
            self.mw_width = i.get('width')
            self.mw_height = i.get('height')


        self.MainWindow.setGeometry(int(self.mws_x), int(self.mws_y), int(self.mw_width), int(self.mw_height))

        for ls in self.recentconfig.findall('listsize'):

            self.list_width = ls.get('width')
            

        for ss in self.recentconfig.findall('stacksize'):

            self.ssize = ss.get('width')


        self.splitter.setSizes([int(self.list_width), int(self.ssize)])
