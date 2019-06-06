# https://baike.baidu.com/item/%E6%B0%B4%E4%BB%99%E8%8A%B1%E6%95%B0
# 寻找水仙花数

fibonacciList = []
for num in range(100, 1000):
    x = num // 100
    y = (num % 100) // 10
    z = num % 10
    if (x**3 + y**3 + z**3) == num:
        fibonacciList.append(num)

print(fibonacciList)
