# 约瑟夫环问题
# https://zh.wikipedia.org/wiki/%E7%BA%A6%E7%91%9F%E5%A4%AB%E6%96%AF%E9%97%AE%E9%A2%98

persons = [True] * 30
counter, index, number = 0, 0, 0 # 丢下去的人数，真实索引，记录是否达到阈值
while counter < 15:
    if persons[index]: # 为 False 说明已经扔下去，掠过
        number += 1
        if number == 9:
            persons[index] = False
            counter += 1
            number = 0
    index += 1
    index %= 30

for person in persons:
    print('基' if person else '非', end='')
