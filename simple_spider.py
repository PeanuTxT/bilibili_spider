# -*- coding:utf-8 -*-

import requests
import time
import re
import os


'''
函数功能：获取弹幕文件的xml地址
参数：
    av_num：视频av号list
返回：
    无
'''
def get_xml_file(av_list):
    count = 1

    for av_num in av_list:
        url = 'https://www.bilibili.com/video/av' + av_num
        headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063' }
        html_code = requests.get(url, headers=headers).text

        # 正则匹配cid编号, 视频标题
        if not re.match(f'.*"cid=(\d+)&aid={av_num}',html_code):
            print(f'[{count}] not found')
            continue
        cid_num = re.match(f'.*"cid=(\d+)&aid={av_num}',html_code).group(1)
        title = re.match(f'.*"title":"(.*)","pubdate"', html_code).group(1)
        xml_url = 'http://comment.bilibili.com/' + cid_num + '.xml'
        xml_data = str(requests.get(xml_url, headers=headers).content, encoding = "utf-8")

        # 格式化xml文件
        xml_format(av_num, xml_data)
        print(f'[{count}] {title} done')
        count += 1
        time.sleep(0.5)


'''
函数功能：格式化xml弹幕文件
参数：
    av_num：视频av号
    xml_data：需要格式化的xml的字符串
返回：
    无
'''
def xml_format(av_num, xml_data):

    # 正则匹配各级标签
    head = re.match('(<\?xml.+?>)',xml_data).group(1)
    tag_i = re.findall('</*i>',xml_data)
    danmu_list = re.findall('<.*?>.*?</.*?>',xml_data)
    body = ''

    # 对标签进行换行和缩进
    for i,tag in enumerate(danmu_list):
        if i == 0:
            body += '\n\t' + tag.replace(head + tag_i[0], '') + '\n\t'
        elif i == len(danmu_list) - 1:
            body += tag + '\n'
        else:
            body += tag + '\n\t'

    # 创建输出文件夹
    if not os.path.isdir('output'):
        os.mkdir('output')

    # 输出格式化后的结果
    result = head + '\n' + tag_i[0] + body + tag_i[1]
    with open(f'output/{av_num}.xml', 'w', encoding = "utf-8") as f:
        f.write(result)


if __name__ == '__main__':
    input_mode = input('==选择爬取模式==\n 1.单视频爬取\n 2.多视频爬取\n=============\n选择模式：')

    print('=============')
    if input_mode == '1':
        av_list = [input('输入视频av号：\n')]
        print('=============\n')
    elif input_mode == '2':
        with open('av_number.txt') as f:
            av_list = [x.replace('\n', '') for x in f.readlines()]

    get_xml_file(av_list)
    print('=============\n')
    print(u'弹幕爬取完成...')
    print(u'2秒后自动退出程序...')
    time.sleep(2)




