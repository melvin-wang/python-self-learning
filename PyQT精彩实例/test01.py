from PyQt5.QtWidgets import *

app = QApplication([])
btn = QPushButton("Hello Kitty")
btn.clicked.connect(app.exit)
btn.show()

app.exec()