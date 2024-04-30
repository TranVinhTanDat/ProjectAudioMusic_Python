import sys
sys.path.append('C:/Users/Admin/Downloads/ProjectAudio_Report/ProjectPythonAudio')
from PyQt5 import QtCore, QtGui, QtWidgets
from loadImageFromUrl import loadImageFromUrl
from dao.SongDAO import SongDao
from dao.TypeDAO import TypeDao
from Ui_SongCollectionWindow import Ui_SongCollectionWindow
from unity.main_list_music import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QPushButton, QDesktopWidget, QLabel

class Ui_DanhSachNhacWindow(object):
    def setupUi(self, DanhSachNhacWindow, songs):  
        self.songs = songs

        DanhSachNhacWindow.setObjectName("DanhSachNhacWindow")
        DanhSachNhacWindow.setFixedSize(641, 1000)
        self.centralwidget = QtWidgets.QWidget(DanhSachNhacWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Tạo một QLabel để hiển thị hình ảnh nền
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 641, 1000))  # Đặt kích thước là toàn bộ cửa sổ
        self.background_label.setPixmap(QPixmap("image/anhnen11.jpg"))  # Đặt hình ảnh nền
        self.background_label.setScaledContents(True)  # Thay đổi kích thước hình ảnh để vừa với kích thước của QLabel
        self.background_label.setObjectName("background_label")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 70, 641, 791))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 620, 789))
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)

        self.DanhSachNhacWindow = DanhSachNhacWindow  # Thêm dòng này để lưu trữ QMainWindow

        for i, song in enumerate(self.songs):
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

            playButton = QtWidgets.QPushButton(groupBox)
            playButton.setGeometry(QtCore.QRect(120, 150, 41, 41))
            font = QtGui.QFont()
            font.setPointSize(24)
            playButton.setFont(font)
            playButton.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("image/play-button.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            playButton.setIcon(icon)
            playButton.setIconSize(QtCore.QSize(32, 32))
            playButton.setObjectName(f"playButton_{i+1}")

            self.gridLayout.addWidget(groupBox, i // 3, i % 3)
            
            # In class Ui_DanhSachNhacWindow, within setupUi, for each song in songs:
            groupBox.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            groupBox.customContextMenuRequested.connect(lambda point, s=song.id, g=groupBox: self.show_context_menu(point, s, g))

            # playButton.clicked.connect(partial(self.playMusic, song.id))  # sửa self.list[0].id thành song.id

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        DanhSachNhacWindow.setCentralWidget(self.centralwidget)

        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(500, 30, 120, 40))  # Tăng chiều rộng và chiều cao
        self.btnBack.setObjectName("btnBack")
        self.btnBack.setText("⬅️ Back")  # Thêm icon và văn bản cho nút
        # self.btnBack.clicked.connect(lambda: self.go_back(DanhSachNhacWindow))

        self.btnAlbum = QtWidgets.QPushButton(self.centralwidget)
        self.btnAlbum.setGeometry(QtCore.QRect(80, 30, 120, 40))  # Tăng chiều rộng và chiều cao
        self.btnAlbum.setObjectName("btnAlbum")
        self.btnAlbum.setText("📀 Album")  # Thêm icon và văn bản cho nút
        self.btnAlbum.clicked.connect(self.show_album)

        self.btnSinger = QtWidgets.QPushButton(self.centralwidget)
        self.btnSinger.setGeometry(QtCore.QRect(200, 30, 120, 40))  # Tăng chiều rộng và chiều cao
        self.btnSinger.setObjectName("btnSinger")
        self.btnSinger.setText("🎤 Singer")  # Thêm icon và văn bản cho nút
        self.btnSinger.clicked.connect(self.show_singer)

        self.btnPlaylist = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlaylist.setGeometry(QtCore.QRect(320, 30, 120, 40))  # Tăng chiều rộng và chiều cao
        self.btnPlaylist.setObjectName("btnPlaylist")
        self.btnPlaylist.setText("🎵 Playlist")  # Thêm icon và văn bản cho nút
        self.btnPlaylist.clicked.connect(self.show_playlist)



        self.retranslateUi(DanhSachNhacWindow)
        QtCore.QMetaObject.connectSlotsByName(DanhSachNhacWindow)

        # In class Ui_DanhSachNhacWindow
    def show_context_menu(self, point, song_id, widget):
        context_menu = QtWidgets.QMenu()
        delete_action = context_menu.addAction("Delete Song")
        action = context_menu.exec_(widget.mapToGlobal(point))
        if action == delete_action:
            self.delete_song(song_id)
    # In class Ui_DanhSachNhacWindow
    def delete_song(self, song_id):
        # Here you call the delete method of SongDao to delete the song
        song_dao = SongDao()
        song_dao.delete_song(song_id)
        # Now you should refresh the UI to reflect the deletion
        self.refresh_ui()
    # In class Ui_DanhSachNhacWindow
    def refresh_ui(self):
        # Remove the old widgets from the gridLayout
        for i in reversed(range(self.gridLayout.count())): 
            widget_to_remove = self.gridLayout.itemAt(i).widget()
            # remove it from the layout list
            self.gridLayout.removeWidget(widget_to_remove)
            # remove it from the gui
            widget_to_remove.setParent(None)
        
        # Reload the songs from the database
        self.songs = SongDao().SelectList()
        # Call setupUi again or another method to repopulate the song list
        self.setupUi(self.DanhSachNhacWindow, self.songs)

    def make_song_clickable(self, song_id):
        def on_click(event):
            self.show_song_details(song_id)
        return on_click
    
    def show_song_details(self, song_id):
        songs = SongDao().get_song_by_id(song_id)
        self.show_song_collection(songs)

    def show_song_collection(self, songs):
        self.songCollectionWindow = QtWidgets.QMainWindow()
        self.ui = Ui_SongCollectionWindow()
        self.ui.setupUi(self.songCollectionWindow, songs)
        self.songCollectionWindow.show()

    # def go_back(self, DanhSachNhacWindow):
    #     DanhSachNhacWindow.close()

    def show_album(self):
        # Thêm mã để hiển thị cửa sổ danh sách Album ở đây
        pass

    def show_singer(self):
        # Thêm mã để hiển thị cửa sổ danh sách Singer ở đây
        pass

    def show_playlist(self):
        # Thêm mã để hiển thị cửa sổ danh sách Playlist ở đây
        pass

    def retranslateUi(self, DanhSachNhacWindow):
        _translate = QtCore.QCoreApplication.translate
        DanhSachNhacWindow.setWindowTitle(_translate("DanhSachNhacWindow", "Danh Sách Nhạc"))
        for i, song in enumerate(self.songs):
            groupBox = self.scrollAreaWidgetContents.findChild(QtWidgets.QGroupBox, f"groupBox_{i+1}")
            if groupBox:
                groupBox.setTitle(_translate("DanhSachNhacWindow", f"Bài hát {i+1}"))
                songName = groupBox.findChild(QtWidgets.QLabel, f"songName_{i+1}")
                if songName:
                    songName.setText(_translate("DanhSachNhacWindow", song.name))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    DanhSachNhacWindow = QtWidgets.QMainWindow()
    ui = Ui_DanhSachNhacWindow()
    song_dao = SongDao()
    songs = song_dao.SelectList()  
    ui.setupUi(DanhSachNhacWindow, songs)
    DanhSachNhacWindow.show()
    sys.exit(app.exec_())

