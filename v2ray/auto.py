import os
import requests
from bs4 import BeautifulSoup


def get_code(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    html = requests.get(url, headers=header)
    soup = BeautifulSoup(html.text, 'html.parser')
    code = soup.find('code').string
    return code


if __name__ == '__main__':
    # # 获取当前工作目录
    # current_directory = os.getcwd()
    # # 构造上级目录的路径
    # parent_dir = os.path.dirname(current_directory)
    # output_file_path = os.path.join(parent_dir, 'speed.txt')
    url = 'https://abshare.github.io/'
    # get_code(url)
    with open('speed.txt', 'w', encoding='utf-8') as f:
        f.write(get_code(url))
