# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       lintt
   date：          2020/6/11
-------------------------------------------------
   Change Activity:2020/6/11:
-------------------------------------------------
"""
import pandas as pd
import requests
data = pd.read_csv('../testdata/beauty_intent_522.csv',encoding='utf-8')
for index, item in data.iterrows():
    # intent = item['intent']
    sentence = item['sentence']
    api = 'http://192.168.26.105:30102/intention/v1?utterance={}&enterprise=skin&multi_intent_mode=False'
    url = api.format(sentence)
    result = requests.get(url)
    res = result.json()
    res_intent = res['data']['intent']
    print(res_intent)