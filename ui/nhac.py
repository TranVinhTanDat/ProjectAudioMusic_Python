from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QPainterPath, QPixmap, QTransform
from PyQt5.QtCore import Qt  # Đảm bảo import Qt để dùng Qt.Horizontal
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(641, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 60, 241, 241))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 440, 621, 571))
        self.widget.setObjectName("widget")

        self.ngau_nhien = QtWidgets.QPushButton(self.widget)
        self.ngau_nhien.setGeometry(QtCore.QRect(10, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.ngau_nhien.setFont(font)
        self.ngau_nhien.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/random.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ngau_nhien.setIcon(icon)
        self.ngau_nhien.setIconSize(QtCore.QSize(35, 35))
        self.ngau_nhien.setObjectName("ngau_nhien")
        self.lap_lai = QtWidgets.QPushButton(self.widget)
        self.lap_lai.setGeometry(QtCore.QRect(260, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lap_lai.setFont(font)
        self.lap_lai.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/repeat.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lap_lai.setIcon(icon1)
        self.lap_lai.setIconSize(QtCore.QSize(32, 32))
        self.lap_lai.setObjectName("lap_lai")
        
        self.volume = QtWidgets.QSlider(self.widget)
        self.volume.setGeometry(QtCore.QRect(420, 20, 191, 22))
        self.volume.setProperty("value", 50)
        self.volume.setOrientation(QtCore.Qt.Horizontal)
        self.volume.setObjectName("volume")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(350, 10, 20, 41))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.loa_active = QtWidgets.QPushButton(self.widget)
        self.loa_active.setGeometry(QtCore.QRect(380, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.loa_active.setFont(font)
        self.loa_active.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/audio.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loa_active.setIcon(icon2)
        self.loa_active.setIconSize(QtCore.QSize(35, 35))
        self.loa_active.setCheckable(False)
        self.loa_active.setObjectName("loa_active")

        self.lui_bai = QtWidgets.QPushButton(self.widget)
        self.lui_bai.setGeometry(QtCore.QRect(60, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lui_bai.setFont(font)
        self.lui_bai.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/back.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lui_bai.setIcon(icon3)
        self.lui_bai.setIconSize(QtCore.QSize(32, 32))
        self.lui_bai.setObjectName("lui_bai")
        self.phat = QtWidgets.QPushButton(self.widget)
        self.phat.setGeometry(QtCore.QRect(110, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.phat.setFont(font)
        self.phat.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/play-button.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.phat.setIcon(icon4)
        self.phat.setIconSize(QtCore.QSize(32, 32))
        self.phat.setObjectName("phat")
        self.tam_dung = QtWidgets.QToolButton(self.widget)
        self.tam_dung.setGeometry(QtCore.QRect(160, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.tam_dung.setFont(font)
        self.tam_dung.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("image/stop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tam_dung.setIcon(icon5)
        self.tam_dung.setIconSize(QtCore.QSize(32, 32))
        self.tam_dung.setObjectName("tam_dung")
        self.chuyen_bai = QtWidgets.QPushButton(self.widget)
        self.chuyen_bai.setGeometry(QtCore.QRect(210, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.chuyen_bai.setFont(font)
        self.chuyen_bai.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("image/next.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chuyen_bai.setIcon(icon6)
        self.chuyen_bai.setIconSize(QtCore.QSize(32, 32))
        self.chuyen_bai.setObjectName("chuyen_bai")
        self.icon = QtWidgets.QPushButton(self.widget)
        self.icon.setEnabled(False)
        self.icon.setGeometry(QtCore.QRect(240, 60, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.icon.setFont(font)
        self.icon.setMouseTracking(False)
        self.icon.setTabletTracking(False)
        self.icon.setAcceptDrops(False)
        self.icon.setAutoFillBackground(False)
        self.icon.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("image/tim_kiem.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon.setIcon(icon7)
        self.icon.setIconSize(QtCore.QSize(18, 26))
        self.icon.setCheckable(False)
        self.icon.setAutoRepeat(False)
        self.icon.setAutoExclusive(False)
        self.icon.setAutoDefault(False)
        self.icon.setDefault(False)
        self.icon.setFlat(False)
        self.icon.setObjectName("icon")
        self.table_list = QtWidgets.QTableWidget(self.widget)
        self.table_list.setGeometry(QtCore.QRect(0, 100, 622, 261))
        self.table_list.setObjectName("table_list")
        self.table_list.setColumnCount(0)
        self.table_list.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(10, 60, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.select = QtWidgets.QComboBox(self.widget)
        self.select.setGeometry(QtCore.QRect(280, 60, 91, 31))
        self.select.setObjectName("select")
        self.dung_lai = QtWidgets.QPushButton(self.widget)
        self.dung_lai.setGeometry(QtCore.QRect(310, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.dung_lai.setFont(font)
        self.dung_lai.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("image/ket_thuc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dung_lai.setIcon(icon8)
        self.dung_lai.setIconSize(QtCore.QSize(32, 32))
        self.dung_lai.setObjectName("dung_lai")
        self.tim_kiem = QtWidgets.QLineEdit(self.widget)
        self.tim_kiem.setGeometry(QtCore.QRect(110, 60, 161, 31))
        self.tim_kiem.setObjectName("tim_kiem")
        self.ngau_nhien.raise_()
        self.lap_lai.raise_()
        self.volume.raise_()
        self.line.raise_()
        self.loa_active.raise_()
        self.lui_bai.raise_()
        self.phat.raise_()
        self.tam_dung.raise_()
        self.chuyen_bai.raise_()
        self.table_list.raise_()
        self.pushButton.raise_()
        self.select.raise_()
        self.dung_lai.raise_()
        self.tim_kiem.raise_()
        self.icon.raise_()

# Không đổi tên widget_2
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 380, 621, 51))
        self.widget_2.setObjectName("widget_2")

        # Sử dụng QSlider cho thanh trượt
        self.noi_dung_mp3 = QtWidgets.QSlider(Qt.Horizontal, self.widget_2)  # Không đổi tên
        self.noi_dung_mp3.setGeometry(QtCore.QRect(60, 10, 551, 31))  # Vị trí và kích thước
        self.noi_dung_mp3.setMinimum(0)  # Giá trị nhỏ nhất
        self.noi_dung_mp3.setMaximum(100)  # Giá trị lớn nhất
        self.noi_dung_mp3.setValue(10)  # Giá trị mặc định để trùng với hình ảnh
        self.noi_dung_mp3.setOrientation(Qt.Horizontal)  # Thanh trượt ngang

        # Cài đặt CSS để tạo thanh trượt giống như trong hình
        self.noi_dung_mp3.setStyleSheet("""
            QSlider::groove:horizontal {
                background: #404040;  # Màu xám như trong hình
                height: 8px;
                border-radius: 4px;
            }
            QSlider::sub-page:horizontal {
                background: #00ff00;  # Màu xanh lá cây
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: white;  # Màu trắng như trong hình
                border-radius: 50%;
                width: 12px;
                height: 12px;
            }
        """)

        # Nhãn thời gian
        self.time_label = QtWidgets.QLabel(self.widget_2)
        self.time_label.setGeometry(QtCore.QRect(10, 20, 41, 16))  # Vị trí nhãn
        self.time_label.setObjectName("time_label")  # Không đổi tên
        
        self.ten_bai_hat = QtWidgets.QLabel(self.centralwidget)
        self.ten_bai_hat.setGeometry(QtCore.QRect(90, 330, 400, 41))  # Adjusted width for centering
        self.ten_bai_hat.setAlignment(QtCore.Qt.AlignCenter)  # Align text to the center horizontally
        self.ten_bai_hat.setObjectName("ten_bai_hat")
        font = QtGui.QFont()
        font.setPointSize(14)  # Increase font size
        font.setBold(True)  # Make text bold
        self.ten_bai_hat.setFont(font)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 100, 40))  # Thay đổi kích thước và chỉnh sửa vị trí nếu cần
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setFixedWidth(100)  # Đặt chiều rộng mới
        self.pushButton_2.setFixedHeight(40)  # Đặt chiều cao mới

        self.thu_vien = QtWidgets.QPushButton(self.centralwidget)
        self.thu_vien.setGeometry(QtCore.QRect(100, 0, 110, 40))  # Thay đổi kích thước và chỉnh sửa vị trí nếu cần
        self.thu_vien.setObjectName("thu_vien")
        self.thu_vien.setFixedWidth(110)  # Đặt chiều rộng mới
        self.thu_vien.setFixedHeight(40)  # Đặt chiều cao mới

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 26))

        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        # Đảm bảo khởi tạo các thuộc tính trước khi sử dụng
        self.rotationAngle = 0  # Khởi tạo góc xoay
        self.rotateTimer = QTimer()  # Tạo timer cho việc xoay hình ảnh
        self.rotateTimer.timeout.connect(self.rotateImage)
        self.rotateTimer.start(20)  # Xoay hình ảnh mỗi 100 ms

        self.setCircularImage("image/guitar.jpg")  # Nên đặt sau các khởi tạo thuộc tính liên quan
        self.rotateTimer = QTimer()
        self.rotateTimer.timeout.connect(self.rotateImage)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setCircularImage(self, image_path):
        original_pixmap = QtGui.QPixmap(image_path)  # Load the original pixmap
        circular_pixmap = QtGui.QPixmap(original_pixmap.size())  # Create a new pixmap with the original size
        circular_pixmap.fill(QtCore.Qt.transparent)  # Set a transparent background for the pixmap
        painter = QtGui.QPainter(circular_pixmap)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        path = QtGui.QPainterPath()
        path.addEllipse(0, 0, original_pixmap.width(), original_pixmap.height())  # Draw an ellipse with the original size
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, original_pixmap)  # Draw the original image onto the circular pixmap
        painter.end()
        self.circular_pixmap = circular_pixmap  # Save the circular pixmap for rotation
        self.updatePixmap()  # Update the pixmap when initializing

    def updatePixmap(self):
        transformed_pixmap = self.circular_pixmap.transformed(QTransform().rotate(self.rotationAngle))
        self.label.setPixmap(transformed_pixmap)  # Set the transformed pixmap directly to the label
    def stopRotation(self):
        self.rotateTimer.stop()  # Dừng QTimer để ngừng xoay
        self.rotationAngle = 0  # Đặt góc xoay về 0
        self.updatePixmap()  # Cập nhật hình ảnh để hiển thị góc xoay mới


    def rotateImage(self):
        self.rotationAngle += 2  # Tăng góc xoay
        if self.rotationAngle >= 360:
            self.rotationAngle = 0
        self.updatePixmap()  # Cập nhật pixmap trên label

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Chọn file"))
        self.time_label.setText(_translate("MainWindow", "00:00"))
        self.ten_bai_hat.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "🏠 Trang chủ"))
        self.thu_vien.setText(_translate("MainWindow", "📚 Thư viện"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
