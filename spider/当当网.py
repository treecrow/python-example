import requests
import re
import json

def main(page):
    print('start spider '+str(page)+' page')
    # 获取页面
    res = requests.get(
        'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page))
    # 解析页面
    pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>', re.S)
    items = re.findall(pattern, res.text)
    # 数据持久化
    for item in items:
        file_ = open('book.txt', 'a', encoding='UTF-8')
        item_ = {
            'range': item[0],
            'iamge': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
        }
        file_.write(json.dumps(item_, ensure_ascii=False) + '\n')
        file_.close()


if __name__ == "__main__":
    for i in range(1, 21):
        main(i)
