import mysql.connector
import sys
sys.path.append('C:/Users/Admin/Downloads/ProjectAudio_Report/ProjectPythonAudio')

from object.music import Playlist
from object.music import Music

class PlaylistDAO:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='musicplayer'
        )

    def get_all_playlists(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM playlist")
        playlists = []
        for (id, name, image, created_at) in cursor:
            playlists.append(Playlist(id, name, image, created_at))
        cursor.close()
        return playlists
    def get_playlist_by_id(self, playlist_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM playlist WHERE id = %s", (playlist_id,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return Playlist(*result)
        else:
            return None

    def add_playlist(self, name, image_url):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO playlist (name, image) VALUES (%s, %s)", (name, image_url))
        self.connection.commit()
        cursor.close()


    def add_song_to_playlist(self, playlist_id, song_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM playlist_song WHERE playlist_id = %s AND song_id = %s", (playlist_id, song_id))
        result = cursor.fetchone()
        if result is None:
            cursor.execute("INSERT INTO playlist_song (playlist_id, song_id) VALUES (%s, %s)", (playlist_id, song_id))
            self.connection.commit()
        cursor.close()


    def get_songs_in_playlist(self, playlist_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT s.*, si.name AS artist_name 
            FROM song s
            JOIN playlist_song ps ON s.id = ps.song_id
            LEFT JOIN singer si ON s.idSinger = si.id
            WHERE ps.playlist_id = %s
        """, (playlist_id,))
        songs = []
        for row in cursor:
            songs.append(Music(*row))
        cursor.close()
        return songs
    
    def get_songs_in_playlist(self, playlist_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT s.*, si.name AS artist_name 
            FROM song s
            JOIN playlist_song ps ON s.id = ps.song_id
            LEFT JOIN singer si ON s.idSinger = si.id
            WHERE ps.playlist_id = %s
        """, (playlist_id,))
        songs = []
        for row in cursor:
            songs.append(Music(*row))
        cursor.close()
        return songs


    def delete_playlist(self, playlist_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM playlist WHERE id = %s", (playlist_id,))
        self.connection.commit()
        cursor.close()
    def delete_song_from_playlist(self, playlist_id, song_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM playlist_song WHERE playlist_id = %s AND song_id = %s", (playlist_id, song_id))
        self.connection.commit()
        cursor.close()

    def update_playlist(self, playlist_id, new_name):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE playlist SET name = %s WHERE id = %s", (new_name, playlist_id))
        self.connection.commit()
        cursor.close()

    def update_playlist_image(self, playlist_id, image_path):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE playlist SET image = %s WHERE id = %s", (image_path, playlist_id))
        self.connection.commit()
        cursor.close()

    def remove_song_from_playlist(self, playlist_id, song_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM playlist_song WHERE playlist_id = %s AND song_id = %s", (playlist_id, song_id))
        self.connection.commit()
        cursor.close()

    def update_song_in_playlist(self, playlist_id, old_song_id, new_song_id):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE playlist_song SET song_id = %s WHERE playlist_id = %s AND song_id = %s", (new_song_id, playlist_id, old_song_id))
        self.connection.commit()
        cursor.close()
    def get_latest_playlist(self):
        # Truy vấn SQL để lấy playlist mới nhất từ cơ sở dữ liệu
        query = "SELECT * FROM playlist ORDER BY created_at DESC LIMIT 1"
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query)
        latest_playlist = cursor.fetchone()
        cursor.close()
        return latest_playlist
    def __del__(self):
        self.connection.close()