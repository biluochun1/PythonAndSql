import requests
from bs4 import BeautifulSoup

url = "http://www.baidu.com/s"

keyword = "test"

params = (
    ('ie', ['utf-8', 'utf-8']),
    ('mod', '1'),
    ('isbd', '1'),
    ('isid', '534306A8A1880189'),
    ('f', '8'),
    ('rsv_bp', '1'),
    ('rsv_idx', '1'),
    ('tn', 'baidu'),
    ('wd', 'test'),
    ('oq', 'test'),
    ('rsv_pq', 'db10cd5f0005430b'),
    ('rsv_t', '5b65xDkvaAOvwP2MCwhD9AOal03iMBGy4f6znMW2uP+SMrkMQO0lOo1U/sQ'),
    ('rqlang', 'cn'),
    ('rsv_enter', '1'),
    ('rsv_dl', 'tb'),
    ('rsv_sug3', '1'),
    ('rsv_sug1', '1'),
    ('rsv_sug7', '100'),
    ('rsv_sug2', '0'),
    ('inputT', '8'),
    ('rsv_sug4', '1055'),
    ('rsv_sug', '1'),
    ('bs', 'test'),
    ('rsv_sid', 'undefined'),
    ('_ss', '1'),
    ('clist', ''),
    ('hsug', ''),
    ('f4s', '1'),
    ('csor', '4'),
    ('_cr1', '31206'),
)
resp = requests.get(url=url,params=params)

html = resp.text

soup = BeautifulSoup(html,"html.parser")

l1 = soup.find_all('a')

for e in l1:
    print(e.contents)
