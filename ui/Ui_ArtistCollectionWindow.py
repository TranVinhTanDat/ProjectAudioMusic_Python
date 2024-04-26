import sys
sys.path.append('C:/Users/Admin/Downloads/ProjectAudio_Report/ProjectPythonAudio')
from PyQt5 import QtCore, QtGui, QtWidgets
from dao.SingerDAO import SingerDao
from loadImageFromUrl import loadImageFromUrl
from Ui_ArtistSongCollectionWindow import Ui_ArtistSongCollectionWindow
from unity.main_list_music import *
class Ui_ArtistCollectionWindow(object):
    def setupUi(self, MainWindow):
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

        # Get list of artists from the database
        singer_dao = SingerDao()
        artists = singer_dao.SelectList()

        # Creating artist cards dynamically based on the list of artists
        for i, artist in enumerate(artists):
            groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
            groupBox.setObjectName(f"groupBox_{i+1}")
            groupBox.setMinimumSize(QtCore.QSize(171, 201))
            groupBox.setMaximumSize(QtCore.QSize(171, 201))

            artistImage = QtWidgets.QLabel(groupBox)
            artistImage.setGeometry(QtCore.QRect(4, 20, 161, 111))
            artistImage.setText("")
            pixmap = None
            if artist.image:  
                pixmap = self.load_image(artist.image)  # Load image here
            else:
                pixmap = QtGui.QPixmap("image/tai_nghe.jpg")
            artistImage.setPixmap(pixmap)
            artistImage.setScaledContents(True)
            artistImage.setObjectName(f"artistImage_{i+1}")

            artistName = QtWidgets.QLabel(groupBox)
            artistName.setGeometry(QtCore.QRect(10, 130, 151, 31))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            artistName.setFont(font)
            artistName.setObjectName(f"artistName_{i+1}")
            artistName.setText(artist.name)

            artistImage.mousePressEvent = self.show_artist_songs(artist.id)
            artistName.mousePressEvent = self.show_artist_songs(artist.id)

            self.gridLayout.addWidget(groupBox, i // 3, i % 3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(500, 30, 120, 40))  # Tăng chiều rộng và chiều cao
        self.btnBack.setObjectName("btnBack")
        self.btnBack.setText("⬅️ Back")  # Thêm icon và văn bản cho nút
        self.btnBack.clicked.connect(lambda: self.go_back(MainWindow))


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def load_image(self, image_path):  
        if image_path.startswith("http"):  
            return loadImageFromUrl(image_path)
        else:
            return QtGui.QPixmap(image_path)

    def show_artist_songs(self, artist_id):
        def on_click(event):
            self.artistSongCollectionWindow = QtWidgets.QMainWindow()
            self.artistSongCollectionUI = Ui_ArtistSongCollectionWindow()

            singer_dao = SingerDao()
            songs = singer_dao.getSongsByArtist(artist_id)

            self.artistSongCollectionUI.setupUi(self.artistSongCollectionWindow, songs)
            self.artistSongCollectionWindow.show()
            self.center_window(self.artistSongCollectionWindow)  # Di chuyển cửa sổ vào giữa màn hình
        return on_click
    
    def go_back(self, MainWindow):
        MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Artist Collection"))
        for i in range(9):
            groupBox = self.scrollAreaWidgetContents.findChild(QtWidgets.QGroupBox, f"groupBox_{i+1}")
            if groupBox:  
                groupBox.setTitle(_translate("MainWindow", f"Artist {i+1}"))

    def center_window(self, window=None):
        if window is None:
            window = MainWindow
        # Lấy kích thước màn hình
        screen_size = QtWidgets.QDesktopWidget().screenGeometry(-1)
        # Lấy kích thước của cửa sổ
        window_size = window.frameGeometry()
        # Tính toán vị trí trung tâm cho cửa sổ
        left = (screen_size.width() - window_size.width()) // 2
        top = (screen_size.height() - window_size.height()) // 15
        # Di chuyển cửa sổ vào vị trí trung tâm
        window.move(left, top)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ArtistCollectionWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
