import sqlite3

def getconn():
    # db에 접속
    conn = sqlite3.connect("c:/dbtest/test.db")
    return conn

def create_table():
    # 회원 테이블 생성
    conn = getconn()
    cur = conn.cursor()
    sql = """
        CREATE TABLE member(
            mid char(5) PRIMARY KEY,
            passwd char(8) NOT NULL,
            name text NOT NULL,
            age integer
        )
    """
    cur.execute(sql)
    conn.commit()
    print("테이블 생성")
    conn.close()

def insert_member():
    # 회원 추가
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO member(mid, passwd, name, age) VALUES (?, ?, ?, ?)"
    cur.execute(sql, ('10002', 'ahn1004', '안산', 20 ))
    conn.commit()
    conn.close()

def select_member():
    # 회원 전체 검색
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member"
    cur.execute(sql)
    rs = cur.fetchall()
    print(rs)
    for i in rs:
        print(i)
    conn.close()

#conn = getconn()
#print("연결", conn)
#create_table()
#insert_member()
select_member()