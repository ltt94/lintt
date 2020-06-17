import uuid
import json
import random
import datetime
from logger import logger
from locust import TaskSet, task, HttpLocust
from addr import addr

long_voice_list = ["18959210280_15s.WAV",
                   "18959210280_30s.WAV",
                   "18965110392_15s.WAV",
                   "18965110392_30s.WAV",
                   "万伋轩.mp3",
                   "严伟.mp3",
                   "余桂菊.mp3",
                   "刘伟伟.mp3",
                   "励梦逸.mp3",
                   "卢宇婷.mp3",
                   "卢鹏.mp3",
                   "叶志强.mp3",
                   "向陆明.mp3",
                   "吴丹.mp3",
                   "吴丹.WAV",
                   "吴佳慧.mp3",
                   "吴学晓.mp3",
                   "吴疆.mp3",
                   "吴疆包头.mp3",
                   "吴疆电话.mp3",
                   "吴芳芳.mp3",
                   "吴长春.WAV",
                   "唐金辉.mp3",
                   "季伟兵.mp3",
                   "宋云龙.mp3",
                   "宫傲.mp3",
                   "宫傲.WAV",
                   "宫傲微信声.mp3",
                   "小叶.mp3",
                   "张沈宇.mp3",
                   "张猛.mp3",
                   "彭鑫.mp3",
                   "徐家辉.mp3",
                   "徐胜伟.mp3",
                   "戴妮.mp3",
                   "戴妮.WAV",
                   "杜金斗.mp3",
                   "杜金斗微信声.mp3",
                   "杜金斗电话声.mp3",
                   "杨淮清.mp3",
                   "毛奕敏.mp3",
                   "毛奕敏.WAV",
                   "毛奕敏微信音.mp3",
                   "江莉萍.mp3",
                   "王荣均.mp3",
                   "王郭子帅.mp3",
                   "王阿龙.mp3",
                   "田野.mp3",
                   "秦汝静.mp3",
                   "胡丹玉.mp3",
                   "胡长春.mp3",
                   "胥莉丽.mp3",
                   "蒋朱红.mp3",
                   "许敏.mp3",
                   "许敏.WAV",
                   "谢佳风.mp3",
                   "邹明江.mp3",
                   "郑力乾.WAV",
                   "郑彦青.mp3",
                   "钱晖.mp3",
                   "钱辉.WAV",
                   "闫绍密.mp3",
                   "陆杨.mp3",
                   "陈佳敏.mp3",
                   "陈春煌.mp3",
                   "陈春煌.WAV",
                   "陶慧贤.mp3",
                   "韩胜杰.mp3",
                   "韩胜杰.WAV",
                   "顾金福.mp3",
                   "马俊.WAV",
                   "马骏.mp3",
                   "鲁芳芳.mp3",
                   "黄薇.mp3"]

'''
排列顺序从左至右依次为：六位数字地址码，八位数字出生日期码，三位数字顺序码和一位校验码:
1、地址码 
表示编码对象常住户口所在县(市、旗、区)的行政区域划分代码，按GB/T2260的规定执行。
2、出生日期码 
表示编码对象出生的年、月、日，按GB/T7408的规定执行，年、月、日代码之间不用分隔符。 
3、顺序码 
表示在同一地址码所标识的区域范围内，对同年、同月、同日出生的人编定的顺序号，顺序码的奇数分配给男性，偶数分配给女性。 
4、校验码计算步骤
    (1)十七位数字本体码加权求和公式 
    S = Sum(Ai * Wi), i = 0, ... , 16 ，先对前17位数字的权求和 
    Ai:表示第i位置上的身份证号码数字值(0~9) 
    Wi:7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2 （表示第i位置上的加权因子）
    (2)计算模 
    Y = mod(S, 11)
    (3)根据模，查找得到对应的校验码 
    Y: 0 1 2 3 4 5 6 7 8 9 10 
    校验码: 1 0 X 9 8 7 6 5 4 3 2
'''



