import requests  # 一个用来请求的包
from bs4 import BeautifulSoup  # 用来解析html的一把枪

url = " https://www.pwccn.com/zh/careers/students/internship.html"  # 请求链接

resp = requests.get(url=url)  # 发起一个请求，收到回复

html_doc = resp.content.decode("utf-8")  # 将 resp 以 utf-8 的编码格式做成字符串给  html_doc

soup = BeautifulSoup(html_doc, 'html.parser')  # 使用html.parser来 解析 html

# print(soup.prettify())

find_list = soup.find_all("div", class_="text-component")

p_list = []
for e in find_list:
    if e is not None:
        e_soup = BeautifulSoup(str(e), 'html.parser')
        p_list.append(e_soup.find_all("p"))

p2_list = []
for e in p_list:
    if len(e) != 0:
        for s in e:
            p2_list.append(s)

# print(p2_list)
res = []
for e in p2_list:
    if "<b>" in str(e) or "class" in str(e) or "href" in str(e):
        continue
    else:
        res.append(str(e)[3:-4])

with open("res.txt", "w") as fw:
    for e in res:
        fw.write(e + "\n")
