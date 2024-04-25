
import mysql.connector
import sys
import sys
sys.path.append('C:/Users/Admin/Downloads/ProjectAudio_Report/ProjectPythonAudio')
from object.music import Singer
from object.music import Music
import eyed3

class SingerDao:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='musicplayer'
        )

    def selectSingerById(self, singer_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM singer WHERE id = %s", (singer_id,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return Singer(result[0], result[1])
        else:
            return None
    def getSingerIdByName(self, artist_name):
            cursor = self.connection.cursor()
            query = "SELECT id FROM singer WHERE name = %s"
            cursor.execute(query, (artist_name,))
            result = cursor.fetchone()
            cursor.close()
            if result:
                return result[0]
            else:
                return None
            
    def get_album_art(self, file_path):
        audiofile = eyed3.load(file_path)
        if audiofile.tag and audiofile.tag.images:
            # Lấy ảnh đầu tiên trong các ảnh của ID3 tag (thường là ảnh bìa album)
            image_data = audiofile.tag.images[0].image_data
            return image_data
        else:
            return None
    def SelectList(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name, image FROM singer")  # Sửa đổi câu lệnh SQL để bao gồm cột image
        result = cursor.fetchall()
        list_singer = []
        for row in result:
            # Bây giờ row cũng sẽ chứa đường dẫn hình ảnh, vì vậy bạn cần thêm nó vào đối tượng Singer
            singer = Singer(row[0], row[1], row[2])  # row[2] chính là cột image
            list_singer.append(singer)
        cursor.close()
        return list_singer
    def getSongsByArtist(self, artist_id):
            cursor = self.connection.cursor()
            # Giả sử cấu trúc bảng `song` có một cột `idSinger` để lưu id của nghệ sĩ
            query = """
            SELECT id, name, file_path, image, idType, idSinger
            FROM song
            WHERE idSinger = %s
            """
            cursor.execute(query, (artist_id,))
            result = cursor.fetchall()
            list_songs = []
            for row in result:
                song = Music(row[0], row[1], row[2], row[3], row[4], row[5])
                list_songs.append(song)
            cursor.close()
            return list_songs

    # Define other methods as needed

    def __del__(self):
        self.connection.close()