def get_check_bit(num17):
    """
    获取身份证最后一位，即校验码
    :param num17: 身份证前17位字符串
    :return: 身份证最后一位
    """
    wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_code = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    zip_wi_num17 = zip(list(num17), wi)
    s = sum(int(i) * j for i, j in zip_wi_num17)
    y = s % 11
    return check_code[y]


def get_addr_code():
    """
    获取身份证前6位，即地址码
    :return: 身份证前6位
    """
    addr_index = random.randint(0, len(addr) - 1)
    return addr[addr_index]


def get_birthday(start="1900-01-01", end="2017-12-30"):
    """
    获取身份证7到14位，即出生年月日
    :param start: 出生日期合理的起始时间
    :param end: 出生日期合理的结束时间
    :return: 份证7到14位
    """
    days = (datetime.datetime.strptime(end, "%Y-%m-%d") - datetime.datetime.strptime(start, "%Y-%m-%d")).days + 1
    birthday = datetime.datetime.strptime(start, "%Y-%m-%d") + datetime.timedelta(random.randint(0, days))
    return datetime.datetime.strftime(birthday, "%Y%m%d")


def get_random_id_card(sex=1):
    """
    获取随机身份证
    :param sex: 性别，默认为男
    :return: 返回一个随机身份证
    """
    id_number, addr_name = get_addr_code()
    id_code = str(id_number) + get_birthday()
    for i in range(2):
        id_code += str(random.randint(0, 9))
    id_code += str(random.randrange(sex, 9, 2))
    id_code += get_check_bit(id_code)
    return id_code


class UserBehavior(TaskSet):
    def on_start(self):
        # 登录
        response = self.client.post("/kvp_mps/v1/login", {
            "account": "fjadmin",
            "pwd": "afd84507f0394b705272e2434e5ec8f7f46967609ff772cdeba6d5543fff3aea"
        })
        res_dict = json.loads(response.text)
        self.access_token = res_dict['access_token']
        print(self.access_token)
        self.headers = {"Authorization": self.access_token, "Content-Type": "application/x-www-form-urlencoded"}
        self.upload_headers = {"Authorization": self.access_token}
        self.file_headers = {"Authorization": self.access_token}

        ## {'code': 0, 'msg': 'success.', 'access_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50IjoiZmphZG1pbiIsImV4cCI6MTU2OTg5Nzc4MCwibGV2ZWwiOjIsIm5hbWUiOiLnpo_lu7rnnIHlhazlhbHmnLrmnoTotoXnuqfnrqHnkIblkZgiLCJvcmdhbml6YXRpb25faWQiOjQwLCJwZXJtaXNzaW9uIjoxMzEwNzF9.syU_m190FE6m6gVE3XLZ74s1mMRvwNnLTYcNgzgXZ9E'}
        print("login result: {}".format(res_dict))

    @task
    def doOrganization(self):

        organization_params = {
            "user_account": "account" + str(uuid.uuid1()),
            "name": "机构" + str(uuid.uuid1()),
            "province": "福建省",
            "city":"厦门市",
            "level":"4",
            "address":"厦门市思明区"
        }
        #wave_file = {"wave_file": open("./voice/{}".format(long_voice_list[random.randint(0, 19)]), 'rb')}
        try:
            with self.client.post("/kvp_mps/v1/management/organization",
                                               params=organization_params,
                                               catch_response=True,headers=self.headers,
                                               ) as organization_response:
                print("organization result: {}".format(organization_response.text))
                organization_res_dict = json.loads(organization_response.text)
                if organization_res_dict['code'] != 0:
                    organization_response.failure(organization_res_dict)
        except Exception as e:
            organization_response.failure(str(e))



class WebUser(HttpLocust):
    task_set = UserBehavior
    host = "http://10.0.2.191:9000"  # kvp-mps
    min_wait = 1000
    max_wait = 2000
