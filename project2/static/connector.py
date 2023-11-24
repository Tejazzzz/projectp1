import mysql.connector as mc
conn = mc.connect(host='localhost',
                  password='project',
                  user='root')

if conn.is_connected:
    print("done") 