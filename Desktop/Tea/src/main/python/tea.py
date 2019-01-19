from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
import sys

def setUpUi(version, window):
    window.setWindowTitle("Tea v" + version)
    wid = QWidget(window)
    window.setCentralWidget(wid)
    #layout = QVBoxLayout()
    layout = QGridLayout(wid)
    labelMood = QLabel()
    labelMood.setText("Choose your mood:")
    moods = QComboBox()
    moodsList = ['cheerful', 'swag', 'soothening','heartbroken']
    exitButton = QPushButton()
    exitButton.setText("Exit")
    exitButton.clicked.connect(closeMe)

    for mood in moodsList: 
        moods.addItem(mood)
    
    moods.currentIndexChanged[str].connect(text_changed)
    layout.addWidget(labelMood, 0, 0)
    layout.addWidget(moods, 1, 0)
    layout.addWidget(exitButton, 2, 0)
    window.webview = QtWebEngineWidgets.QWebEngineView()
    window.webview.setUrl(QUrl("https://www.youtube.com/watch?v=kx-dGsRA40w"))
    layout.addWidget(window.webview)
    window.setGeometry(10, 10, 400, 400)

def text_changed(str):
    print(str)

def closeMe(): 
    print ("Bye!")
    sys.exit()

