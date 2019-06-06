# 判断是否是回文数
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10  # 增加一个数量级 && 个位数追加剩余数的个位数
        temp //= 10
    return total == num


print(is_palindrome(6789))
