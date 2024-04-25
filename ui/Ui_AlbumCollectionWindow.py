import sys
sys.path.append('C:/Users/Admin/Downloads/ProjectAudio_Report/ProjectPythonAudio/ui')
from loadImageFromUrl import loadImageFromUrl
from dao.AlbumDAO import AlbumDAO
# Other imports remain the same
from Ui_SongCollectionWindow import Ui_SongCollectionWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AlbumCollectionWindow(object):
    def setupUi(self, AlbumCollectionWindow, albums):  
        self.albums = albums

        AlbumCollectionWindow.setObjectName("AlbumCollectionWindow")
        AlbumCollectionWindow.setFixedSize(641, 1000)
        self.centralwidget = QtWidgets.QWidget(AlbumCollectionWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 70, 622, 791))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 620, 789))
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)

        for i, album in enumerate(self.albums):
            groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
            groupBox.setObjectName(f"groupBox_{i+1}")
            groupBox.setMinimumSize(QtCore.QSize(171, 201))
            groupBox.setMaximumSize(QtCore.QSize(171, 201))

            albumImage = QtWidgets.QLabel(groupBox)
            albumImage.setGeometry(QtCore.QRect(4, 20, 161, 111))
            albumImage.setText("")
            pixmap = loadImageFromUrl(album.cover_image)  # Sử dụng hàm loadImageFromUrl để tải hình ảnh từ URL
            albumImage.setPixmap(pixmap)
            albumImage.setScaledContents(True)
            albumImage.setObjectName(f"albumImage_{i+1}")

            albumTitle = QtWidgets.QLabel(groupBox)
            albumTitle.setGeometry(QtCore.QRect(10, 130, 151, 31))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            albumTitle.setFont(font)
            albumTitle.setObjectName(f"albumTitle_{i+1}")
            albumTitle.setText(album.name)

            releaseDate = QtWidgets.QLabel(groupBox)
            releaseDate.setGeometry(QtCore.QRect(10, 160, 151, 31))
            releaseDate.setObjectName(f"releaseDate_{i+1}")
            releaseDate.setText(album.release_date.strftime('%d-%m-%Y'))  # Chuyển đổi thành chuỗi ngày phát hành

            # Make album cover and title clickable
            albumImage.mousePressEvent = self.make_album_clickable(album.id)
            albumTitle.mousePressEvent = self.make_album_clickable(album.id)
            # Rest of your setupUi code
            playButton = QtWidgets.QPushButton(groupBox)
            playButton.setGeometry(QtCore.QRect(120, 150, 41, 41))
            font = QtGui.QFont()
            font.setPointSize(24)
            playButton.setFont(font)
            playButton.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("image/album.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            playButton.setIcon(icon)
            playButton.setIconSize(QtCore.QSize(32, 32))
            playButton.setObjectName(f"playButton_{i+1}")

            self.gridLayout.addWidget(groupBox, i // 3, i % 3)


        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        AlbumCollectionWindow.setCentralWidget(self.centralwidget)

        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(500, 30, 120, 40))  # Tăng chiều rộng và chiều cao
        self.btnBack.setObjectName("btnBack")
        self.btnBack.setText("⬅️ Back")  # Thêm icon và văn bản cho nút
        self.btnBack.clicked.connect(lambda: self.go_back(AlbumCollectionWindow))


        self.retranslateUi(AlbumCollectionWindow)
        QtCore.QMetaObject.connectSlotsByName(AlbumCollectionWindow)

    
    def center_window(self, window=None):
        if window is None:
            window = self.AlbumCollectionWindow
        screen_size = QtWidgets.QDesktopWidget().screenGeometry(-1)
        window_size = window.frameGeometry()
        left = (screen_size.width() - window_size.width()) // 2
        top = (screen_size.height() - window_size.height()) // 15
        window.move(left, top)
    # Method to handle click event
    def make_album_clickable(self, album_id):
        def on_click(event):
            # Retrieve the list of songs in the clicked album
            songs = AlbumDAO().get_songs_in_album(album_id)
            # Assuming that show_song_collection will handle the display of songs
            self.show_song_collection(songs)
        return on_click
    
    # Method to display song collection
    def show_song_collection(self, songs):
        # This assumes you have a QMainWindow or similar to show the songs
        self.songCollectionWindow = QtWidgets.QMainWindow()
        self.ui = Ui_SongCollectionWindow()
        self.ui.setupUi(self.songCollectionWindow, songs)  # Pass songs to the song collection UI
        self.center_window(self.songCollectionWindow)  # Chỉnh cửa sổ để nằm chính giữa màn hình
        self.songCollectionWindow.show()

    # Method to go back
    def go_back(self, AlbumCollectionWindow):
        # Close the current window
        AlbumCollectionWindow.close()

    def retranslateUi(self, AlbumCollectionWindow):
        _translate = QtCore.QCoreApplication.translate
        AlbumCollectionWindow.setWindowTitle(_translate("AlbumCollectionWindow", "Album Collection"))
        for i, album in enumerate(self.albums):
            groupBox = self.scrollAreaWidgetContents.findChild(QtWidgets.QGroupBox, f"groupBox_{i+1}")
            if groupBox:
                groupBox.setTitle(_translate("AlbumCollectionWindow", f"Album {i+1}"))
                albumTitle = groupBox.findChild(QtWidgets.QLabel, f"albumTitle_{i+1}")
                if albumTitle:
                    albumTitle.setText(_translate("AlbumCollectionWindow", album.name))  # Sử dụng tên thực của album


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    AlbumCollectionWindow = QtWidgets.QMainWindow()
    ui = Ui_AlbumCollectionWindow()
    album_dao = AlbumDAO()
    albums = album_dao.get_all_albums()  
    ui.setupUi(AlbumCollectionWindow, albums)
    AlbumCollectionWindow.show()
    sys.exit(app.exec_())