# -*- coding:utf-8 -*-

from collections import Counter
from bs4 import BeautifulSoup
import pandas as np
import os
import re


def list_all_files(rootdir, filetype):
    _files = []
    list = os.listdir(rootdir) # 列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
        path = os.path.join(rootdir,list[i])
        if os.path.isdir(path):
           month_list.append(path)
           _files.extend(list_all_files(path, filetype))
        if os.path.isfile(path):
            if path.split('.')[-1] in filetype:
                _files.append(path)
    return _files


def get_danmu_txt(path):

    date = path.split('\\')[1]
    date = date[:4] + '-' + date[4:6] + '-' + date[-2:]
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
    soup = BeautifulSoup(data, 'lxml')
    danmu_list = [x.get_text() for x in soup.find_all('d')]

    punctuation = '[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+'
    for word in danmu_list:
        word = re.sub(punctuation, '', word)
        if len(word) > 1:
            final_list.append(word)
    return date


month_list = []
list_all_files('201801', ['xml'])

csv_list = []
for month in month_list:
    final_list = []
    file_list = list_all_files(month, ['xml'])
    for file in file_list:
        re_date = get_danmu_txt(file)

    print(re_date)
    top10 = Counter(final_list).most_common()
    for data in list(top10):
        if data[1] <= 10:
            continue
        name = data[0]
        type = 'dd'
        value = data[1]
        date = re_date
        csv_list.append([name, type, value, date])

df = np.DataFrame(csv_list, columns=['name', 'type', 'value', 'date'])
df.to_csv('201801.csv', sep=',', na_rep='NA', index=None)