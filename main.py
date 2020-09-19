import sys
from PyQt5.QtWidgets import QApplication
from editor import NotesEditing

application = QApplication(sys.argv)
application.setStyleSheet(open("qss/app.qss", "r").read())
application.setStyle('fusion')
Editor = NotesEditing()
sys.exit(application.exec_())


