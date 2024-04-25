import mysql.connector
import sys
sys.path.append('C:/Users/Admin/Downloads/ProjectAudio_Report/ProjectPythonAudio')
from object.music import Type

class TypeDao:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='musicplayer'
        )

    def selectTypeIdByName(self, type_name):
        cursor = self.connection.cursor()
        query = "SELECT id FROM typesong WHERE name = %s"
        cursor.execute(query, (type_name,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return result[0]
        else:
            return None
    def addType(self, type_name):
        cursor = self.connection.cursor()
        query = "INSERT INTO typesong (name) VALUES (%s)"
        cursor.execute(query, (type_name,))
        self.connection.commit()
        new_type_id = cursor.lastrowid
        cursor.close()
        return new_type_id
    def SelectListType(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM typesong")
        result = cursor.fetchall()
        list_type = []
        for row in result:
            music_type = Type(row[0], row[1])
            list_type.append(music_type)
        cursor.close()
        return list_type
    
    def searchName(self, name):
        cursor = self.connection.cursor()
        query = "SELECT * FROM typesong WHERE name = %s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return Type(result[0], result[1])  # Trả về đối tượng Type nếu tìm thấy
        else:
            return None  # Trả về None nếu không tìm thấy
        
    def selectTypeById(self, type_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM typesong WHERE id = %s", (type_id,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return Type(result[0], result[1])
        else:
            return None
    
    def selectTypeByName(self, type_name):
        cursor = self.connection.cursor()
        query = "SELECT * FROM typesong WHERE name = %s"
        cursor.execute(query, (type_name,))
        result = cursor.fetchone()  # Sử dụng fetchone() vì chúng ta chỉ mong đợi một kết quả duy nhất
        cursor.close()
        if result:
            return Type(result[0], result[1])  # Tạo và trả về đối tượng Type dựa trên kết quả
        else:
            return None
        
    def insertType(self, type_obj):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO typesong (id, name) VALUES (%s, %s)", (type_obj.id, type_obj.name))
        self.connection.commit()
        cursor.close()
    
    def updateType(self, type_obj):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE typesong SET name = %s WHERE id = %s", (type_obj.name, type_obj.id))
        self.connection.commit()
        cursor.close()
    
    def deleteTypeById(self, type_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM typesong WHERE id = %s", (type_id,))
        self.connection.commit()
        cursor.close()

    def __del__(self):
        self.connection.close()
    def SelectListType(self):
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM typesong")
            result = cursor.fetchall()
            list_type = []
            for row in result:
                # Đảm bảo rằng đối tượng Type được tạo với cả id và name
                music_type = Type(row[0], row[1])  # Assumption: row[0] is id, row[1] is name
                list_type.append(music_type)
            cursor.close()
            return list_type
    
    