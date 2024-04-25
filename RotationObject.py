import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtCore import QObject, QPropertyAnimation, QRectF
from PyQt5.QtGui import QPixmap


class RotationObject(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._rotation = 0

    def setRotation(self, rotation):
        self._rotation = rotation

    def rotation(self):
        return self._rotation

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Khởi tạo QGraphicsView và QGraphicsScene cho hình tròn
        self.circle_view = QGraphicsView(self)
        self.circle_scene = QGraphicsScene()
        self.circle_view.setScene(self.circle_scene)
        self.circle_view.setGeometry(10, 10, 200, 200)  # Đặt kích thước và vị trí cho QGraphicsView
        self.circle_scene.setSceneRect(QRectF(self.circle_view.rect()))  # Đặt kích thước cho QGraphicsScene

        # Khởi tạo QGraphicsPixmapItem với hình ảnh mặc định
        self.circle_pixmap_item = QGraphicsPixmapItem(QPixmap("./image/tai_nghe.jpg"))
        self.circle_scene.addItem(self.circle_pixmap_item)

        # Tạo một QObject mới để quản lý thuộc tính rotation
        self.rotation_obj = RotationObject()
        
        # Tạo một QPropertyAnimation cho thuộc tính rotation của QObject
        self.animation = QPropertyAnimation(self.rotation_obj, b"rotation", parent=self)
        self.animation.setDuration(5000)  # Đặt thời gian quay là 5 giây
        self.animation.setStartValue(0)   # Góc ban đầu
        self.animation.setEndValue(360)   # Góc kết thúc
        self.animation.setLoopCount(-1)   # Lặp vô hạn

        # Gắn QGraphicsView cho cửa sổ chính
        self.setCentralWidget(self.circle_view)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
