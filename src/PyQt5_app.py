import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtGui import QIcon

class WebPage(QWebEnginePage):
    def __init__(self, parent=None):
        super(WebPage, self).__init__(parent)

    def on_load_finished(self, ok):
        print("Load finished:", ok)
        if ok:
            
            viewer.show()

    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceID):
        print(f"Console message ({level}): {message} (line {lineNumber})")


class HtmlViewer(QMainWindow):
    def __init__(self, flask_url):
        super().__init__()

        self.webview = QWebEngineView()
        self.webpage = WebPage(self.webview)
        self.webview.setPage(self.webpage)

        # Load HTML content from Flask app URL
        self.webview.load(QUrl(flask_url))

        # Connect signals for debugging
        self.webpage.loadFinished.connect(self.webpage.on_load_finished)

        self.setCentralWidget(self.webview)
        self.setGeometry(100, 100, 1200, 1000)
        self.setWindowTitle("Graph Coloring")
        self.setWindowIcon(QIcon('static/images/image01.jpeg'))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # URL of your Flask app serving HTML content
    flask_url = "http://127.0.0.1:5001/"

    viewer = HtmlViewer(flask_url)
    viewer.show()

    sys.exit(app.exec_())