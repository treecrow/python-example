# https://baike.baidu.com/item/%E5%AE%8C%E5%85%A8%E6%95%B0/370913
# 求出10000以内所有的完全数

def numbers(number):
    sum = 0
    d = list()
    for i in range(1, number):
        if number % i == 0:
            d.append(i)
        else:
            continue
    for i in d:
        sum += i
    if sum == number:
        print(number)


for i in range(2, 10001):
    numbers(i)
