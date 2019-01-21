# -*- coding:utf-8 -*-

import pandas as pd
import requests
import time
import re
import os


def get_xml_file(video_items):
    num = 1
    for item in video_items:
        av_num = item[0]
        date = re.sub('-', '', item[1])
        year_month = date[:-2]
        url = 'https://www.bilibili.com/video/av' + str(av_num)
        headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063' }
        html_code = requests.get(url, headers=headers).text

        # 正则匹配cid编号
        if not re.match(f'.*"cid=(\d+)&aid={av_num}',html_code):
            print(f'[{num}] {url} done')
            num += 1
            continue
        cid_num = re.match(f'.*"cid=(\d+)&aid={av_num}',html_code).group(1)
        xml_url = 'http://comment.bilibili.com/' + cid_num + '.xml'
        xml_data = requests.get(xml_url, headers=headers).content

        # 创建csv文件路径
        if not os.path.isdir('xml_files'):
            os.mkdir('xml_files')
        if not os.path.isdir(f'xml_files/{year_month}'):
            os.mkdir(f'xml_files/{year_month}')
        if not os.path.isdir(f'xml_files/{year_month}/{date}'):
            os.mkdir(f'xml_files/{year_month}/{date}')

        if os.path.isfile(f'xml_files/{year_month}/{date}/' + str(av_num) + '.xml'):
            print(f'[{num}] {url} done')
            num += 1
            continue

        # 弹幕文件保存为csv
        with open(f'xml_files/{year_month}/{date}/' + str(av_num) + '.xml', 'wb') as f:
            f.write(xml_data)
        print(f'[{num}] {url} done')
        num += 1
        time.sleep(0.1)


data = pd.read_csv('csv_files/month_01.csv')
video_items = [[row['link'].split('av')[1], row['date']] for index,row in data.iterrows()]
get_xml_file(video_items)

