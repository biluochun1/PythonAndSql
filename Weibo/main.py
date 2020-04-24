from Weibo.crawler import WeiBoCrawler
import time
import requests

if __name__ == '__main__':
    headers = {}
    c = WeiBoCrawler(headers=headers)



# 1、拿到第一页微博，统计微博数量
# 2、每条微博的评论数，并自定义一种比较友好的方式保存到文件里面
# 3、统计谁评论的最多
# 4、保存第一微博的图片
# 5、统计转发微博多少，原创微博有多少
