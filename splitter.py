#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Python 3.6.2 and PyQt5 are used in this example


from PyQt5.QtWidgets import (
  QPushButton,
  QSplitter,
  QWidget,
  QApplication,
)

import sys


class ButtonWrapper(QPushButton):

    def sizeHint(self):

        return self.minimumSize()


class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.resize(400, 400)

        m = QSplitter(self)
        m.resize(200, 100)

        x = ButtonWrapper(self)
        x.setGeometry(0, 0, 100, 100)

        y = QPushButton(self)
        y.setGeometry(0, 100, 100, 100)

        m.addWidget(x)
        m.addWidget(y)

        m.setSizes([20, 180])

        #Now it really shows "20" as expected
        print(x.width())

        #minimumWidth() is zero by default for empty QPushButton
        print(x.minimumWidth())

        #Result of our overloaded sizeHint() method
        print(x.sizeHint().width())
        print(x.minimumSizeHint().width())

        self.setWindowTitle('Example')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())