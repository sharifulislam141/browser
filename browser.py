from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

class WebBrowser(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Web Browser")
        self.setGeometry(100, 100, 800, 600)
        
        # Create a QWebEngineView widget and set it as the central widget
        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.setCentralWidget(self.browser)
        
        # Create a QLineEdit widget for the URL bar
        self.urlbar = QtWidgets.QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        
        # Create a QToolBar and add the URL bar and navigation buttons
        self.toolbar = self.addToolBar("Navigation")
        self.toolbar.addWidget(self.urlbar)
        self.toolbar.addAction("Go", self.navigate_to_url)
        self.toolbar.addSeparator()
        self.toolbar.addAction("Back", self.browser.back)
        self.toolbar.addAction("Forward", self.browser.forward)
        self.toolbar.addAction("Refresh", self.browser.reload)
        
        # Connect the urlChanged signal to update the URL bar
        self.browser.urlChanged.connect(self.update_urlbar)
        
        # Show the window
        self.show()
        
    def navigate_to_url(self):
        url = self.urlbar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QtCore.QUrl(url))
        
    def update_urlbar(self, qurl):
        self.urlbar.setText(qurl.toString())
        self.urlbar.setCursorPosition(0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    browser = WebBrowser()
    sys.exit(app.exec_())
