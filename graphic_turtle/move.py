import turtle

turtle.shape("turtle")
turtle.color('blue')

# 이동
"""
turtle.forward(100)  # forward(거리)
turtle.right(90)     # right(각도)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
"""

# for문 구현
# 사각형
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.color('red')
for i in range(3):
    turtle.forward(100)
    turtle.left(120)

turtle.color('green')
turtle.circle(50)  #반지름-50

turtle.mainloop()