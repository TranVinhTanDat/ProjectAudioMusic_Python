import mysql.connector
import sys
sys.path.append('C:/Users/Admin/Downloads/ProjectAudio_Report/ProjectPythonAudio')
from object.music import Album
from object.music import Music

class AlbumDAO:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='musicplayer'
        )

    def get_all_albums(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM album")
        albums = []
        for (id, name, release_date, cover_image) in cursor:
            albums.append(Album(id, name, release_date, cover_image))
        cursor.close()
        return albums

    def get_album_by_id(self, album_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM album WHERE id = %s", (album_id,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return Album(*result)
        else:
            return None

    def add_album(self, name, release_date, cover_image):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO album (name, release_date, cover_image) VALUES (%s, %s, %s)", (name, release_date, cover_image))
        self.connection.commit()
        cursor.close()

    def add_song_to_album(self, album_id, song_id):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO album_song (album_id, song_id) VALUES (%s, %s)", (album_id, song_id))
        self.connection.commit()
        cursor.close()

    def get_songs_in_album(self, album_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT song.*, singer.name FROM song
            JOIN album_song ON song.id = album_song.song_id
            JOIN singer ON song.idSinger = singer.id
            WHERE album_song.album_id = %s
        """, (album_id,))
        songs = []
        for row in cursor:
            # Giả sử rằng cột cuối cùng trong row là tên nghệ sĩ
            music = Music(row[0], row[1], row[2], row[3], row[4], row[5])
            music.artist_name = row[-1]  # Gán tên nghệ sĩ vào thuộc tính mới
            songs.append(music)
        cursor.close()
        return songs

