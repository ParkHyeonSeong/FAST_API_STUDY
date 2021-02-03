import sqlite3
print(sqlite3.version)
print(sqlite3.sqlite_version)

conn = sqlite3.connect("test.db", isolation_level=None) # db 생성(Auto Commit)
c = conn.cursor()   # 커서
command = ""
while command != "exit":
    command = input(">>")
    c.execute(command)
    print(c.fetchall())
