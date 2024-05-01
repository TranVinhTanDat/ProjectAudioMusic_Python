import mysql.connector
import sys
sys.path.append('C:/Users/Admin/Downloads/ProjectAudio_Report/ProjectPythonAudio/dao')
from TypeDAO import TypeDao
# Thêm import cho các đối tượng Type và Singer từ module music
from object.music import Music, Type, Singer

class SongDao:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='musicplayer'
        )

    def SelectList(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM song")
        result = cursor.fetchall()
        list_music = []
        for row in result:
            music = Music(row[0], row[1], row[2], row[3], row[4], row[5])
            list_music.append(music)
        cursor.close()
        return list_music
    
    def addMusic(self, link, name, idSinger, image_path, type_name):
        cursor = self.connection.cursor()
        
        # Chuyển đổi giá trị name thành chuỗi nếu nó không phải là chuỗi
        if not isinstance(name, str):
            name = str(name)
        
        # Thêm bản ghi mới vào bảng song
        query = "INSERT INTO song (name, file_path, idSinger, image) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, link, idSinger, image_path))
        self.connection.commit()

        # Lấy id của thể loại từ tên thể loại
        type_id = TypeDao().selectTypeIdByName(type_name)
        
        # Kiểm tra xem type_id có giá trị hợp lệ không
        if type_id is not None:
            # Cập nhật idType của bài hát mới nếu type_id hợp lệ
            update_query = "UPDATE song SET idType = %s WHERE name = %s"
            cursor.execute(update_query, (type_id, name))
            self.connection.commit()
        else:
            print("Không tìm thấy thể loại:", type_name)
            
        cursor.close()


    def getTypeIdByName(self, type_name):
            cursor = self.connection.cursor()
            query = "SELECT id FROM typesong WHERE name = %s"
            cursor.execute(query, (type_name,))
            result = cursor.fetchone()
            cursor.close()
            if result:
                return result[0]
            else:
                return None
    def getSingerIdByName(self, artist_name):
        print("Artist Name:", artist_name)
        print("Type of Artist Name:", type(artist_name))
        cursor = self.connection.cursor()
        query = "SELECT id FROM singer WHERE name = %s"
        cursor.execute(query, (artist_name,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return result[0]
        else:
            return None

        
    def addSinger(self, artist_name):
        cursor = self.connection.cursor()
        query = "INSERT INTO singer (name) VALUES (%s)"
        cursor.execute(query, (artist_name,))
        self.connection.commit()
        new_singer_id = cursor.lastrowid
        cursor.close()
        return new_singer_id
    
    def selectSongsByTypeId(self, type_id):
        cursor = self.connection.cursor()
        query = "SELECT * FROM song WHERE idType = %s"
        cursor.execute(query, (type_id,))
        result = cursor.fetchall()
        list_songs = []
        for row in result:
            song = Music(row[0], row[1], row[2], row[3], row[4], row[5])
            list_songs.append(song)
        cursor.close()
        return list_songs
    
    def select_all_songs_with_details(self):
        cursor = self.connection.cursor()
        query = """
        SELECT song.id, song.name, song.file_path, song.image, typesong.id, typesong.name, singer.id, singer.name 
        FROM song
        JOIN typesong ON song.idType = typesong.id
        JOIN singer ON song.idSinger = singer.id
        LIMIT 0, 25
        """
        cursor.execute(query)
        result = cursor.fetchall()
        list_music = []
        for row in result:
            # Tạo đối tượng Type và Singer với thông tin tương ứng
            music_type = Type(row[4], row[5])
            singer = Singer(row[6], row[7])

            # Tạo đối tượng Music với đối tượng Type và Singer
            music = Music(row[0], row[1], row[2], row[3], music_type, singer)
            list_music.append(music)

        cursor.close()
        return list_music
    
    # In class SongDao
    def delete_song(self, song_id):
        cursor = self.connection.cursor()
        query = "DELETE FROM song WHERE id = %s"
        cursor.execute(query, (song_id,))
        self.connection.commit()
        cursor.close()

    def searchByName(self, name, connection):
        cursor = connection.cursor()
        query = "SELECT * FROM song WHERE LOWER(name) LIKE %s"
        cursor.execute(query, ('%' + name.lower() + '%',))
        result = cursor.fetchall()
        list_music = [Music(*row) for row in result]
        cursor.close()
        return list_music

    def __del__(self):
        self.connection.close()
