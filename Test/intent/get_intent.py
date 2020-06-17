# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     get_intent
   Description :
   Author :       lintt
   date：          2020/6/11
-------------------------------------------------
   Change Activity:2020/6/11:
-------------------------------------------------
"""
import pandas as pd
import requests
import xlwt
import unittest
import os
#data = pd.read_csv('../testdata/beauty_intent_522.csv',encoding='utf-8')
#print(data)

class GetResIntent:
    def get_res_intent(self,api):
        data = pd.read_csv('../testdata/beauty_intent_522.csv', encoding='utf-8')
        sentence_List = []
        intent_List = []
        judge = ''
        judge_List = []
        res_intent_List = []
        for index,item in data.iterrows():
            intent = item['intent']
            sentence = item['sentence']
            intent_List.append(intent)
            sentence_List.append(sentence)
            #api = 'http://192.168.26.105:30102/intention/v1?utterance={}&enterprise=skin&multi_intent_mode=False'
            url = api.format(sentence)
            result = requests.get(url)
            res = result.json()
            res_intent = res['data']['intent']
            res_intent_List.append(res_intent)
            judge = CommonUse.get_judge(res_intent,intent)
            judge_List.append(judge)
        #return judge_List
        data["sentence"] = sentence_List
        data["intent"] = intent_List
        data["res_intent"] = res_intent_List
        data["judge"] = judge_List
        data.to_excel('../resultdata/result_judge_0612.xls',index=False, encoding="utf-8")
        target_List = CommonUse.get_intents()
        #precision_List, recall_List, f1_List, count_r_all_List, count_p_all_List,count_rt_List = CommonUse.calculation(intent_List,res_intent_List,target_List)
        precision_List, recall_List, f1_List, count_rg_List, count_jk_List, count_same_List = CommonUse.calculation(
            intent_List, res_intent_List, target_List)
        #p_List,r_List,f1_List, count_rg_List, count_jk_List, count_same_List
        filePath = '../resultdata/result_intent_0612.xls'
        CommonUse.save_excel(filePath,target_List,precision_List,recall_List, f1_List, count_rg_List, count_jk_List, count_same_List)

        # for target in target_List:
        #     p,r,f1 = CommonUse.get_calculation(intent_List,res_intent_List,target)

            #return res_intent
            #print(res_intent)
            #intentList.append(res_intent)


class CommonUse:
    @staticmethod
    def get_judge(str1,str2):
        if str1 == str2:
            judge = 'true'
        else:
            judge = 'false'
        return judge

    @staticmethod
    def get_intents():
        intents_List = []
        data = pd.read_csv('../testdata/beauty_intent_522.csv', encoding='utf-8')
        for index, item in data.iterrows():
            if item['intent'] not in intents_List:
                intents_List.append(item['intent'])
            else:
                pass
        return intents_List

    @staticmethod
    def get_calculation(intent_list,res_intent_list,target):
        count_p = 0
        count_r = 0
        count_p_all = 0
        count_r_all = 0
        result = list(zip(intent_list,res_intent_list))
        for res in result:
            int1 = res[0]
            int2 = res[1]
            # 准确率
            if int2 == target:
                count_p_all += 1 # 接口标注数
                if int1 == int2:
                    count_p += 1
            # 召回率
            if int1 == target:
                count_r_all += 1 # 人工标注数
                if int1 == int2:
                    count_r += 1 # 一致数
        if count_p_all != 0 and count_r_all != 0:
            precision = count_p / count_p_all
            recall = count_r / count_r_all
            f1 = 2 * precision * recall / (precision + recall)
        else:
            precision = 0
            recall = 0
            f1 = 0
        print(precision)
        print(recall)
        print(f1)
        print(count_r_all)# 人工标注数
        print(count_p_all)# 接口标注数
        print(count_r)
        return precision, recall, f1,count_r_all,count_p_all,count_r

    @staticmethod
    def calculation(intent_List, res_intent_List,target_List):
        p_List = []
        r_List = []
        f1_List = []
        count_rg_List = []
        count_jk_List =[]
        count_same_List = []
        for target in target_List:
            print("************{}************".format(target))
            # 准确率、召回率、人工标注数，接口标注数，一致数
            p, r, f1, count_rg, count_jk, count_same = CommonUse.get_calculation(intent_List, res_intent_List, target)
            p_List.append(p)
            r_List.append(r)
            f1_List.append(f1)
            count_rg_List.append(count_rg)
            count_jk_List.append(count_jk)
            count_same_List.append(count_same)

        print(count_rg_List)
        print("************人工标注数************")
        print(count_jk_List)
        print("************接口标注数************")
        print(count_same_List)
        print("************一致数************")
        print(count_same_List)

        return p_List,r_List,f1_List, count_rg_List, count_jk_List, count_same_List

    @staticmethod
    def save_excel(filePath,target_List,p_List, r_List, f1_List, count_rg_List, count_jk_List, count_same_List):
        workbook = xlwt.Workbook()
        sheet1 = workbook.add_sheet('意图统计结果', cell_overwrite_ok=True)
        sheet1.write(0, 0, "意图列表")
        sheet1.write(0, 1, "人工标注数量")
        sheet1.write(0, 2, "接口结果数量")
        sheet1.write(0, 3, "一致数")
        sheet1.write(0, 4, "准确率")
        sheet1.write(0, 5, "召回率")
        sheet1.write(0, 6, "F1值")
        for i in range(0,len(target_List)):
            sheet1.write(i + 1, 0, target_List[i])
            sheet1.write(i + 1, 1, count_rg_List[i])
            sheet1.write(i + 1, 2, count_jk_List[i])
            sheet1.write(i + 1, 3, count_same_List[i])
            sheet1.write(i + 1, 4, p_List[i])
            sheet1.write(i + 1, 5, r_List[i])
            sheet1.write(i + 1, 6, f1_List[i])
        workbook.save(filePath)









if __name__ == '__main__':
    print('开始测试')
    api = 'http://192.168.26.105:30102/intention/v1?utterance={}&enterprise=skin&multi_intent_mode=False'
    #data = pd.read_csv('../testdata/beauty_intent_522.csv', encoding='utf-8')
    # res_r = GetResIntent().get_res_intent(api)
    # print(res_r)
    # intentsList = CommonUse.get_intents()
    # print(intentsList)
    # print(len(intentsList))
    res = GetResIntent()
    res.get_res_intent(api)
    print('测试结束')

