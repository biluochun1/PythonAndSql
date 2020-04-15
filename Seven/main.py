import requests
import json

cookies = {
    'selectionBar': '125803405',
    'JSESSIONID': 'dcbmd1IgO0yEM_-bzg_fx',
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate',
    'Host': '202.115.47.141',
    'Origin': 'http://202.115.47.141',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15',
    'Connection': 'keep-alive',
    'Referer': 'http://202.115.47.141/student/integratedQuery/scoreQuery/allTermScores/index',
    'Content-Length': '40',
    'Proxy-Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest',
}

scores_dict_list = []


def get_scores():
    data = {
        'zxjxjhh': '',
        'kch': '',
        'kcm': '',
        'pageNum': '1',
        'pageSize': '67'
    }

    response = requests.post('http://202.115.47.141/student/integratedQuery/scoreQuery/allTermScores/data',
                             headers=headers,
                             cookies=cookies, data=data)

    scores = response.json()

    scores_list = scores["list"]["records"]

    for score in scores_list:
        scores_dict_list.append({
            "name": score[12],
            "score": score[8],
            "xuefen": score[13],
            "is_need": True if '必' in score[15] else False,
            "is_xingshi": True if 'Situation' in score[12] else False
        })
        print(score)

    with open("score.txt", "w", encoding="utf-8") as fw:
        fw.write(json.dumps(scores_dict_list))


def get_max_score():
    lesson = []
    max_score = 0
    with open("score.txt", "r") as f:
        s = json.loads(f.read())
        for e in s:
            if e['score'] >= max_score:
                max_score = e["score"]

        for e in s:
            if e["score"] == max_score:
                lesson.append(e)
    return lesson


def get_max_score_zip():
    with open("score.txt", "r") as f:
        s = json.loads(f.read())
        s = sorted(s, key=lambda e: e["score"], reverse=True)
    return s

def average_score():
    with open("score.txt", "r") as f:
        s = json.loads(f.read())



if __name__ == '__main__':
    max_score_lesson = get_max_score_zip()
    print(max_score_lesson)
