import requests
import re
import datetime
from bs4 import BeautifulSoup
from lxml import etree
from .wb import TweetItem, CommentItem, extract_weibo_content, extract_comment_content


class WeiBoCrawler:

    def __init__(self, headers=None):
        self.headers = headers
        self.base_url = "https://weibo.cn/"

    def get_first_page_weibo_by_userid(self, user_id):
        params = (
            ('page', '1'),
        )
        response = requests.get(self.base_url + str(user_id) + '/profile', headers=self.headers, params=params)
        wbs = self.parse_resp(response=response)
        return wbs

    def get_all_weibo_by_userid(self, user_id):
        params = (
            ('page', '1'),
        )
        response = requests.get(self.base_url + str(user_id) + '/profile', headers=self.headers, params=params)
        num = self.get_page_num(response=response)
        wbs = []
        for i in range(1, num + 1):
            params = (
                ('page', str(i)),
            )
            response = requests.get(self.base_url + str(user_id) + '/profile', headers=self.headers, params=params)
            wbs.extend(self.parse_resp(response=response))
        return wbs

    def get_one_comment_by_weiboid(self, weibo_id):
        url = f"{self.base_url}/comment/{weibo_id}?page=1"
        response = requests.get(url=url, headers=self.headers)
        # 评论特别多的情况下 可能有很多页
        comments = []
        num = self.get_page_num(response=response)
        if num == 1:
            comments.extend(self.parse_resp(response=response))
            return comments
        else:
            for i in range(1, num + 1):
                url = f"{self.base_url}/comment/{weibo_id}?page={str(i)}"
                response = requests.get(url, headers=self.headers)
                comments.extend(self.parse_resp(response=response))
            # comments = self.parse_comment_resp(response)
            return comments

    def get_page_num(self, response):
        """
        得到一个用户的微博有多少页
        :return: 返回页数
        """
        if response.url.endswith('page=1'):
            all_page = re.search(r'/>&nbsp;1/(\d+)页</div>', response.text)
            if all_page:
                all_page = all_page.group(1)
                all_page = int(all_page)
            return all_page

    def parse_resp(self, response):
        """
        解析一个resp结构，即requests.get/post等方法返回的resp，通过lxml解析每条微博内容、点赞数、评论数等
        :param resp: requests.get/post等方法返回的resp
        :return: items 每个item是一个TweetItem对象，包含一条微博的信息
        """
        items = []
        tree_node = etree.HTML(response.content)
        # print(tree_node)
        tweet_nodes = tree_node.xpath('//div[@class="c" and @id]')
        # print(len(tweet_nodes))
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

            items.append(tweet_item)
            # print(tweet_item.content)
        return items

    def parse_comment_resp(self, response):
        """
        解析一个评论resp结构，即requests.get/post等方法返回的resp，通过lxml解析评论内容、点赞数等
        :param resp: requests.get/post等方法返回的resp
        :return: items 每个item是一个CommentItem对象，包含一条评论的信息
        """
        items = []
        tree_node = etree.HTML(response.content)
        comment_nodes = tree_node.xpath('//div[@class="c" and contains(@id,"C_")]')
        for comment_node in comment_nodes:
            comment_user_url = comment_node.xpath('.//a[contains(@href,"/u/")]/@href')
            if not comment_user_url:
                continue
            comment_item = CommentItem()

            comment_item.weibo_id = response.url.split('/')[-1].split('?')[0]
            comment_item.comment_user_id = re.search(r'/u/(\d+)', comment_user_url[0]).group(1)
            comment_item.content = extract_comment_content(etree.tostring(comment_node, encoding='unicode'))
            comment_item._id = comment_node.xpath('./@id')[0]
            created_at_info = comment_node.xpath('.//span[@class="ct"]/text()')[0]
            like_num = comment_node.xpath('.//a[contains(text(),"赞[")]/text()')[-1]
            comment_item.like_num = int(re.search('\d+', like_num).group())
            items.append(comment_item)
        return items
