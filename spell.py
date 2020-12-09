import html
import json

import requests
from bs4 import BeautifulSoup


def spell_check(text: str, is_weak: bool = True):
    cookies = {
        "ruleMode": "weak" if is_weak else "strong"
    }

    data = {"text1": text.replace("\n", "\n ", len(text))}

    res = requests.post("http://speller.cs.pusan.ac.kr/results", cookies=cookies, data=data)
    soup = BeautifulSoup(res.text, "html.parser")

    if "맞춤법과" in str(soup.select_one("#tdBody")).split('\n')[0]:
        return []

    resArr = str(soup.find_all("script")[2]).split('\n')[2]
    resArr = json.loads(resArr[8:-2])

    arr = []

    for i in resArr[0]["errInfo"]:
        tempDict = {"orgStr": i["orgStr"], "help": html.unescape(i["help"]).replace("<br/>", "\n"),
                    "candWord": to_array(str(i["candWord"]).split('|'))}

        arr.append(tempDict)

    return arr


def to_array(texts: list[str]):
    arr = []

    for text in texts:
        arr.append(text)

    return arr
