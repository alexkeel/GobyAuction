import sys
from PyQt5 import QtWidgets, QtGui
import GUI
import SqlHandler
    
app = QtWidgets.QApplication(sys.argv)
my_gui = GUI.GUI()
my_gui.start()
sys.exit(app.exec_())
