# 튜플 자료구조로 예제
# 고민 상담 예제
import random
import time

answers = (
    "자! 해보세요!",
    "됐네요, 이 사람아",
    "뭐라고? 다시 생각해보세요",
    "모르니 두려운 것입니다.",
    "당신이라면 할 수 있어요!"
)

print("""
안녕하세요~ Magic 상담소입니다.
조언을 구하소 싶으면 질문을 입력하고,
엔터 키를 누르세요""")

question = input("질문 : ")

print("고민 중...\n" * 4)
time.sleep(2)   # 대기 시간
"""
rnd = random.randint(0, 4)
print(rnd)
print(answers[rnd])
"""

# 리스트인 경우 랜던 선택 함수
print(random.choice(answers))