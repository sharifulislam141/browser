from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget

app = QApplication([])

view = QWebEngineView()
view.load(QUrl("http://www.google.com"))

layout = QVBoxLayout()
layout.addWidget(view)

window = QWidget()
window.setLayout(layout)
window.show()

app.exec_()
