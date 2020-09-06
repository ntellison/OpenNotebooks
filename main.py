import sys
from PyQt5.QtWidgets import QApplication
from appback import NotesEditing

application = QApplication(sys.argv)
Editor = NotesEditing()
sys.exit(application.exec_())