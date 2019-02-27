#!/usr/bin/env python
from PyQt5.QtWidgets import *
a = QApplication([])
m = QMainWindow()
m.setCentralWidget(QLabel("HELLO"))
m.show()
a.exec_()
