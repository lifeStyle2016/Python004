import requests
from bs4 import BeautifulSoup as bs
import json
from time import sleep
import pandas as pd
import re
import random

#日期解析
def get_time(movie_time) :
    movie_time = movie_time.replace('年', '-').replace('月', '-').replace('日',
                                                         ' ').replace('/', '-').strip()
    movie_time = re.sub('\s+', ' ', movie_time)
    t = ''
    regex_list = [
     '(\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2})',
     '(\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2})',
     '(\d{4}-\d{1,2}-\d{1,2})',
     '(\d{4}-\d{1,2})',
    ]
    for regex in regex_list:
        t = re.search(regex, movie_time)
        if t:
            t = t.group(1)
            return t
    return t

#解析电影名称、电影类型和上映时间
def parser_url(abs_url) :
    sleep(random.sample(range(10),1)[0])
    detail_res = requests.get(abs_url, headers=req_headers)
    detail_pser = bs(detail_res.text, 'html.parser')
    for tag_divs in detail_pser.find_all('div', attrs={'class' : 'movie-brief-container'}) :
        movie_name = tag_divs.find('h1', attrs={'class' : 'name'}).text.strip()
        tag_lis = tag_divs.find_all('li', attrs={'class' : 'ellipsis'})

        movie_type = []
        for lis in tag_lis[0].find_all('a'):
            movie_type.append(lis.text.strip())

        movie_time = get_time(tag_lis[-1].text.strip())
        #文件保存
        print(movie_name,' / '.join(movie_type),movie_time)
        movie_data = [(movie_name,' / '.join(movie_type), movie_time)]
        pd_list = pd.DataFrame(data = movie_data)
        pd_list.to_csv('./movie_detail.csv', sep=',', mode='a', encoding='utf_8_sig', index=False, header=False)


topN = 10
my_url = 'https://maoyan.com/films?showType=3'
dmn = 'https://maoyan.com'

req_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Cookie': '__mta=145054347.1601213060399.1601261306207.1601261310125.11; uuid_n_v=v1; uuid=BF03CF2000C411EB908019617B169A6301140148A7ED4516A943A51FD92CBE59; _csrf=5fc098c6647fa27b06a3e282564a04474d7fcd88d6abf69b168f2784a8067583; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1601213060; _lxsdk_cuid=174cfbc5486c8-01a7c4ab33b123-5e1a3c18-1fa400-174cfbc5486c8; mojo-uuid=299881d2bca23f7e9c24bac61fca6aa9; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22174d012ceb62e1-016decc97ffc73-2c76224e-349600-174d012ceb717c%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22174d012ceb62e1-016decc97ffc73-2c76224e-349600-174d012ceb717c%22%7D; _lxsdk=BF03CF2000C411EB908019617B169A6301140148A7ED4516A943A51FD92CBE59; mojo-session-id={"id":"31973318e4f5853df566066c175a1e09","time":1601291676697}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1601291677; __mta=145054347.1601213060399.1601261310125.1601291676924.12; _lxsdk_s=174d46bec6e-10d-4dc-cd%7C%7C2'
    }

#初始化
movie_title = [('电影名称', '电影类型', '上映时间')]
pd_title = pd.DataFrame(data = movie_title)
pd_title.to_csv('./movie_detail.csv', sep=',', mode='w', encoding='utf_8_sig', index=False, header=False)

html_res = requests.get(my_url,headers=req_headers)
sleep(random.sample(range(10),1)[0])
html_pser = bs(html_res.text, 'html.parser')

#解析
for tag_divs in html_pser.find_all('div', attrs={'class':'channel-detail movie-item-title'}) :
    if topN > 0 : 
        topN = topN - 1
        abs_url = dmn + tag_divs.find('a').get('href')
        parser_url(abs_url)
