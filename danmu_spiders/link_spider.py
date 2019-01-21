# -*- coding:utf-8 -*-

import pandas as pd
import requests
import time
import json
import os


def get_month_data(month):
    page = 1
    num = 1
    video_list = []

    while(True):
        print('*****' * 10, f'page[{page}]', '*****' * 10)

        # 处理月份格式
        if month in ['01', '03', '05', '07', '08', '10', '12']:
            url = f'https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&pic_size=160x100&order=click&copy_right=-1&cate_id=22&page={page}&pagesize=20&time_from=2018{month}01&time_to=2018{month}31'
        elif month in ['04', '06', '09', '11']:
            url = f'https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&pic_size=160x100&order=click&copy_right=-1&cate_id=22&page={page}&pagesize=20&time_from=2018{month}01&time_to=2018{month}30'
        else:
            url = f'https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&pic_size=160x100&order=click&copy_right=-1&cate_id=22&page={page}&pagesize=20&time_from=2018{month}01&time_to=2018{month}28'

        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
        html_code = requests.get(url, headers=headers).text

        # 获取当前网页最大页数
        max_page = json.loads(html_code)['numPages']
        # 获取视频信息
        results = json.loads(html_code)['result']

        for result in results:
            print(result['title'], result['arcurl'], result['pubdate'].split(' ')[0], result['play'], result['video_review'], result['favorites'], result['author'])
            video_list.append([result['title'],
                               result['arcurl'],
                               result['pubdate'].split(' ')[0],
                               result['play'],
                               result['video_review'],
                               result['favorites'],
                               result['author']])
            num += 1
        page += 1
        time.sleep(0.5)
        if page > max_page:
            if not os.path.isdir('csv_files'):
                os.mkdir('csv_files')
            result_df = pd.DataFrame(video_list, columns=['title', 'link', 'date', 'play_count', 'danmu_num', 'favorites', 'author'])
            result_df.to_csv(f'csv_files/month_{month}.csv', sep=',', na_rep='NA')
            break


for month in range(1,13):
    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)
    get_month_data(month)