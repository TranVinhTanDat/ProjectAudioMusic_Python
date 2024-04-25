import sys
sys.path.append('C:/Users/Admin/Downloads/ProjectAudio_Report/ProjectPythonAudio')
from object.music import *
from dao.TypeDAO import *
from dao.SingerDAO import *
from dao.SongDAO import *
# from dao.AlbumDAO import AlbumDAO


class MusicController:
    typeDao = TypeDao()
    singerDao = SingerDao()
    songDao = SongDao()
    # albumDao = AlbumDAO()  # Thêm dòng này để tạo đối tượng albumDao

    def __init__(self) -> None:
        pass

    def searchTypeId(self, name):
        type_obj = self.typeDao.searchName(name)
        if type_obj:
            return type_obj.id
        return None

    def searchName(self, name):
        return self.typeDao.searchName(name)

    def searchSingerId(self, id):
        # Sử dụng phương thức selectSingerById để tìm kiếm theo id
        return self.singerDao.selectSingerById(id)

    def listTypeDao(self):
        return self.typeDao.SelectListType()

    def searchListSongType(self, type_name):
        type_obj = self.typeDao.selectTypeByName(type_name)  # Sử dụng phương thức mới
        if type_obj:
            return self.songDao.selectSongsByTypeId(type_obj.id)  # Giả sử bạn có phương thức này
        return []

    # Các phương thức khác giữ nguyên...


    def searchText(self, text):
        result = []
        while len(text) > 0:
            songs = self.searchNameSong(text)
            if songs:
                return songs
            songs = self.searchListSongToType(self.searchNameType(text))
            if songs:
                return songs
            songs = self.searchListSongToSinger(self.searchNameSinger(text))
            if songs:
                return songs
            text = text[1:]
        return result

    def searchNameSong(self, name):
        result = []
        length = len(name)
        songs = self.songDao.SelectList()
        for song in songs:
            if name == song.name[:length]:
                result.append(song)
        return result

    def searchNameType(self, name):
        result = []
        length = len(name)
        types = self.typeDao.SelectListType()
        for type_ in types:
            if name == type_.name[:length]:
                result.append(type_)
        return result

    def searchListSongToType(self, types):
        result = []
        songs = self.songDao.SelectList()
        for type_ in types:
            for song in songs:
                if type_.id == song.idType:
                    result.append(song)
        return result


    def searchNameSinger(self, name):
        result = []
        length = len(name)
        singers = self.singerDao.SelectList()
        for singer in singers:
            if name == singer.name[:length]:
                result.append(singer)
        return result

    def searchListSongToSinger(self, singers):
        result = []
        songs = self.songDao.SelectList()
        for singer in singers:
            for song in songs:
                if singer.id == song.idSinger:
                    result.append(song)
        return result

    def listSong(self):
        return self.songDao.SelectList()

# Trong phương thức addMusic của MusicController.py
    def addMusic(self, link, name, artist_id, image_path, type_name):
        self.songDao.addMusic(link, name, artist_id, image_path, type_name)

    def getSingerIdByName(self, artist_name):
        return self.songDao.getSingerIdByName(artist_name)

    def addSinger(self, artist_name):
        return self.songDao.addSinger(artist_name)