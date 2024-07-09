import os
import requests
import schedule as schedule
from bs4 import BeautifulSoup
import time


def get_code():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    url = 'https://abshare.github.io/'
    html = requests.get(url, headers=header)
    soup = BeautifulSoup(html.text, 'html.parser')
    code = soup.find('code').string
    with open('speed.txt', 'w', encoding='utf-8') as f:
        f.write(code)
    print('节点下载成功')


if __name__ == '__main__':
    # 安排每小时执行一次的任务
    # schedule.every(10).minute.do(get_code)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    get_code()



