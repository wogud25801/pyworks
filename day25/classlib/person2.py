#멤버 변수를 private으로 만들면 get, set함수를 만들어 접근함
class Person:
    def __init__(self):
        self._name = ""
        self._age = 0

    def setname(self, name):
        self._name = name

    def getname(self):
        return self._name

    def setage(self, age):
        self._age = age

    def getage(self):
        return self._age

p1 = Person()
p1.setname("흥부")
p1.setage(31)
print("이름 :", p1.getname())
print("나이 :", p1.getage())