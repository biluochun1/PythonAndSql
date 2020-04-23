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


headers = {
    'authority': 'weibo.cn',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'ALF=1590252555; SCF=AuyBnr4HvZH7JQCybmP3ZH_XVlXr6iqelzsV4fUOTSjWn7c8h6LY526RZu3L5SsE3McwvO6lmb8-ddxAkFcrAXg.; SUB=_2A25zpbfGDeRhGeNH7VIZ8i7JyT6IHXVRadmOrDV6PUJbktAKLUHAkW1NSo5mARRmBB79AgUFZBvwuLgdPBg7w8HJ; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWnY-0qw8K7UDJ04PJPHz815JpX5K-hUgL.Fo-4So5Reo5feoz2dJLoI0qLxKBLB.zL122LxK-LBKBLBK.LxKBLBonL12BLxK-L1h2L1-2LxKBLB.2LB.2LxKBLB.2L1hqt; SUHB=0YhR8lMDIpcU89; SSOLoginState=1587660694; _T_WM=a0ed342bd98a23348c5c437a41579d98',
}

params = (
    ('page', '1'),
)
base_url = "https://weibo.cn/"
response = requests.get('https://weibo.cn/5225912372/profile', headers=headers, params=params)


# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://weibo.cn/5225912372/profile?page=1', headers=headers)

def get_page_num(response):
    if response.url.endswith('page=1'):
        all_page = re.search(r'/>&nbsp;1/(\d+)页</div>', response.text)
        if all_page:
            all_page = all_page.group(1)
            all_page = int(all_page)
        return all_page


keyword_re = re.compile('<span class="kt">|</span>|原图|<!-- 是否进行翻译 -->|<span class="cmt">|\[组图共.张\]')
emoji_re = re.compile('<img alt="|" src="//h5\.sinaimg(.*?)/>')
white_space_re = re.compile('<br />')
div_re = re.compile('</div>|<div>')
image_re = re.compile('<img(.*?)/>')
url_re = re.compile('<a href=(.*?)>|</a>')


def extract_weibo_content(weibo_html):
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


soup = BeautifulSoup(response.text, 'html.parser')


# divs = soup.find_all("div", class_="c", id=re.compile("M*"))

# print(len(divs))
#
# for div in divs:
#     print(div.div.get_text())
def parse_resp(resp):
    tree_node = etree.HTML(resp.content)
    # print(tree_node)
    tweet_nodes = tree_node.xpath('//div[@class="c" and @id]')
    print(len(tweet_nodes))
    for tweet_node in tweet_nodes:
        tweet_item = TweetItem()
        tweet_repost_url = tweet_node.xpath('.//a[contains(text(),"转发[")]/@href')[0]
        user_tweet_id = re.search(r'/repost/(.*?)\?uid=(\d+)', tweet_repost_url)
        tweet_item.weibo_url = 'https://weibo.com/{}/{}'.format(user_tweet_id.group(2),
                                                                user_tweet_id.group(1))
        tweet_item.user_id = user_tweet_id.group(2)
        tweet_item._id = user_tweet_id.group(1)

        like_num = tweet_node.xpath('.//a[contains(text(),"赞[")]/text()')[-1]
        tweet_item.like_num = int(re.search('\d+', like_num).group())

        repost_num = tweet_node.xpath('.//a[contains(text(),"转发[")]/text()')[-1]
        tweet_item.repost_num = int(re.search('\d+', repost_num).group())

        comment_num = tweet_node.xpath(
            './/a[contains(text(),"评论[") and not(contains(text(),"原文"))]/text()')[-1]
        tweet_item.comment_num = int(re.search('\d+', comment_num).group())

        images = tweet_node.xpath('.//img[@alt="图片"]/@src')
        if images:
            tweet_item.image_url = images

        videos = tweet_node.xpath('.//a[contains(@href,"https://m.weibo.cn/s/video/show?object_id=")]/@href')
        if videos:
            tweet_item.video_url = videos
        all_content_link = tweet_node.xpath('.//a[text()="全文" and contains(@href,"ckAll=1")]')
        if all_content_link:
            all_content_url = "https://weibo.cn" + all_content_link[0].xpath('./@href')[0]
            tweet_item.content = all_content_url
        else:
            tweet_html = etree.tostring(tweet_node, encoding='unicode')
            tweet_item.content = extract_weibo_content(tweet_html)

        print(tweet_item.content)


parse_resp(response)
