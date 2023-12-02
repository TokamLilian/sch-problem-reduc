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
        self.setGeometry(100, 100, 2000, 1600)
        self.setWindowTitle("Graph Coloring")
        self.setWindowIcon(QIcon('static/images/image01.jpeg'))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # URL of your Flask app serving HTML content
    flask_url = "http://127.0.0.1:5001/"

    viewer = HtmlViewer(flask_url)
    viewer.show()

    sys.exit(app.exec_())
#
#In this code, we have a `QMainWindow` application that displays a webpage using the `QWebEngineView` widget. The `WebPage` class is a subclass of `QWebEnginePage` that provides additional functionality, such as handling JavaScript console messages.
#
#The `HtmlViewer` class is responsible for creating the main window and setting up the `QWebEngineView` widget. It takes a URL as input, which should be the URL of your Flask app serving the HTML content.
#
#The `on_load_finished` method in the `WebPage` class is called when the webpage has finished loading. If the load was successful (indicated by the `ok` parameter), the main window is shown.
#
#The `javaScriptConsoleMessage` method in the `WebPage` class is called when there is a console message from the JavaScript code running on the webpage. It prints the message, along with its level, source ID, and line number.
#
#Finally, the `QApplication` object is created and executed, and the `HtmlViewer` object is created with the specified Flask URL. The main window is shown, and the application runs until the user closes it..</s>