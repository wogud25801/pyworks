import turtle as t

# 다각형 그리기
def polygon(n):
    for i in range(n):
        t.forward(50)
        t.left(360 / n)  # 다각형의 내각 공식

def polygon2(n, d):
    for i in range(n):
        t.forward(d)
        t.left(360 / n)

t.shape()  # 기본이므로 생략 가능
polygon(3)
polygon(5)

# 거리 이동
t.up()     # 펜 올리기
t.forward(100)
t.color('blue')
t.down()   # 펜 내리기

polygon2(3, 100)
polygon2(5, 100)
t.mainloop()