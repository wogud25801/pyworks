# 도서 db 만들기
import sqlite3 as sql

def getconn():
    # 데이터베이스 생성 및 접속
    conn = sql.connect("./book.db")
    return conn

def create_table():
    # book 테이블 생성
    con = getconn()
    cursur = con.cursor()
    sql = """
        CREATE TABLE book(
            book_no integer PRIMARY KEY AUTOINCREMENT,
            title text NOT NULL,
            publisher text NOT NULL,
            page integer
        )
    """
    cursur.execute(sql)
    con.commit()
    con.close()

def insert_book():
    # 도서 추가
    con = getconn()
    cursor = con.cursor()
    sql = "INSERT INTO book (title, publisher, page) VALUES (?, ?, ?)"
    # book_no는 자동이므로 입력하면 안됨
    cursor.execute(sql, ('점프 투 파이썬', '박응용', 350))
    con.commit()
    con.close()

def select_book():
    # 도서 전체 검색
    con = getconn()
    cursor = con.cursor()
    sql = "SELECT * FROM book"
    cursor.execute(sql)
    # 책 정보 가져오기
    rs = cursor.fetchall()
    print(rs)
    for i in rs:
        print(i)
    con.close()

def select_one():
    # 특정 도서 검색
    con = getconn()
    cursor = con.cursor()
    sql = "SELECT * FROM book WHERE book_no = ?"
    cursor.execute(sql, (2,))  # 튜플 1개일때 콤머 붙임
    # 책 정보 가져오기
    rs = cursor.fetchone()
    print(rs)
    con.close()

def update_book():
    # 도서 수정
    con = getconn()
    cursor = con.cursor()
    sql = "UPDATE book SET page = ? WHERE book_no = ?"
    cursor.execute(sql, (400, 2))
    con.commit()
    con.close()

def delete_book():
    # 도서 삭제
    con = getconn()
    cursor = con.cursor()
    sql = "DELETE FROM book WHERE book_no = ?"
    cursor.execute(sql, (1, ))
    con.commit()
    con.close()

if __name__=="__main__":
    # con = getconn()
    # print(con, "연결됨")
    #create_table()
    #insert_book()
    #select_one()
    #update_book()
    delete_book()
    select_book()