from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMenu
from PyQt5.QtGui import QPixmap  # Import QPixmap để làm việc với hình ảnh

from loadImageFromUrl import loadImageFromUrl
from dao.PlaylistDAO import PlaylistDAO
from dao.SongDAO import SongDao


class Ui_PlaylistSongCollectionWindow(object):
    def __init__(self, current_playlist_id):
        self.current_playlist_id = current_playlist_id

    def setupUi(self, MainWindow, songs):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(641, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Tạo một QLabel để hiển thị hình ảnh nền
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 641, 1000))  # Đặt kích thước là toàn bộ cửa sổ
        self.background_label.setPixmap(QPixmap("image/anhnen11.jpg"))  # Đặt hình ảnh nền
        self.background_label.setScaledContents(True)  # Thay đổi kích thước hình ảnh để vừa với kích thước của QLabel
        self.background_label.setObjectName("background_label")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 70, 622, 791))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 622, 789))
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

            playButton.clicked.connect(lambda _, s=song.id: self.playMusic(s))

            # Kết nối sự kiện chuột phải để hiển thị menu context
            groupBox.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            groupBox.customContextMenuRequested.connect(lambda point, s=song.id, groupBox=groupBox: self.show_context_menu(point, s, groupBox))



        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.addMusicButton = QtWidgets.QPushButton(self.centralwidget)
        self.addMusicButton.setGeometry(QtCore.QRect(262, 10, 140, 40))  # Tăng chiều rộng và chiều cao
        self.addMusicButton.setObjectName("addMusicButton")
        self.addMusicButton.setText("➕ Add Music to Playlist")  # Thêm icon và văn bản cho nút
        self.addMusicButton.clicked.connect(self.show_add_music_dialog)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Song Collection"))

    def playMusic(self, song_id):
        from main import MainWindow
        self.main_window = MainWindow()
        self.main_window.playMusicToID(song_id)
        self.main_window.show()

    def show_add_music_dialog(self):
        self.add_music_dialog = AddMusicDialog(parent=self.centralwidget, current_playlist_id=self.current_playlist_id)
        self.add_music_dialog.added_song.connect(lambda: self.reload_interface(self.centralwidget.window(),
                                                                                self.current_playlist_id))
        self.add_music_dialog.exec_()



    def reload_interface(self, MainWindow, current_playlist_id):
        ui = Ui_PlaylistSongCollectionWindow(current_playlist_id)
        songs = PlaylistDAO().get_songs_in_playlist(current_playlist_id)
        ui.setupUi(MainWindow, songs)

    # Thêm hàm để hiển thị menu context
# Thêm hàm để hiển thị menu context
    def show_context_menu(self, point, song_id, groupBox):
        context_menu = QtWidgets.QMenu()
        delete_action = context_menu.addAction("Delete Song")
        
        # Use the groupBox to map to global coordinates
        global_point = groupBox.mapToGlobal(point)
        
        # Hiển thị menu tại vị trí chuột phải được click
        action = context_menu.exec_(global_point)
        if action == delete_action:
            self.delete_song(song_id, groupBox.window())






    def delete_song(self, song_id, MainWindow):
        playlist_id = self.current_playlist_id
        PlaylistDAO().delete_song_from_playlist(playlist_id, song_id)
        # Refresh giao diện sau khi xóa bài hát
        self.reload_interface(MainWindow, playlist_id)


class AddMusicDialog(QtWidgets.QDialog):
    added_song = QtCore.pyqtSignal()

    def __init__(self, parent=None, current_playlist_id=None):
        super(AddMusicDialog, self).__init__(parent)
        self.current_playlist_id = current_playlist_id
        self.setWindowTitle("Add Music to Playlist")
        layout = QtWidgets.QVBoxLayout()

        self.song_combobox = QtWidgets.QComboBox()
        self.load_songs()
        layout.addWidget(QtWidgets.QLabel("Select Song:"))
        layout.addWidget(self.song_combobox)

        self.add_button = QtWidgets.QPushButton("Add")
        self.add_button.clicked.connect(self.add_song_to_playlist)  # Connect the button to the method
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def load_songs(self):
        songDAO = SongDao()
        songs = songDAO.SelectList()
        for song in songs:
            self.song_combobox.addItem(song.name, song.id)

    def add_song_to_playlist(self):  # Define the method to add the song to the playlist
            selected_song_id = self.song_combobox.currentData()
            if selected_song_id:
                playlistDAO = PlaylistDAO()
                # Kiểm tra xem bài hát đã tồn tại trong playlist chưa
                if playlistDAO.check_song_in_playlist(self.current_playlist_id, selected_song_id):
                    QMessageBox.warning(self, "Error", "The selected song already exists in the playlist.")
                else:
                    playlistDAO.add_song_to_playlist(self.current_playlist_id, selected_song_id)
                    QMessageBox.information(self, "Success", "Added song to playlist successfully!")
                    self.accept()
                    self.added_song.emit()
            else:
                QMessageBox.warning(self, "Error", "Please select a song.")
