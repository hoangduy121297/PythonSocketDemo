import sqlite3 as lite
import sys
import os
conn= None
try:

    conn = lite.connect("MyDb.db") #biến conn để connect
    with conn:
        cur= conn.cursor()  #biến cur để duyệt qua các bản ghi thông qua hàm cursor()
        cur.execute("SELECT SQLITE_VERSION()")  #execute để thực hiện câu truy vấn lấy version sqlite
        data=cur.fetchone() #lấy về dòng đầu tiên của database
        print("SQLite version " + str(data)) #in ra version
        cur.execute("CREATE TABLE Nguoidung1 (Id INT PRIMARY KEY, Name STRING);") #tao bang
        cur.execute("INSERT INTO Nguoidung1 VALUES(1,'Hoang Manh Duy');") #insert 1 hàng vào database

except lite.Error as e:
    print("Error: %s" %e.args[0]) #in ra exeption
    sys.exit(1)
finally:
    if conn:
        conn.close() #ngắt kết nối