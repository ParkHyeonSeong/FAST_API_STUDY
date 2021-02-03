import sqlite3
print(sqlite3.version)
print(sqlite3.sqlite_version)

def user_login_compare(id, pwd):

    conn = sqlite3.connect("test.db", isolation_level=None) # db 생성(Auto Commit)
    c = conn.cursor()   # 커서
    db_pwd = c.execute("SELECT password FROM USER_DB WHERE id='%s'" % id).fetchall()
    conn.close()
    if db_pwd == []:    # 데이터베이스에서 찾을 수 없음
        return "계정이 존재하지 않습니다."
    if pwd == db_pwd[0][0]: # id pwd 일치
        return "로그인에 성공하였습니다"
    else:   # 비밀번호 불일치
        return "비밀번호가 일치하지 않습니다."

