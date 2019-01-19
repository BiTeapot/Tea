from PyQt5.QtWidgets import *
from PyQt5 import *
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

    
    layout.addWidget(labelMood, 0, 0)
    layout.addWidget(moods, 1, 0)
    layout.addWidget(exitButton, 2, 0)

    #wid.setLayout(layout)
    window.setGeometry(10, 10, 400, 400)

def closeMe(): 
    print ("Bye!")
    sys.exit()

