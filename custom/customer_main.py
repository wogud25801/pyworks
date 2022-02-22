from custom.customer import Customer
from custom.goldcustomer import GoldCustomer
from custom.vipcustomer import VIPCustomer

silver = Customer(101, "놀부")
gold = GoldCustomer(102, "흥부")
vip = VIPCustomer(103, "심청", 7777)

price = 10000
# 상품 가격 계산
cost_s = silver.calc_price(price)
cost_g = gold.calc_price(price)
cost_v = vip.calc_price(price)

print("********** 상품 구매 비용 **********")
print(silver.getname() + "님의 구매 비용은 " + str(cost_s) + "원입니다.")
print(gold.getname() + "님의 구매 비용은 " + str(cost_g) + "원입니다.")
print(vip.getname() + "님의 구매 비용은 " + str(cost_g) + "원입니다.")

print("******************** 고객 정보 ********************")
print(silver)
print(gold)
print(vip)