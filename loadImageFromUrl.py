import os
import requests
from PyQt5 import QtGui
from io import BytesIO

def loadImageFromUrl(url):
    # Nếu đường dẫn là URL, hãy đảm bảo nó có "schema"
    if url.startswith(("http://", "https://")):
        # Gửi yêu cầu HTTP
        try:
            response = requests.get(url, timeout=5)  # Thời gian chờ 5 giây
            response.raise_for_status()  # Kiểm tra phản hồi hợp lệ
            image_bytes = BytesIO(response.content)  # Dữ liệu hình ảnh
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(image_bytes.getvalue())  # Tạo QPixmap từ dữ liệu
            return pixmap
        except Exception as e:
            # Xử lý lỗi kết nối hoặc HTTP
            print(f"Error loading image from URL: {e}")
            return QtGui.QPixmap("image/default.jpg")  # Sử dụng hình ảnh mặc định
    
    elif os.path.exists(url):
        # Nếu là tệp cục bộ, trả về QPixmap từ tệp
        return QtGui.QPixmap(url)
    
    return QtGui.QPixmap("image/MUSIC.jpg")  # Sử dụng hình ảnh mặc định nếu không hợp lệ
