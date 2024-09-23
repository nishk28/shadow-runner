import sys
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QWebEngineView widget
        self.browser = QWebEngineView()

        # Get the absolute path of the HTML file
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'index.html'))

        # Ensure the file exists
        if not os.path.exists(file_path):
            print(f"Error: {file_path} does not exist.")
            sys.exit()

        # Load the local HTML file using the absolute path
        self.browser.setUrl(QUrl.fromLocalFile(file_path))

        # Set the browser as the central widget of the window
        self.setCentralWidget(self.browser)

        # Set window properties
        self.setWindowTitle('Shadow Runner')
        self.showMaximized()

# Create the application
app = QApplication(sys.argv)

# Create and show the main window
window = MainWindow()

# Run the application
sys.exit(app.exec_())
