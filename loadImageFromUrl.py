import requests
from io import BytesIO
from PyQt5 import QtGui

def loadImageFromUrl(url):
    response = requests.get(url)
    imageBytes = BytesIO(response.content)
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(imageBytes.getvalue())
    return pixmap
