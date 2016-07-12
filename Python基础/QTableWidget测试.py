from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

app = QApplication(sys.argv)
table = QTableWidget(3, 5)
table.setEditTriggers(QAbstractItemView.NoEditTriggers)
table.setSelectionBehavior(QAbstractItemView.SelectRows)
table.setSelectionMode(QAbstractItemView.MultiSelection)

for r in range(table.rowCount()):
    for c in range(table.columnCount()):
        item = QTableWidgetItem()
        item.setText("第{0}行，第{1}列".format(r + 1, c + 1))
        table.setItem(r, c, item)

item1 = table.item(0, 0)
item1.setText('改动')
item1.setBackgroundColor(QColor(255, 0, 0))


win = QWidget()
# win.setWindowFlags(Qt.Popup)
layout = QHBoxLayout()
layout.addWidget(table)
win.setLayout(layout)
win.show()
sys.exit(app.exec())
