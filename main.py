import sys
from PyQt5.QtWidgets import QApplication
from editor import NotesEditing

application = QApplication(sys.argv)
Editor = NotesEditing()
sys.exit(application.exec_())