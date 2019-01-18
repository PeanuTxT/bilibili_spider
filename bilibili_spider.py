# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import jieba
import re
import os

def get_xml_file(aid_nums):
    for aid_num in aid_nums:
        aid_url = 'https://www.bilibili.com/video/av' + str(aid_num)
        headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063' }
        html_code = requests.get(aid_url, headers=headers).text

        # 正则匹配cid编号
        cid_num = re.match(f'.*"cid=(\d+)&aid={aid_num}',html_code).group(1)
        xml_url = 'http://comment.bilibili.com/' + cid_num + '.xml'
        xml_data = requests.get(xml_url, headers=headers).content

        if not os.path.isdir('xml_files'):
            os.mkdir('xml_files')
        with open('xml_files/' + str(aid_num) + '.xml', 'wb') as f:
            f.write(xml_data)

def get_danmu_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
    soup = BeautifulSoup(data, 'lxml')
    danmu_list = [x.get_text() for x in soup.find_all('d')]

    final_list = []
    for sentence in danmu_list:
        for word in sentence:
            if len(word) > 1:
                final_list.append(word)
    print(danmu_list)

url_list = ['https://www.bilibili.com/video/av40909320']
av_num = [av_num.split('av')[1] for av_num in url_list]
get_xml_file(av_num)
get_danmu_txt('xml_files/40909320.xml')

