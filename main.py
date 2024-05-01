import sys
sys.path.append('C:/Users/Admin/Downloads/ProjectAudio_Report/ProjectPythonAudio/dao')
from dao.TypeDAO import TypeDao
from dao.SongDAO import SongDao
from dao.SingerDAO import SingerDao
from unity.main_list_music import Main_List_Music_MainWindow
import random
import threading as th 
import pygame
import time  
import ffmpeg
import tkinter
import re
from tkinter import filedialog
from mutagen.mp3 import MP3
from threading import Timer  
from tkinter import messagebox
import os
import requests
from io import BytesIO
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QPushButton, QDesktopWidget, QLabel
from ui.nhac import Ui_MainWindow
from object.music import Music
from dao.SongDAO import SongDao
from controller.MusicController import MusicController
from unity.volume import *
from loadImageFromUrl import loadImageFromUrl
from PyQt5.QtCore import QPropertyAnimation, QRect
from database.db import connect

from mutagen.id3 import ID3, APIC
from PIL import Image
from io import BytesIO

class RepeatTimer(Timer):  
    def run(self):  
        while not self.finished.wait(self.interval):  
            self.function(*self.args,**self.kwargs)  
class MainWindow(QMainWindow):
    
    
    list = []
    
    songDao = SongDao()
    controller = MusicController()
    __playMusic=False
    index = 0
    timer = ""
    callBackMusic = False
    ran = False
    volumn = True
    valueVolumn = 50
    valueVolumnOld = 50
    cellSelect = -1
    currentTime = 0
    listTemp = []
    def check_database_connection(self):
        try:
            cursor = connect()
            cursor.execute("SELECT * FROM singer")
            rows = cursor.fetchall()
            print("Kết nối cơ sở dữ liệu thành công")
            return True
        except Exception as e:
            print("Lỗi kết nối đến cơ sở dữ liệu:", e)
            return False

   
    def __init__(self):
        super().__init__()
        self.uic= Ui_MainWindow()
        pygame.init()
        self.uic.setupUi(self)
        self.songDao = SongDao()  # Tạo đối tượng songDao từ lớp SongDao

        self.center_window()

        self.uic.phat.clicked.connect(self.show_music)
        self.uic.dung_lai.clicked.connect(self.stopMusic)
        self.uic.tam_dung.clicked.connect(self.pause_music)
        self.uic.lui_bai.clicked.connect(self.prevMusic)
        self.uic.lap_lai.clicked.connect(self.callBackMus)
        self.uic.chuyen_bai.clicked.connect(self.nextMusic)
        self.uic.ngau_nhien.clicked.connect(self.randomMusic)
        self.uic.loa_active.clicked.connect(self.setVolumn)
        self.uic.table_list.cellClicked.connect(self.setCellClick)
        self.uic.tim_kiem.textChanged.connect(self.searchText)
        self.uic.volume.setValue(self.valueVolumn)
        self.uic.volume.valueChanged.connect(self.setValueVolumn)
        self.list = self.songDao.SelectList()
        self.listTemp = self.createListTeam()
        self.timer = RepeatTimer(1,self.display) 
        self.uic.pushButton.clicked.connect(self.addMusicToFile)
        self.selectListType()
        self.uic.select.currentTextChanged.connect(self.on_combobox_changed)
        self.uic.thu_vien.clicked.connect(self.show_list_music)
        self.uic.noi_dung_mp3.setMinimum(0)
        self.uic.noi_dung_mp3.setMaximum(300)
        self.uic.noi_dung_mp3.setValue(0)
        self.add_guest()
        # #QMediaPlayer
        # self.mediaPlayer = QMediaPlayer(None,QMediaPlayer.VideoSurface)
        # self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('kk.mp3')))

        # #set Widget
        # self.videoWidget=QVideoWidget()
        # self.uic.verticalLayout.addWidget(self.videoWidget)
        # self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.uic.noi_dung_mp3.valueChanged.connect(self.setCurrentTime)
        



    def createListTeam(self):
        result = []
        for value in self.list:
            result.append(value)
        return result
    def setCellClick(self,row,col):
        self.index = self.findIndexSong(row)
        self.playMusic()
        self.restartTimer()
        
    #thêm bài hát từ file
    # def addMusicToFile(self):    
    #     root =  tkinter.Tk()
    #     root.withdraw() #use to hide tkinter window 
    #     currdir = "/"
    #     root.sourceFile = filedialog.askopenfilename(parent=root, initialdir= currdir, title='Please select a directory')
    #     if len(root.sourceFile) > 0:
    #         link = root.sourceFile
    #         name = os.path.basename(root.sourceFile)
    #         name = name[:-4]
    #         self.controller.addMusic(link,name)
    #         self.list = self.controller.listSong()
    #         self.listTemp = self.createListTeam()
    #         self.add_guest()
        
    #chuyên trang
    # Chuyển trang
    # Trong hàm show_list_music của main.py
    def show_list_music(self):
        from unity.main_list_music import Main_List_Music_MainWindow
        self.timer.cancel()
        # Khởi tạo QStackedWidget
        self.stacked_widget = QStackedWidget(self)
        
        # Tạo hai trang con cho QStackedWidget
        self.main_widget = MainWindow()
        # self.main_widget.setObjectName("MainWidget")
        # self.main_widget.setStyleSheet("#MainWidget { background-color: #000; }")
        self.thu_vien = QPushButton("Thu vien!!!", self.main_widget)
        self.thu_vien.setGeometry(50, 50, 250, 50)
        
        # Truyền danh sách bài hát self.list vào Main_List_Music_MainWindow
        self.list_music_widget = Main_List_Music_MainWindow(self.list)  # Truyền danh sách bài hát vào đây
        self.list_music_widget.index = self.index
        self.list_music_widget.currentTime = self.currentTime
        self.list_music_widget.volumn = self.uic.volume.value() 
        self.stacked_widget.addWidget(self.main_widget)
        self.stacked_widget.addWidget(self.list_music_widget)
        
        self.setCentralWidget(self.stacked_widget)
        self.stacked_widget.setCurrentWidget(self.list_music_widget)  


    def createListTeam(self):
        result = []
        for value in self.list:
            result.append(value)
        return result
    
    def setCellClick(self, row, col):
        self.index = self.findIndexSong(row)
        self.playMusic()
        self.restartTimer()
        
    # Thêm bài hát từ file

    # def rotateImage(self):
    #     self.rotationAngle += 2  # Tăng góc xoay
    #     if self.rotationAngle >= 360:
    #         self.rotationAngle = 0
    #     self.updatePixmap()  # Cập nhật pixmap trên label

    def addMusicToFile(self):
        root = tkinter.Tk()
        root.withdraw()
        currdir = "/"
        root.sourceFile = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select an audio file')
        
        if len(root.sourceFile) > 0:
            link = root.sourceFile
            audio = MP3(link, ID3=ID3) 
            
            name_music = audio.tags.get('TIT2', 'Unknown')
            artist_music = audio.tags.get('TPE1', 'Unknown')
            
            if isinstance(artist_music, list):
                artist_music = ", ".join(artist_music)
            else:
                artist_music = str(artist_music)

            artist_music = re.sub(r'[",]', '', artist_music)

            artist_id = self.controller.getSingerIdByName(artist_music)
            if artist_id is None:
                artist_id = self.controller.addSinger(artist_music)

            image_path = None
            image_data = audio.tags.get('APIC:', None)
            if image_data:
                image_path = "image_" + os.path.basename(link) + ".jpg"  
                with open(image_path, 'wb') as img_file:
                    img_file.write(image_data.data)  
            if not image_path:
                image_path = 'https://i.scdn.co/image/ab67706f0000000281722192322800ae99c2ed06'
            
            type_name = "Pop"
            
            self.controller.addMusic(link, name_music, artist_id, image_path, type_name)

            self.list = self.controller.listSong()
            self.listTemp = self.createListTeam()
            self.add_guest()

    # Chuyển trang
    # def show_list_music(self):
    #     # Tạo một cửa sổ mới của lớp Main_List_Music_MainWindow
    #     self.list_music_window = Main_List_Music_MainWindow(self.list)
    #     self.list_music_window.show()
 
    
    # Tìm kiếm

    def searchText(self):
        text = self.uic.tim_kiem.text().lower().strip()
        if text:
            # Gọi hàm searchByName từ đối tượng songDao và truyền connection vào
            self.listTemp = self.songDao.searchByName(text, self.songDao.connection)
            self.refresh_song_list()
        else:
            self.reset_song_list()

    def refresh_song_list(self):
        self.uic.table_list.clear()
        self.add_guest()  # Add songs to the UI from self.listTemp

    # Reset song list to all songs
    def reset_song_list(self):
        self.listTemp = self.createListTeam()
        self.refresh_song_list()



    # Tua nhạc
    def setCurrentTime(self):
        value = int(self.uic.noi_dung_mp3.value())
        if value > int(self.currentTime) or value < int(self.currentTime):
            if self.currentTime != 0 :
                if self.__playMusic != False:
                    pygame.mixer.music.play(0, value)
                    self.uic.noi_dung_mp3.setValue(value)
                    self.currentTime = value
                    self.restartTimer()

    # Đặt giá trị âm lượng
    def setValueVolumn(self):
        self.valueVolumn = self.uic.volume.value()
        set_master_volume(self.valueVolumn)
    
    # Âm lượng 
    def setVolumn(self):
        if self.volumn == True:
            self.valueVolumnOld = self.valueVolumn
            self.uic.volume.setValue(0)
            self.volumn = False
        else:
            self.volumn = True
            self.uic.volume.setValue(self.valueVolumnOld)
    
    # Bật/Tắt ngẫu nhiên
    def randomMusic(self):
        if self.ran == False:
            self.ran = True
        else:
             self.ran = False
    
    # Bật/Tắt lặp lại
    def callBackMus(self):
        if self.callBackMusic == False:
            self.callBackMusic = True
        else:
             self.callBackMusic = False
             
    # Dừng nhạc
    def stopMusic(self):
        pygame.mixer.music.stop()
        self.uic.stopRotation() 
        self.__playMusic = False
        self.currentTime = 0
        self.timer.center

    # Phát nhạc theo ID
    def playMusicToID(self, id):
        index = self.findIndexSongToID(id)
        self.index = index
        self.playMusic()
        self.restartTimer()
    
    def rotateImage(self):
        self.rotationAngle += 2
        if self.rotationAngle >= 360:
            self.rotationAngle = 0
        self.updatePixmap()  
    # Hàng đợi nhạc
    def queuMusic(self):
        for value in self.list:
            pygame.mixer.music.queue(value.link)
    
    # Hiển thị thời gian
    def tong_thoi_gian_bai_hat(danh_sach_thoi_gian):
        tong = 0
        for thoi_gian in danh_sach_thoi_gian:
            phut, giay = thoi_gian.split(":")
            tong += int(phut) * 60 + int(giay)
        return tong   
    
    def display(self):
        self.currentTime = self.currentTime + 1
        mi = int(self.currentTime/60)
        if mi < 10:
            mi = "0" + str(mi)
        second = int(self.currentTime%60)
        if second < 10:
            second = "0" + str(second)
        self.uic.time_label.setText( "{}:{}".format(mi, second))
        self.uic.noi_dung_mp3.setValue(int(mi)*60+int(second))
        if int(self.currentTime) >= self.duration(self.list[self.index].file_path)-5:
            self.uic.noi_dung_mp3.setValue(0)
            self.uic.time_label.setText( "{}:{}".format("00", "00"))
            cel = self.findIndexSongTable(self.index)
            self.uic.table_list.selectRow(cel)
            self.nextMusic()
            self.restartTimer()


    # Lùi bài hát
    def prevMusic(self):
        if self.callBackMusic == True:
            self.index = self.index
        elif self.ran == True:
            self.index = self.random()
        elif self.index > 0:
            self.index -= 1   
        else:
            self.index = len(self.list)-1
        
        # Chơi nhạc
        self.playMusic()
        self.restartTimer()
    
    def restartTimer(self):
        self.timer.cancel()
        self.timer = RepeatTimer(1, self.display) 
        self.timer.start()
    
    # Chuyển tiếp bài hát
    def nextMusic(self):
        if self.callBackMusic == True:
            self.index = self.index
        elif self.ran == True:
            self.index = self.random()
        elif self.index < len(self.list)-1:
            self.index += 1 
        else:
            self.index = 0
        self.playMusic()
        self.restartTimer()
    
    def showMessageError(self):
        messagebox.showinfo("Error", "Không tìm thấy nguồn bài hát này")
   
    def playMusic(self):
        self.uic.stopRotation()

        if self.timer.is_alive():
            self.timer.cancel()  

        # Khởi tạo lại bộ đếm thời gian
        self.timer = RepeatTimer(1, self.display)  
        self.timer.start()  

        self.currentTime = 0

        music = self.list[self.index]
        file_path = music.file_path

        if os.path.isfile(file_path):
            maxTime = self.duration(file_path) - 5
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            self.uic.ten_bai_hat.setText(music.name)

            if music.image:
                if music.image.startswith("http://") or music.image.startswith("https://"):
                    pixmap = loadImageFromUrl(music.image)
                else:
                    pixmap = QtGui.QPixmap(music.image)
                self.uic.setCircularImage(pixmap)
            else:
                self.uic.setCircularImage("./image/MUSIC.jpg")

            # Chọn hàng trong bảng liên quan đến bài hát đang phát
            cel = self.findIndexSongTable(self.index)
            if cel != -1:
                self.uic.table_list.selectRow(cel)
                self.uic.noi_dung_mp3.setMaximum(maxTime)

            self.uic.rotateTimer.start(20)

        else:
            self.showMessageError() 





    def random(self):
        return random.randint(0, len(self.list)-2)
    
    def pause_music(self):
        pygame.mixer.music.pause()
        self.uic.stopRotation()

        if self.timer.is_alive(): 
            self.timer.cancel()


    
    def findIndexSong(self, row):
        song = self.listTemp[row]
        point = 0
        for value in self.list:
            if song.id == value.id:
                return point
            point = point + 1
        return -1
    
    def findIndexSongToID(self, id):
        point = 0
        for value in self.list:
            if id == value.id:
                return point
            point = point + 1
    
    def findIndexSongTable(self, index):
        song = self.list[index]
        point = 0
        for value in self.listTemp:
            if song.id == value.id:
                return point
            point = point + 1
        return -1
    
    def show_music(self):
        if not self.__playMusic:
            self.playMusic()
            self.__playMusic = True
            self.uic.rotateTimer.start(20)
            
            if not self.timer.is_alive():
                self.timer = RepeatTimer(1, self.display)
                self.timer.start()
        else:
            pygame.mixer.music.unpause()
            self.uic.rotateTimer.start(20) 
            
            if not self.timer.is_alive():
                self.timer = RepeatTimer(1, self.display)
                self.timer.start()


    

    def add_guest(self):
            rowPosition = self.uic.table_list.rowCount()
            self.uic.table_list.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
            self.uic.table_list.insertRow(rowPosition)
            label = ["Tên bài hát", "Thể loại", "Ca sĩ"]
            numcols = 3
            numrows = len(self.listTemp)      
            self.uic.table_list.setRowCount(numrows)
            self.uic.table_list.setColumnCount(numcols)  
            self.uic.table_list.setHorizontalHeaderLabels(label)
            header = self.uic.table_list.horizontalHeader()       
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

            index = 0
            for value in self.listTemp:
                # Kiểm tra nếu value là đối tượng Music
                if isinstance(value, Music):
                    name = value.name
                    
                    # Lấy thông tin chi tiết về thể loại từ cơ sở dữ liệu
                    type_obj = TypeDao().selectTypeById(value.idType)
                    type_name = type_obj.name if type_obj else "Unknown"
                    
                    # Lấy thông tin chi tiết về ca sĩ từ cơ sở dữ liệu
                    singer_obj = SingerDao().selectSingerById(value.idSinger)
                    singer_name = singer_obj.name if singer_obj else "Unknown"
                    
                    self.uic.table_list.setItem(index, 0, QtWidgets.QTableWidgetItem(name))
                    self.uic.table_list.setItem(index, 1, QtWidgets.QTableWidgetItem(type_name))
                    self.uic.table_list.setItem(index, 2, QtWidgets.QTableWidgetItem(singer_name))
                    index += 1



    def duration(self, song):
        return int(float((ffmpeg.probe(song)['format']['duration'])))
    def selectListType(self):
            listType = self.controller.listTypeDao()
            self.uic.select.addItem("Tất cả")
            for value in listType:
                self.uic.select.addItem(value.name)
    def on_combobox_changed(self,value):
            
            self.listTemp.clear()
        
            if value != "Tất cả":
                self.listTemp = self.controller.searchListSongType(value)
            else:
                self.listTemp = self.createListTeam()
            self.uic.table_list.clear()
            
            self.add_guest()
    def center_window(self):
        screen_size = QDesktopWidget().screenGeometry(-1)
        window_size = self.frameGeometry()
        left = (screen_size.width() - window_size.width()) // 2
        top = (screen_size.height() - window_size.height()) // 15

        self.move(left, top)


# Kết thúc game
pygame.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.check_database_connection()
    main_win.add_guest()  # Di chuyển dòng này ra khỏi phương thức __init__
    main_win.show()
    sys.exit(app.exec())

