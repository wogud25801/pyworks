#DB - 사원 관리
import sqlite3

def select_emp():
    # 사원 전체 검색
    conn = sqlite3.connect("c:/mydb/willdb.db") #연결 객체 생성
    cur = conn.cursor()  #작업 객체 생성
    sql = "SELECT * FROM employee ORDER BY salary DESC"
    # 검색 SQL 언어 (ASC-오름차순, DESC-내림차순)
    cur.execute(sql)                # sql 실행
    # 자료 가져오기
    rs = cur.fetchall()   #rs-resulte set
    #print(rs)
    for i in rs:
        print(i)
    conn.close()   # 연결 종료

def insert_emp():
    # 사원 정보 삽입
    conn = sqlite3.connect("c:/mydb/willdb.db")
    cur = conn.cursor()
    sql = "INSERT INTO employee(emp_id, name, age) VALUES ('e102', '안산', 21)"
    cur.execute(sql)
    conn.commit()  # 커밋 실행
    conn.close()   # 연결 종료

def select_one():
    # 특정한 사원 1명 검색
    conn = sqlite3.connect("c:/mydb/willdb.db")
    cur = conn.cursor()
    sql = "SELECT * FROM employee WHERE emp_id = 'e101'"
    cur.execute(sql)
    rs = cur.fetchone()   # 1개 반환
    print(rs)
    conn.close()

def update_emp():
    # 사원 정보 수정
    conn = sqlite3.connect("c:/mydb/willdb.db")
    cur = conn.cursor()
    sql = "UPDATE employee SET salary = 10000 WHERE name = '안산'"
    cur.execute(sql)
    conn.commit()  # 커밋 실행
    conn.close()

def delete_emp():
    # 사원 정보 삭제
    conn = sqlite3.connect("c:/mydb/willdb.db")
    cur = conn.cursor()
    sql = "DELETE FROM employee WHERE emp_id = 'e103'"
    cur.execute(sql)
    conn.commit()
    conn.close()

# insert_emp()
#select_one()
#update_emp()
delete_emp()
select_emp()