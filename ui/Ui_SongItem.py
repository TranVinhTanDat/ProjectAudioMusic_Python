# import sys
# from loadImageFromUrl import loadImageFromUrl
# from PyQt5 import QtCore, QtGui, QtWidgets
# from dao.AlbumDAO import AlbumDAO

# class Ui_SongItem(object):
#     def setupUi(self, SongItem, song):
#         SongItem.setObjectName("SongItem")
#         SongItem.resize(161, 201)
#         self.groupBox = QtWidgets.QGroupBox(SongItem)
#         self.groupBox.setGeometry(QtCore.QRect(0, 0, 161, 201))
#         self.groupBox.setObjectName("groupBox")
#         self.songImage = QtWidgets.QLabel(self.groupBox)
#         self.songImage.setGeometry(QtCore.QRect(4, 20, 151, 111))
#         self.songImage.setText("")
#         pixmap = QtGui.QPixmap(song.image) if song.image else QtGui.QPixmap("image/tai_nghe.jpg")
#         self.songImage.setPixmap(pixmap)
#         self.songImage.setScaledContents(True)
#         self.songImage.setObjectName("songImage")
#         self.songName = QtWidgets.QLabel(self.groupBox)
#         self.songName.setGeometry(QtCore.QRect(10, 130, 141, 31))
#         font = QtGui.QFont()
#         font.setBold(True)
#         font.setWeight(75)
#         self.songName.setFont(font)
#         self.songName.setObjectName("songName")
#         self.songName.setText(song.name)
#         self.songInfo = QtWidgets.QLabel(self.groupBox)
#         self.songInfo.setGeometry(QtCore.QRect(10, 160, 141, 31))
#         self.songInfo.setObjectName("songInfo")
#         self.songInfo.setText("Additional Info")

#         QtCore.QMetaObject.connectSlotsByName(SongItem)

#     def retranslateUi(self, SongItem):
#         _translate = QtCore.QCoreApplication.translate
#         SongItem.setWindowTitle(_translate("SongItem", "Song Item"))


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     AlbumCollectionWindow = QtWidgets.QMainWindow()
#     ui = Ui_AlbumCollectionWindow()
#     album_dao = AlbumDAO()
#     albums = album_dao.get_all_albums()  
#     ui.setupUi(AlbumCollectionWindow, albums)
#     AlbumCollectionWindow.show()
#     sys.exit(app.exec_())