

class Music:
    def __init__(self, id=-1, name="", file_path="", image="", idType=-1, idSinger=-1, artist_name="",singer=None):
        self.id = id
        self.name = name
        self.file_path = file_path
        self.image = image
        self.idType = idType
        self.idSinger = idSinger
        self.artist_name = artist_name  # Thêm thuộc tính này
        self.singer = singer


class Type:
    def __init__(self, id=-1, name=""):
        self.id = id
        self.name = name

class Singer:
    def __init__(self, id=-1, name="", image=""):
        self.id = id
        self.name = name
        self.image = image

class Album:
    def __init__(self, id=-1, name="", release_date=None, cover_image=""):
        self.id = id
        self.name = name
        self.release_date = release_date
        self.cover_image = cover_image
class Playlist:
    def __init__(self, id=-1, name="", image="", created_at=None):
        self.id = id
        self.name = name
        self.image = image
        self.created_at = created_at
