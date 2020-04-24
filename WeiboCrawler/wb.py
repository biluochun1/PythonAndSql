import requests
import re
import datetime
from bs4 import BeautifulSoup
from lxml import etree


class TweetItem():
    """Tweet information """
    _id = ""  # 微博id
    weibo_url = ""  # 微博URL
    like_num = 0  # 点赞数
    repost_num = 0  # 转发数
    comment_num = 0  # 评论数
    content = ""  # 微博内容
    user_id = ""  # 发表该微博用户的id
    tool = ""  # 发布微博的工具
    image_url = ""  # 图片
    video_url = ""  # 视频
    origin_weibo = ""  # 原始微博，只有转发的微博才有这个字段


class CommentItem():
    """
    微博评论信息
    """
    _id = ""
    comment_user_id = ""  # 评论用户的id
    content = ""  # 评论的内容
    weibo_id = ""  # 评论的微博的id
    created_at = ""  # 评论发表时间
    like_num = 0  # 点赞数


# 定义一些用于匹配微博内容的正则表达式
keyword_re = re.compile('<span class="kt">|</span>|原图|<!-- 是否进行翻译 -->|<span class="cmt">|\[组图共.张\]')
emoji_re = re.compile('<img alt="|" src="//h5\.sinaimg(.*?)/>')
white_space_re = re.compile('<br />')
div_re = re.compile('</div>|<div>')
image_re = re.compile('<img(.*?)/>')
url_re = re.compile('<a href=(.*?)>|</a>')


def extract_comment_content(comment_html):
    """
    工具函数 解析一个微博评论html内容，转发和原创两种类型
    :param weibo_html: 传入单条微博评论的div
    :return: 返回解析出来的微博内容
    """
    s = comment_html
    if 'class="ctt">' in s:
        s = s.split('class="ctt">', maxsplit=1)[1]
    s = s.split('举报', maxsplit=1)[0]
    s = emoji_re.sub('', s)
    s = keyword_re.sub('', s)
    s = url_re.sub('', s)
    s = div_re.sub('', s)
    s = image_re.sub('', s)
    s = white_space_re.sub(' ', s)
    s = s.replace('\xa0', '')
    s = s.strip(':')
    s = s.strip()
    return s


def extract_weibo_content(weibo_html):
    """
    工具函数 解析一个微博html内容，转发和原创两种类型
    :param weibo_html: 传入单条微博的div
    :return: 返回解析出来的微博内容
    """
    s = weibo_html
    if 'class="ctt">' in s:
        s = s.split('class="ctt">', maxsplit=1)[1]
    s = emoji_re.sub('', s)
    s = url_re.sub('', s)
    s = div_re.sub('', s)
    s = image_re.sub('', s)
    if '<span class="ct">' in s:
        s = s.split('<span class="ct">')[0]
    splits = s.split('赞[')
    if len(splits) == 2:
        s = splits[0]
    if len(splits) == 3:
        origin_text = splits[0]
        retweet_text = splits[1].split('转发理由:')[1]
        s = origin_text + '转发理由:' + retweet_text
    s = white_space_re.sub(' ', s)
    s = keyword_re.sub('', s)
    s = s.replace('\xa0', '')
    s = s.strip(':')
    s = s.strip()
    return s
