import mysql.connector
from datetime import datetime

mydb= mysql.connector.connect(host="localhost",user="user",password="password",port="3310")
mycursor=mydb.cursor()
#mycursor.execute("Create database `images`;")
mycursor.execute("USE `images`")
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("""
CREATE TABLE IF NOT EXISTS face_recognizers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    face_image LONGBLOB NOT NULL,
    timestamp DATETIME NOT NULL,
    name VARCHAR(255)
)
""")
img_path = "media/binh/IT/OpenCV-Python-Series/src/7.png"
people = [
    ("Phan Văn Binh", "my.png"),
    ("Hotgirl", "hotgirl.jpg"),
]
sql = """
INSERT INTO face_recognizers (face_image, timestamp, name)
VALUES (%s, %s, %s)
"""

for name, img_path in people:
    with open(img_path, 'rb') as file:
        image_data = file.read()
    mycursor.execute(sql, (image_data, datetime.now(), name))
mydb.commit()
