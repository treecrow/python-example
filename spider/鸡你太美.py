from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get("https://www.bilibili.com/")

WAIT = WebDriverWait(browser, 10)

# 被那个破登录遮住了
index = WAIT.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "#primary_menu > ul > li.home > a")))
index.click()

# 模拟搜索
input = WAIT.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#banner_link > div > div > form > input")))
submit = WAIT.until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="banner_link"]/div/div/form/button')))
input.send_keys('蔡徐坤 篮球')
submit.click()

# 获取并存储数据
def get_source():
    WAIT.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#server-search-app > div.contain > div.body-contain > div > div.result-wrap.clearfix')))
    soup = BeautifulSoup(browser.page_source, 'lxml')
    print(soup.title)

# 切换操作页面
browser.switch_to.window(browser.window_handles[1])
# 总共多少页
lastPage = WAIT.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#server-search-app > div.contain > div.body-contain > div > div.page-wrap > div > ul > li.page-item.last > button")))
totalPage = int(lastPage.text)
# 获取首页数据
get_source()


# 遍历后面页面
for page in range(2, int(totalPage+1)):
    # 下一页
    next_btn = WAIT.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#server-search-app > div.contain > div.body-contain > div > div.page-wrap > div > ul > li.page-item.next > button')))
    next_btn.click()
    # 判断下一页切换成功
    WAIT.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '#server-search-app > div.contain > div.body-contain > div > div.page-wrap > div > ul > li.page-item.active > button'), str(page)))
    # 获取soup
    get_source()
