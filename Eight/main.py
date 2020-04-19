# import json
import json

import pandas
from Seven.main import get_scores
from pandas.io.json import json_normalize


def read_json_to_df(path="/Users/weizijian/Downloads/PythonTeaching/Seven/score.txt"):
    with open(path, "r") as f:
        s = json.loads(f.read())
    df = json_normalize(s)
    return df


if __name__ == '__main__':
    lesson_df = read_json_to_df()
    # lesson_df.
