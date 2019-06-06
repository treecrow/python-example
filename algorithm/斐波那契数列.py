# 斐波那契数列
# https://baike.baidu.com/item/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97/99145


# 递归法
# def fib_recur(n):
#     assert n >= 0, "n > 0"
#     if n <= 1:
#         return n
#     return fib_recur(n-1) + fib_recur(n-2)
# for i in range(1, 20):
#     print(fib_recur(i))

# 递推法
# def fib_loop(n):
#     a, b = 0, 1
#     for i in range(n+1):
#         a, b = b, a + b
#         if i == n:
#             return a
# for j in range(20):
#     print(fib_loop(j), end=' ')
