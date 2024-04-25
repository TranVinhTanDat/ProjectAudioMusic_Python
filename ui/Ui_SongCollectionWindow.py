from PyQt5 import QtCore, QtGui, QtWidgets
from loadImageFromUrl import loadImageFromUrl

class Ui_SongCollectionWindow(object):
    def setupUi(self, MainWindow, songs):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(641, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 70, 622, 791))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 620, 789))
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)

        for i, song in enumerate(songs):
            groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
            groupBox.setObjectName(f"groupBox_{i+1}")
            groupBox.setMinimumSize(QtCore.QSize(171, 201))
            groupBox.setMaximumSize(QtCore.QSize(171, 201))
            songImage = QtWidgets.QLabel(groupBox)
            songImage.setGeometry(QtCore.QRect(4, 20, 161, 111))
            songImage.setText("")
            songImage.setScaledContents(True)
            songImage.setObjectName(f"songImage_{i+1}")

            if song.image and song.image.strip():
                pixmap = loadImageFromUrl(song.image)
            else:
                # Đường dẫn đến hình ảnh mặc định, bạn cần thay thế bằng hình ảnh mặc định của mình
                pixmap = QtGui.QPixmap('image/tai_nghe.jpg')
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

            # Add play button
            playButton = QtWidgets.QPushButton(groupBox)
            playButton.setGeometry(QtCore.QRect(120, 150, 41, 41))
            font = QtGui.QFont()
            font.setPointSize(24)
            playButton.setFont(font)
            playButton.setText("")
            icon = QtGui.QIcon()
            # Cung cấp đường dẫn đúng đắn đến biểu tượng play của bạn
            icon.addPixmap(QtGui.QPixmap("image/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Song Collection"))

    def playMusic(self, song_id):
        from main import MainWindow  # Import lớp MainWindow từ file main.py
        self.main_window = MainWindow()
        self.main_window.playMusicToID(song_id)
        self.main_window.show()
