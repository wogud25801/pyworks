from custom.customer import Customer
from custom.goldcustomer import GoldCustomer
from custom.vipcustomer import VIPCustomer

# 객체 리스트 생성
customer = [
    Customer(101, "놀부"),
    Customer(102, "팥쥐"),
    GoldCustomer(201, "흥부"),
    GoldCustomer(202, "콩쥐"),
    VIPCustomer(301, "심청", 777)
]

# 상품 가격 계산
price = 20000
print("********** 구매 비용 **********")
for c in customer:
    cost = c.calc_price(price)
    #print(c.getname() + "님의 구매비용은 " + str(cost) + "원입니다.")
    print(c.getname() + "님의 구매비용은 " + format(cost, ',d') + "원입니다.")

print("*********** 고객 정보 **********")
for c in customer:
    print(c)