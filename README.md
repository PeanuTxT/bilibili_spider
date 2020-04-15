# bilibili 弹幕爬虫

<img src="https://github.com/PeanuTxT/picture_warehouse/blob/master/bilibili_spider/bilibili.jpg" width=256 height=256 />

## 1.简易爬虫使用说明：

* ### 单视频爬取

1.运行simple_spider.exe，输入数字1并回车

2.输入要爬取的B站视频的av号后并回车，在当前目录的output文件夹下生成.xml弹幕文件

* ### 多视频爬取

1.修改av_number.txt配置文件，每行为一个视频的av号（请勿输入其他无效字符）

2.运行simple_spider.exe，输入数字2并回车

3.等待程序结束在当前目录的output文件夹下生成.xml弹幕文件

## 2.分区爬虫说明：

1.danmu_spiders/下为鬼畜分区代码文件

2.rank.csv文件为2018鬼畜区【调教x人力】完整弹幕排行

3.动态排名可视化展示：https://github.com/Jannchie/Historical-ranking-data-visualization-based-on-d3.js 作者：[@Jannchie](https://github.com/Jannchie)

注：该动态排名可视化项目可在页面中实时渲染并展示每一天的数据增加情况

4.动态排名可视化视频演示：https://www.bilibili.com/video/BV11t411876Q

5.2018鬼畜区【调教x人力】弹幕排行预览图

<img src="https://github.com/PeanuTxT/picture_warehouse/blob/master/bilibili_spider/2018_guichuzone_danmu_rank.png" width=100% height=100% />
