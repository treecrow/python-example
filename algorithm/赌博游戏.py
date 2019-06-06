# Craps赌博游戏
# https://blog.csdn.net/Darkman_EX/article/details/80630332

from random import randint
def main():
    money = 1000
    while money > 0:
        print('你的总资产为:', money)
        needs_go_on = False

        # 下注金额大于等于0小于等于总资产才能往下进行，否则一直提示“请下注”
        while True:
            debt = int(input('请下注: '))
            if debt > 0 and debt <= money:
                break

        first = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % first)
        if first == 7 or first == 11:
            print('玩家胜!')
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print('庄家胜!')
            money -= debt
        else:
            needs_go_on = True

        # 僵持阶段（7-庄家， first-玩家）
        while needs_go_on:
            current = randint(1, 6) + randint(1, 6)
            print('玩家摇出了%d点' % current)
            if current == 7:
                print('庄家胜')
                money -= debt
                needs_go_on = False
            elif current == first:
                print('玩家胜')
                money += debt
                needs_go_on = False

    print('你破产了, 游戏结束!')


if __name__ == '__main__':
    main()
