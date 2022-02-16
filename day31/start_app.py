# 웹 서버 만들기
# 127.0.0.1 주소를 사용하기
from flask import Flask

# 웹 서버 객체 생성
app = Flask(__name__)

# url 경로 설정
@app.route('/')  # 루트 경로 - 127.0.0.1:5000/
def index():
    return "<h1>Hello ~ Flask</h1>"

@app.route('/login/') # 127.0.0.1:5000/login/
def login():
    return "<h1>로그인 페이지 입니다.</h1>"

@app.route('/register/')  # 127.0.0.1:5000/registar/
def registar():
    return "<h1>회원가입 페이지 입니다.</h1>"

@app.route('/info/')  # 127.0.0.1:5000/info/
def info():
    return "<h1>회원 정보</h1>"

app.run()