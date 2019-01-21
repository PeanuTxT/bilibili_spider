# -*- coding:utf-8 -*-

import requests
import re


def get_xml_file(av_num):
    url = 'https://www.bilibili.com/video/av' + str(av_num)
    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063' }
    html_code = requests.get(url, headers=headers).text

    # 正则匹配cid编号
    if not re.match(f'.*"cid=(\d+)&aid={av_num}',html_code):
        pass
    cid_num = re.match(f'.*"cid=(\d+)&aid={av_num}',html_code).group(1)
    xml_url = 'http://comment.bilibili.com/' + cid_num + '.xml'
    xml_data = requests.get(xml_url, headers=headers).content

    # 弹幕文件保存为csv
    with open(str(av_num) + '.xml', 'wb') as f:
        f.write(xml_data)

    print('done...')

if __name__ == '__main__':
    get_xml_file('40681810')

