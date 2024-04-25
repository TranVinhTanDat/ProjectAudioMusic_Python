from PyQt5.QtWidgets import QWidget, QListWidget, QVBoxLayout, QListWidgetItem, QMainWindow

class AlbumWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.albums = []  # Danh sách album

        # Tạo giao diện cho danh sách album
        self.album_list_widget = QListWidget(self)
        self.album_list_widget.itemClicked.connect(self.album_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.album_list_widget)
        self.setLayout(layout)

    def load_albums(self, albums):
        self.albums = albums
        # Xóa danh sách album cũ
        self.album_list_widget.clear()
        # Thêm các thẻ item album vào danh sách
        for album in albums:
            item = QListWidgetItem(album.name)
            self.album_list_widget.addItem(item)

    def album_clicked(self, item):
        # Xử lý sự kiện khi người dùng chọn một album
        index = self.album_list_widget.row(item)
        selected_album = self.albums[index]
        # Gọi hàm để hiển thị danh sách các bài hát trong album này
        self.show_songs_of_album(selected_album)

    def show_songs_of_album(self, album):
        # Hiển thị danh sách các bài hát trong album
        pass  # Bạn cần triển khai hàm này để hiển thị danh sách bài hát trong album

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.album_widget = AlbumWidget(self)
        self.setCentralWidget(self.album_widget)
        # Load danh sách album khi khởi động ứng dụng
        self.load_albums()

    def load_albums(self):
        # Load danh sách album từ cơ sở dữ liệu hoặc nơi khác
        albums = []  # Thay bằng mã để load danh sách album
        self.album_widget.load_albums(albums)
