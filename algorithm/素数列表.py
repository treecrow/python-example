# 判断是否是素数
def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False


fs_ = open('素数列表.txt', 'w', encoding='utf-8')
try:
    for number in range(1, 10000):
        if is_prime(number):
            fs_.write(str(number) + '\n')
except IOError as ex:
    print(ex)
    print('写文件时发生错误!')
finally:
    fs_.close()
print('操作完成!')
