from PyQt5 import QtCore, QtGui, QtWidgets
from loadImageFromUrl import loadImageFromUrl
from unity.main_list_music import *
class Ui_ArtistSongCollectionWindow(object):
    def setupUi(self, MainWindow, songs):
        MainWindow.setObjectName("ArtistSongCollectionWindow")
        MainWindow.setFixedSize(641, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 641, 1000))
        self.background_label.setPixmap(QPixmap("image/anhnen11.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.setObjectName("background_label")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 70, 641, 791))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 641, 791))
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)

        for i, song in enumerate(songs):
            groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
            groupBox.setObjectName(f"groupBox_{i+1}")
            groupBox.setMinimumSize(QtCore.QSize(171, 201))

            songImage = QtWidgets.QLabel(groupBox)
            songImage.setGeometry(QtCore.QRect(4, 20, 161, 111))
            songImage.setText("")
            songImage.setScaledContents(True)
            songImage.setObjectName(f"songImage_{i+1}")

            pixmap = QtGui.QPixmap('image/MUSIC.jpg')
            if song.image and song.image.strip():
                pixmap = loadImageFromUrl(song.image)
            songImage.setPixmap(pixmap)

            songName = QtWidgets.QLabel(groupBox)
            songName.setGeometry(QtCore.QRect(10, 130, 151, 31))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            songName.setFont(font)
            songName.setObjectName(f"songName_{i+1}")
            songName.setText(song.name)

            artistName = QtWidgets.QLabel(groupBox)
            artistName.setGeometry(QtCore.QRect(10, 160, 151, 31))
            artistName.setObjectName(f"artistName_{i+1}")
            artistName.setText(song.artist_name)

            playButton = QtWidgets.QPushButton(groupBox)
            playButton.setGeometry(QtCore.QRect(120, 150, 41, 41))
            font = QtGui.QFont()
            font.setPointSize(24)
            playButton.setFont(font)
            playButton.setText("")
            icon = QtGui.QIcon("image/play-button.svg")
            playButton.setIcon(icon)
            playButton.setIconSize(QtCore.QSize(32, 32))
            playButton.setObjectName(f"playButton_{i+1}")

            self.gridLayout.addWidget(groupBox, i // 3, i % 3)

            playButton.clicked.connect(lambda _, s=song.id: self.playMusic(s))

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Artist's Song Collection"))

    def playMusic(self, song_id):
        from main import MainWindow
        self.main_window = MainWindow()
        self.main_window.playMusicToID(song_id)
        self.main_window.show()

