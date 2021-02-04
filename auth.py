import sqlite3
import jwt
import secret

def user_login_compare(id, pwd):

	conn = sqlite3.connect("test.db", isolation_level=None) # db 생성(Auto Commit)
	c = conn.cursor()   # 커서
	db_pwd = c.execute("SELECT password FROM USER_DB WHERE id='%s'" % id).fetchall()
	



	
	if db_pwd == []:	# 데이터베이스에서 찾을 수 없음
		conn.close()	# 쿼리 연결 종료
		return "0"
	if pwd == db_pwd[0][0]: # id pwd 일치
		data = {'user_id' : id}
		token = jwt.encode(data, secret.SECRET_KEY, secret.ALGORITHM)
		c.execute("UPDATE USER_DB SET token = ? WHERE id = ?", (token, id))

		conn.close()	# 쿼리 연결 종료
		return token
	else:   # 비밀번호 불일치
		conn.close()	# 쿼리 연결 종료
		return "2"

