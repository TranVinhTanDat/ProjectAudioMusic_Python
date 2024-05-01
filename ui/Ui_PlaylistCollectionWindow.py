import sys
sys.path.append('C:/Users/Admin/Downloads/ProjectAudio_Report/ProjectPythonAudio')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap  # Import QPixmap để làm việc với hình ảnh
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel  # Import các widget chính

from dao.PlaylistDAO import PlaylistDAO
from dao.TypeDAO import TypeDao
from dao.SongDAO import SongDao
from Ui_PlaylistSongCollectionWindow import Ui_PlaylistSongCollectionWindow
from loadImageFromUrl import loadImageFromUrl
import traceback
from PyQt5.QtWidgets import QApplication, QMainWindow
import os

class Ui_PlaylistCollectionWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(641, 1000)
        self.main_window = MainWindow

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        # Tạo một QLabel để hiển thị hình ảnh nền
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 641, 1000))
        self.background_label.setPixmap(QPixmap("image/anhnen11.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.setObjectName("background_label")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.addMusicButton = QtWidgets.QPushButton(self.centralwidget)
        
        self.addMusicButton.setObjectName("addMusicButton")
        self.addMusicButton.setText("🎵 Add Music to Playlist")
        self.addMusicButton.setFixedSize(180, 40)

        self.horizontalLayout.addWidget(self.addMusicButton)

        self.btnAddPlaylist = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddPlaylist.setObjectName("btnAddPlaylist")
        self.btnAddPlaylist.setText("📚 Add Playlist") 
        self.btnAddPlaylist.setFixedSize(180, 40)  

        self.horizontalLayout.addWidget(self.btnAddPlaylist)

        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setObjectName("btnBack")
        self.btnBack.setText("⬅️ Back")  
        self.btnBack.setFixedSize(180, 40)  

        self.horizontalLayout.addWidget(self.btnBack)


        self.centralLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.centralLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setAlignment(QtCore.Qt.AlignHCenter)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 70, 622, 791))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 620, 789))
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)

        self.playlistDAO = PlaylistDAO()

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.centralLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnAddPlaylist.clicked.connect(self.add_playlist)
        self.addMusicButton.clicked.connect(self.show_add_music_dialog)
        self.render_playlists()
        self.btnBack.clicked.connect(lambda: self.go_back(MainWindow))
    
    def go_back(self, MainWindow): 
        MainWindow.close()
    def reload_interface(self):
        self.setupUi(self.main_window)
    
    def add_playlist(self):
        self.add_playlist_form = AddPlaylistForm(self.main_window)
        self.add_playlist_form.move(850, 350)
        self.add_playlist_form.playlist_added.connect(lambda: self.render_playlists())
        result = self.add_playlist_form.exec_()
        if result == QtWidgets.QDialog.Accepted:
            self.main_window.update()
            self.reload_interface()

    def show_playlist_songs(self, playlist_id):
        def on_click(event):
            if event.button() == QtCore.Qt.RightButton:
                self.show_context_menu(event, playlist_id)
            else:
                self.playlistSongCollectionWindow = QtWidgets.QMainWindow()
                # Truyền playlist_id vào khi khởi tạo Ui_PlaylistSongCollectionWindow
                self.playlistSongCollectionUI = Ui_PlaylistSongCollectionWindow(playlist_id)
                songs = self.playlistDAO.get_songs_in_playlist(playlist_id)
                self.playlistSongCollectionUI.setupUi(self.playlistSongCollectionWindow, songs)
                self.playlistSongCollectionWindow.show()
                self.center_window(self.playlistSongCollectionWindow)

        return on_click

    def show_context_menu(self, event, playlist_id):
        context_menu = QtWidgets.QMenu()
        edit_action = context_menu.addAction("Edit Playlist")
        delete_action = context_menu.addAction("Delete Playlist")

        action = context_menu.exec_(QtGui.QCursor.pos())
        if action == edit_action:
            self.edit_playlist(playlist_id)
        elif action == delete_action:
            self.delete_playlist(playlist_id)
    def edit_playlist(self, playlist_id):
        playlist = self.playlistDAO.get_playlist_by_id(playlist_id)
        if playlist:
            dialog = EditPlaylistForm(self.main_window, playlist, self.playlistDAO)  # Chuyển playlistDAO sang EditPlaylistForm
            dialog.playlist_edited.connect(self.reload_interface)
            result = dialog.exec_()
            if result == QtWidgets.QDialog.Accepted:
                self.reload_interface()


    def delete_playlist(self, playlist_id):
        reply = QtWidgets.QMessageBox.question(self.main_window, 'Delete Playlist', 'Are you sure you want to delete this playlist?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.playlistDAO.delete_playlist(playlist_id)
            self.reload_interface()


    def render_playlists(self):
        for i in reversed(range(self.gridLayout.count())):
            widget = self.gridLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        self.playlists = self.playlistDAO.get_all_playlists()
        
        for i, playlist in enumerate(self.playlists):
            groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
            groupBox.setObjectName(f"groupBox_{i+1}")
            groupBox.setMinimumSize(QtCore.QSize(171, 201))
            groupBox.setMaximumSize(QtCore.QSize(171, 201))

            playlistImage = QtWidgets.QLabel(groupBox)
            playlistImage.setGeometry(QtCore.QRect(4, 20, 161, 111))
            playlistImage.setText("")
            
            # Kiểm tra nếu đường dẫn là URL hợp lệ, thì tải từ URL, ngược lại sử dụng hình ảnh từ đường dẫn file
            if playlist.image and playlist.image.startswith("http"):
                pixmap = loadImageFromUrl(playlist.image)
            elif playlist.image and os.path.exists(playlist.image):
                pixmap = QtGui.QPixmap(playlist.image)
            else:
                pixmap = QtGui.QPixmap("image/MUSIC.jpg")
            
            playlistImage.setPixmap(pixmap)
            playlistImage.setScaledContents(True)
            playlistImage.setObjectName(f"playlistImage_{i+1}")

            playlistName = QtWidgets.QLabel(groupBox)
            playlistName.setGeometry(QtCore.QRect(10, 130, 151, 31))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            playlistName.setFont(font)
            playlistName.setObjectName(f"playlistName_{i+1}")
            playlistName.setText(playlist.name)

            playlistName.mousePressEvent = self.show_playlist_songs(playlist.id)
            playlistImage.mousePressEvent = self.show_playlist_songs(playlist.id)
            playlistName.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            playlistName.customContextMenuRequested.connect(lambda event, playlist_id=playlist.id: self.show_context_menu(event, playlist_id))

            self.gridLayout.addWidget(groupBox, i // 3, i % 3)

        self.scrollAreaWidgetContents.update()



    def show_add_music_dialog(self):
        self.add_song_dialog = AddSongDialog()
        self.add_song_dialog.added_song.connect(self.reload_interface)
        self.add_song_dialog.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Playlist Collection"))
    
    def center_window(self, window=None):
        if window is None:
            window = self.main_window
        screen_size = QtWidgets.QDesktopWidget().screenGeometry(-1)
        window_size = window.frameGeometry()
        left = (screen_size.width() - window_size.width()) // 2
        top = (screen_size.height() - window_size.height()) // 15
        window.move(left, top)   

    def delete_song_from_playlist(self, playlist_id, song_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM playlist_song WHERE playlist_id = %s AND song_id = %s", (playlist_id, song_id))
        self.connection.commit()
        cursor.close()

class AddPlaylistForm(QtWidgets.QDialog):
    playlist_added = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(AddPlaylistForm, self).__init__(parent)
        self.setWindowTitle("Add Playlist")
        layout = QtWidgets.QVBoxLayout()

        self.playlist_name_input = QtWidgets.QLineEdit()
        self.playlist_image_input = QtWidgets.QLineEdit()

        self.browse_button = QtWidgets.QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_image)  

        layout.addWidget(QtWidgets.QLabel("Playlist Name:"))
        layout.addWidget(self.playlist_name_input)
        layout.addWidget(QtWidgets.QLabel("Image URL or Path:"))
        layout.addWidget(self.playlist_image_input)

        # Thêm QLabel để hiển thị hình ảnh
        self.image_label = QtWidgets.QLabel()
        layout.addWidget(self.image_label)

        layout.addWidget(self.browse_button)

        self.add_button = QtWidgets.QPushButton("Add")
        self.add_button.clicked.connect(self.add_playlist)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def browse_image(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
        file_dialog.setViewMode(QtWidgets.QFileDialog.Detail)
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            self.playlist_image_input.setText(file_path)
            # Cập nhật hình ảnh trên QLabel khi chọn tập tin
            pixmap = QtGui.QPixmap(file_path)
            self.image_label.setPixmap(pixmap.scaledToWidth(200))  # Chỉnh kích thước hình ảnh để nó vừa với QLabel

    def add_playlist(self):
        playlist_name = self.playlist_name_input.text()
        playlist_image_url = self.playlist_image_input.text()
        if playlist_name:
            playlist_dao = PlaylistDAO()
            playlist_dao.add_playlist(playlist_name, playlist_image_url)
            QtWidgets.QMessageBox.information(self, "Success", "Playlist added successfully.")
            self.playlist_added.emit()
            self.accept()
            if isinstance(self.parent(), Ui_PlaylistCollectionWindow):
                self.parent().reload_interface()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please enter a playlist name.")





class AddSongDialog(QtWidgets.QDialog):
    added_song = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(AddSongDialog, self).__init__(parent)
        self.setWindowTitle("Add Song to Playlist")
        layout = QtWidgets.QVBoxLayout()

        self.song_combobox = QtWidgets.QComboBox()
        self.load_songs()
        layout.addWidget(QtWidgets.QLabel("Select Song:"))
        layout.addWidget(self.song_combobox)

        self.playlist_combobox = QtWidgets.QComboBox()
        self.load_playlists()
        layout.addWidget(QtWidgets.QLabel("Select Playlist:"))
        layout.addWidget(self.playlist_combobox)

        self.add_button = QtWidgets.QPushButton("Add")
        self.add_button.clicked.connect(self.add_song_to_playlist)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def load_songs(self):
        songDAO = SongDao()
        songs = songDAO.SelectList()
        for song in songs:
            self.song_combobox.addItem(song.name, song.id)

    def load_playlists(self):
        playlistDAO = PlaylistDAO()
        playlists = playlistDAO.get_all_playlists()
        for playlist in playlists:
            self.playlist_combobox.addItem(playlist.name, playlist.id)

    def add_song_to_playlist(self):
        selected_song_id = self.song_combobox.currentData()
        selected_playlist_id = self.playlist_combobox.currentData()
        if selected_song_id and selected_playlist_id:
            playlistDAO = PlaylistDAO()
            # Kiểm tra xem bài hát đã tồn tại trong playlist chưa
            if playlistDAO.check_song_in_playlist(selected_playlist_id, selected_song_id):
                QtWidgets.QMessageBox.warning(self, "Error", "This song already exists in the playlist.")
            else:
                # Nếu bài hát chưa tồn tại trong playlist, thêm vào
                playlistDAO.add_song_to_playlist(selected_playlist_id, selected_song_id)
                QtWidgets.QMessageBox.information(self, "Success", "Added song to playlist successfully!")
                self.accept()
                self.added_song.emit()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Please select both song and playlist.")


class EditPlaylistForm(QtWidgets.QDialog):
    playlist_edited = QtCore.pyqtSignal()

    def __init__(self, parent=None, playlist=None, playlistDAO=None):
        super(EditPlaylistForm, self).__init__(parent)
        self.setWindowTitle("Edit Playlist")
        self.playlist = playlist
        self.playlistDAO = playlistDAO  # Lưu trữ playlistDAO

        layout = QtWidgets.QVBoxLayout()

        self.playlist_name_input = QtWidgets.QLineEdit()
        self.playlist_name_input.setText(playlist.name)
        layout.addWidget(QtWidgets.QLabel("Playlist Name:"))
        layout.addWidget(self.playlist_name_input)

        self.edit_button = QtWidgets.QPushButton("Edit")
        self.edit_button.clicked.connect(self.edit_playlist)
        layout.addWidget(self.edit_button)

        self.setLayout(layout)

    def edit_playlist(self):
        if self.playlistDAO:  # Kiểm tra xem playlistDAO có giá trị None hay không
            new_name = self.playlist_name_input.text()
            if new_name:
                self.playlistDAO.update_playlist(self.playlist.id, new_name)
                QtWidgets.QMessageBox.information(self, "Success", "Playlist updated successfully.")
                self.playlist_edited.emit()
                self.accept()
            else:
                QtWidgets.QMessageBox.warning(self, "Warning", "Please enter a playlist name.")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Playlist DAO is not available.")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_PlaylistCollectionWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    try:
        sys.exit(app.exec_())
    except Exception as e:
        traceback.print_exc()
