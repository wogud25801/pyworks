# Counter 클래스 정의와 사용
class Counter:
    x = 0    #클래스 멤버 변수

    def __init__(self):  # 클래스 이름으로 직접 접근
        Counter.x = Counter.x + 1

    def getcount(self):
        return Counter.x

c1 = Counter()
#print(c1.x)  #1
print(c1.getcount())

c2 = Counter()
#print(c1.x)  #2
print(c2.getcount())

c3 = Counter()
print(c3.getcount())  #3