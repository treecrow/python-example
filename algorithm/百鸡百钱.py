# 百鸡百钱
# https://baike.baidu.com/item/%E7%99%BE%E9%B8%A1%E7%99%BE%E9%92%B1/5857320

# 穷举法
import random
for x in range(0, 20):
    for y in range(0, 33):
        z = 100-x-y
        if 5*x+3*y+z/3 == 100:
            print('公鸡：%s 母鸡：%s 小鸡：%s' % (x, y, z))

# 随机方
while True:
    x = random.randrange(0, 20)
    y = random.randrange(0, 33)
    z = random.randrange(0, 100)
    if 5*x+3*y+z/3 == 100 and x+y+z == 100:
        print('公鸡:', x)
        print('母鸡:', y)
        print('小鸡:', z)
