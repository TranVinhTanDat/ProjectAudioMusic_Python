import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QDesktopWidget
from PyQt5.QtGui import QPixmap

from ui.Danh_Sach_Nhac import Ui_MainWindow as Danh_Sach_Nhac_Ui_MainWindow
from ui.Ui_AlbumCollectionWindow import Ui_AlbumCollectionWindow
from ui.Ui_ArtistCollectionWindow import Ui_ArtistCollectionWindow
from ui.Ui_PlaylistCollectionWindow import Ui_PlaylistCollectionWindow
from ui.Ui_DanhSachNhacWindow import Ui_DanhSachNhacWindow

from controller.MusicController import MusicController
from loadImageFromUrl import loadImageFromUrl
from dao.AlbumDAO import AlbumDAO
from dao.SongDAO import SongDao
from object.music import Music


class Main_List_Music_MainWindow(QMainWindow):
    def __init__(self, songs):  
        super().__init__()
        self.uic = Ui_DanhSachNhacWindow()
        self.uic.setupUi(self, songs)
        self.controller = MusicController()
        self.list = songs
        self.getListSong()
        self.center_window()

    def getListSong(self):
        self.list = self.controller.listSong()
        self.uic.setupUi(self, self.list)
        self.connect_buttons()

    def showAlbumCollection(self):
        self.album_collection_window = QMainWindow()
        self.album_collection_ui = Ui_AlbumCollectionWindow()
        album_dao = AlbumDAO()
        albums = album_dao.get_all_albums()
        self.album_collection_ui.setupUi(self.album_collection_window, albums)
        self.center_window(self.album_collection_window)  # Center the new window
        self.album_collection_window.show()

    def showPlaylistCollection(self):
        self.playlist_collection_window = QMainWindow()
        self.playlist_collection_ui = Ui_PlaylistCollectionWindow()
        self.playlist_collection_ui.setupUi(self.playlist_collection_window)
        self.center_window(self.playlist_collection_window)  # Center the new window
        self.playlist_collection_window.show()

    def showArtistCollection(self):
        self.artist_collection_window = QMainWindow()
        self.artist_collection_ui = Ui_ArtistCollectionWindow()
        self.artist_collection_ui.setupUi(self.artist_collection_window)
        self.center_window(self.artist_collection_window)  # Center the new window
        self.artist_collection_window.show()

    def connect_buttons(self):
        self.uic.btnAlbum.clicked.connect(self.showAlbumCollection)
        self.uic.btnSinger.clicked.connect(self.showArtistCollection)
        self.uic.btnPlaylist.clicked.connect(self.showPlaylistCollection)

    def center_window(self, window=None):
        if window is None:
            window = self
        # Get the screen size
        screen_size = QDesktopWidget().screenGeometry(-1)
        # Get the size of the window
        window_size = window.frameGeometry()
        # Calculate the center position for the window
        left = (screen_size.width() - window_size.width()) // 2
        top = (screen_size.height() - window_size.height()) // 15
        # Move the window to the center position
        window.move(left, top)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    song_dao = SongDao()
    songs = song_dao.SelectList()
    main_win = Main_List_Music_MainWindow(songs)
    main_win.show()
    sys.exit(app.exec_())