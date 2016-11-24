#! usr/bin/python
# coding=utf-8
"""
File Name: SplitPinyin.py
Description: Split user's input (pinyin sequence)
Date: 2016-11-12
Author: QIU HU
"""
import collections


class SplitPinyin(object):

    def __init__(self):

        self.pinyin, self.prefix = self.load_valid_pinyin()

    def load_valid_pinyin(self):
        pinyin = collections.defaultdict(int)
        pf = collections.defaultdict(int)  # prefix
        pinyin["a"] = 1
        pinyin["ai"] = 1
        pinyin["an"] = 1
        pinyin["ao"] = 1
        pinyin["ang"] = 1

        pf["b"] = 1
        pinyin["ba"] = 1
        pinyin["bai"] = 1
        pinyin["ban"] = 1
        pinyin["bang"] = 1
        pinyin["bao"] = 1
        pf["be"] = 1
        pinyin["bei"] = 1
        pinyin["ben"] = 1
        pinyin["beng"] = 1
        pinyin["bi"] = 1
        pf["bia"] = 1
        pinyin["bian"] = 1
        pinyin["biao"] = 1
        pinyin["bie"] = 1
        pinyin["bin"] = 1
        pinyin["bing"] = 1
        pinyin["bo"] = 1
        pinyin["bu"] = 1

        pf["c"] = 1
        pinyin["ca"] = 1
        pinyin["cai"] = 1
        pinyin["can"] = 1
        pinyin["cang"] = 1
        pinyin["cao"] = 1
        pinyin["ce"] = 1
        pinyin["cen"] = 1
        pinyin["ceng"] = 1
        pinyin["ci"] = 1
        pf["co"] = 1
        pf["con"] = 1
        pinyin["cong"] = 1
        pinyin["cou"] = 1
        pinyin["cu"] = 1
        pf["cua"] = 1
        pinyin["cuan"] = 1
        pinyin["cui"] = 1
        pinyin["cun"] = 1
        pinyin["cuo"] = 1

        pf["d"] = 1
        pinyin["da"] = 1
        pinyin["dai"] = 1
        pinyin["dan"] = 1
        pinyin["dang"] = 1
        pinyin["dao"] = 1
        pinyin["de"] = 1
        pinyin["dei"] = 1
        pf["den"] = 1
        pinyin["deng"] = 1
        pinyin["di"] = 1
        pinyin["dia"] = 1
        pinyin["dian"] = 1
        pinyin["diao"] = 1
        pinyin["die"] = 1
        pinyin["din"] = 1
        pinyin["ding"] = 1
        pinyin["diu"] = 1
        pf["do"] = 1
        pf["don"] = 1
        pinyin["dong"] = 1
        pinyin["dou"] = 1
        pinyin["du"] = 1
        pf["dua"] = 1
        pinyin["duan"] = 1
        pinyin["dui"] = 1
        pinyin["dun"] = 1
        pinyin["duo"] = 1

        pinyin["e"] = 1
        pinyin["ei"] = 1
        pinyin["en"] = 1
        pinyin["er"] = 1

        pf["f"] = 1
        pinyin["fa"] = 1
        pinyin["fan"] = 1
        pinyin["fang"] = 1
        pf["fe"] = 1
        pinyin["fei"] = 1
        pinyin["fen"] = 1
        pinyin["feng"] = 1
        pf["fi"] = 1
        pf["fia"] = 1
        pinyin["fiao"] = 1  # 覅
        pinyin["fo"] = 1
        pinyin["fou"] = 1
        pinyin["fu"] = 1

        pf["g"] = 1
        pinyin["ga"] = 1
        pinyin["gai"] = 1
        pinyin["gan"] = 1
        pinyin["gang"] = 1
        pinyin["gao"] = 1
        pinyin["ge"] = 1
        pinyin["gei"] = 1
        pinyin["gen"] = 1
        pinyin["geng"] = 1
        pf["go"] = 1
        pf["gon"] = 1
        pinyin["gong"] = 1
        pinyin["gou"] = 1
        pinyin["gu"] = 1
        pinyin["gua"] = 1
        pinyin["guai"] = 1
        pinyin["guan"] = 1
        pinyin["guang"] = 1
        pinyin["gui"] = 1
        pinyin["gun"] = 1
        pinyin["guo"] = 1

        pf["h"] = 1
        pinyin["ha"] = 1
        pinyin["hai"] = 1
        pinyin["han"] = 1
        pinyin["hang"] = 1
        pinyin["hao"] = 1
        pinyin["he"] = 1
        pinyin["hei"] = 1
        pinyin["hen"] = 1
        pinyin["heng"] = 1
        pf["hon"] = 1
        pinyin["hong"] = 1
        pf["ho"] = 1
        pinyin["hou"] = 1
        pinyin["hu"] = 1
        pinyin["hua"] = 1
        pinyin["huai"] = 1
        pinyin["huan"] = 1
        pinyin["huang"] = 1
        pinyin["hui"] = 1
        pinyin["hun"] = 1
        pinyin["huo"] = 1

        pf["j"] = 1
        pinyin["ji"] = 1
        pinyin["jia"] = 1
        pinyin["jian"] = 1
        pinyin["jiang"] = 1
        pinyin["jiao"] = 1
        pinyin["jie"] = 1
        pinyin["jin"] = 1
        pinyin["jing"] = 1
        pf["jio"] = 1
        pf["jion"] = 1
        pinyin["jiong"] = 1
        pinyin["jiu"] = 1
        pinyin["ju"] = 1
        pf["jua"] = 1
        pinyin["juan"] = 1
        pinyin["jue"] = 1
        pinyin["jun"] = 1

        pf["k"] = 1
        pinyin["ka"] = 1
        pinyin["kai"] = 1
        pinyin["kan"] = 1
        pinyin["kang"] = 1
        pinyin["kao"] = 1
        pinyin["ke"] = 1
        pinyin["ken"] = 1
        pinyin["keng"] = 1
        pf["ko"] = 1
        pf["kon"] = 1
        pinyin["kong"] = 1
        pinyin["kou"] = 1
        pinyin["ku"] = 1
        pinyin["kui"] = 1
        pinyin["kun"] = 1
        pinyin["kua"] = 1
        pinyin["kuai"] = 1
        pinyin["kuan"] = 1
        pinyin["kuang"] = 1
        pinyin["kuo"] = 1

        pf["l"] = 1
        pinyin["la"] = 1
        pinyin["lai"] = 1
        pinyin["lan"] = 1
        pinyin["lang"] = 1
        pinyin["lao"] = 1
        pinyin["le"] = 1
        pinyin["lei"] = 1
        pf["len"] = 1
        pinyin["leng"] = 1
        pinyin["li"] = 1
        pinyin["lia"] = 1
        pinyin["lian"] = 1
        pinyin["liang"] = 1
        pinyin["liao"] = 1
        pinyin["lie"] = 1
        pinyin["lin"] = 1
        pinyin["ling"] = 1
        pinyin["liu"] = 1
        pinyin["lo"] = 1
        pf["lon"] = 1
        pinyin["long"] = 1
        pinyin["lou"] = 1
        pinyin["lu"] = 1
        pf["lua"] = 1
        pinyin["luan"] = 1
        pinyin["lun"] = 1
        pinyin["luo"] = 1
        pinyin["lv"] = 1
        pinyin["lve"] = 1

        pf["m"] = 1
        pinyin["ma"] = 1
        pinyin["mai"] = 1
        pinyin["man"] = 1
        pinyin["mang"] = 1
        pinyin["mao"] = 1
        pinyin["me"] = 1
        pinyin["mei"] = 1
        pinyin["men"] = 1
        pinyin["meng"] = 1
        pinyin["mi"] = 1
        pf["mia"] = 1
        pinyin["mian"] = 1
        pinyin["miao"] = 1
        pinyin["mie"] = 1
        pinyin["min"] = 1
        pinyin["ming"] = 1
        pinyin["miu"] = 1
        pinyin["mo"] = 1
        pinyin["mou"] = 1
        pinyin["mu"] = 1

        pf["n"] = 1
        pinyin["na"] = 1
        pinyin["nai"] = 1
        pinyin["nan"] = 1
        pinyin["nang"] = 1
        pinyin["nao"] = 1
        pinyin["ne"] = 1
        pinyin["nei"] = 1
        pinyin["nen"] = 1
        pinyin["neng"] = 1
        pinyin["ni"] = 1
        pf["nia"] = 1
        pinyin["nian"] = 1
        pinyin["niang"] = 1
        pinyin["niao"] = 1
        pinyin["nie"] = 1
        pinyin["nin"] = 1
        pinyin["ning"] = 1
        pinyin["niu"] = 1
        pf["non"] = 1
        pf["no"] = 1
        pinyin["nong"] = 1
        pinyin["nou"] = 1
        pinyin["nu"] = 1
        pf["nua"] = 1
        pinyin["nuan"] = 1
        pinyin["nun"] = 1
        pinyin["nuo"] = 1
        pinyin["nv"] = 1
        pinyin["nve"] = 1

        pinyin["o"] = 1
        pinyin["ou"] = 1

        pf["p"] = 1          ###
        pinyin["pa"] = 1
        pinyin["pai"] = 1
        pinyin["pan"] = 1
        pinyin["pang"] = 1
        pinyin["pao"] = 1
        pinyin["pe"] = 1
        pinyin["pei"] = 1
        pinyin["pen"] = 1
        pinyin["peng"] = 1
        pinyin["pi"] = 1
        pf["pia"] = 1
        pinyin["pian"] = 1
        pinyin["piao"] = 1
        pinyin["pie"] = 1
        pinyin["pin"] = 1
        pinyin["ping"] = 1
        pinyin["po"] = 1
        pinyin["pou"] = 1
        pinyin["pu"] = 1

        pf["q"] = 1
        pinyin["qi"] = 1
        pinyin["qia"] = 1
        pinyin["qian"] = 1
        pinyin["qiang"] = 1
        pinyin["qiao"] = 1
        pinyin["qie"] = 1
        pinyin["qin"] = 1
        pinyin["qing"] = 1
        pf["qio"] = 1
        pf["qion"] = 1
        pinyin["qiong"] = 1
        pinyin["qiu"] = 1
        pinyin["qu"] = 1
        pf["qua"] = 1
        pinyin["quan"] = 1
        pinyin["que"] = 1
        pinyin["qun"] = 1

        pf["r"] = 1
        pf["ra"] = 1
        pinyin["ran"] = 1
        pinyin["rang"] = 1
        pinyin["rao"] = 1
        pinyin["re"] = 1
        pinyin["ren"] = 1
        pinyin["reng"] = 1
        pinyin["ri"] = 1
        pf["ro"] = 1
        pf["ron"] = 1
        pinyin["rong"] = 1
        pinyin["rou"] = 1
        pinyin["ru"] = 1
        pf["rua"] = 1
        pinyin["ruan"] = 1
        pinyin["rui"] = 1
        pinyin["run"] = 1
        pinyin["ruo"] = 1

        pf["s"] = 1
        pinyin["sa"] = 1
        pinyin["sai"] = 1
        pinyin["san"] = 1
        pinyin["sang"] = 1
        pinyin["sao"] = 1
        pinyin["se"] = 1
        pinyin["sen"] = 1
        pinyin["seng"] = 1
        pinyin["si"] = 1
        pf["son"] = 1
        pf["so"] = 1
        pinyin["song"] = 1
        pinyin["sou"] = 1
        pinyin["su"] = 1
        pf["sua"] = 1
        pinyin["suan"] = 1
        pinyin["sui"] = 1
        pinyin["sun"] = 1
        pinyin["suo"] = 1

        pf["t"] = 1
        pinyin["ta"] = 1
        pinyin["tai"] = 1
        pinyin["tan"] = 1
        pinyin["tang"] = 1
        pinyin["tao"] = 1
        pinyin["te"] = 1
        pinyin["tei"] = 1
        pf["ten"] = 1
        pinyin["teng"] = 1
        pinyin["ti"] = 1
        pf["tia"] = 1
        pinyin["tian"] = 1
        pinyin["tiao"] = 1
        pinyin["tie"] = 1
        pf["tin"] = 1
        pf["ton"] = 1
        pf["to"] = 1
        pinyin["ting"] = 1
        pinyin["tong"] = 1
        pinyin["tou"] = 1
        pinyin["tu"] = 1
        pf["tua"] = 1
        pinyin["tuan"] = 1
        pinyin["tui"] = 1
        pinyin["tun"] = 1
        pinyin["tuo"] = 1

        pf["w"] = 1
        pinyin["wa"] = 1
        pinyin["wai"] = 1
        pinyin["wan"] = 1
        pinyin["wang"] = 1
        pf["we"] = 1
        pinyin["wei"] = 1
        pinyin["wen"] = 1
        pinyin["weng"] = 1
        pinyin["wo"] = 1
        pinyin["wu"] = 1

        pf["x"] = 1
        pinyin["xi"] = 1
        pinyin["xia"] = 1
        pinyin["xian"] = 1
        pinyin["xiang"] = 1
        pinyin["xiao"] = 1
        pinyin["xie"] = 1
        pinyin["xin"] = 1
        pinyin["xing"] = 1
        pf["xion"] = 1
        pinyin["xiong"] = 1
        pinyin["xiu"] = 1
        pinyin["xu"] = 1
        pf["xua"] = 1
        pinyin["xuan"] = 1
        pinyin["xue"] = 1
        pinyin["xun"] = 1

        pf["y"] = 1
        pinyin["ya"] = 1
        pinyin["yan"] = 1
        pinyin["yang"] = 1
        pinyin["yao"] = 1
        pinyin["ye"] = 1
        pinyin["yi"] = 1
        pinyin["yin"] = 1
        pinyin["ying"] = 1
        pinyin["yo"] = 1
        pf["yon"] = 1
        pinyin["yong"] = 1
        pinyin["you"] = 1
        pinyin["yu"] = 1
        pf["yua"] = 1
        pinyin["yuan"] = 1
        pinyin["yue"] = 1
        pinyin["yun"] = 1

        pf["z"] = 1
        pinyin["za"] = 1
        pinyin["zai"] = 1
        pinyin["zan"] = 1
        pinyin["zang"] = 1
        pinyin["zao"] = 1
        pinyin["ze"] = 1
        pinyin["zei"] = 1
        pinyin["zen"] = 1
        pinyin["zeng"] = 1
        pinyin["zi"] = 1
        pf["zon"] = 1
        pf["zo"] = 1
        pinyin["zong"] = 1
        pinyin["zou"] = 1
        pinyin["zu"] = 1
        pf["zua"] = 1
        pinyin["zuan"] = 1
        pinyin["zui"] = 1
        pinyin["zun"] = 1
        pinyin["zuo"] = 1

        pf["ch"] = 1
        pinyin["cha"] = 1
        pinyin["chai"] = 1
        pinyin["chan"] = 1
        pinyin["chang"] = 1
        pinyin["chao"] = 1
        pinyin["che"] = 1
        pinyin["chen"] = 1
        pinyin["cheng"] = 1
        pinyin["chi"] = 1
        pf["cho"] = 1
        pf["chon"] = 1
        pinyin["chong"] = 1
        pinyin["chou"] = 1
        pinyin["chu"] = 1
        pinyin["chua"] = 1
        pinyin["chuai"] = 1
        pinyin["chuan"] = 1
        pinyin["chuang"] = 1
        pinyin["chui"] = 1
        pinyin["chun"] = 1
        pinyin["chuo"] = 1

        pf["sh"] = 1
        pinyin["sha"] = 1
        pinyin["shai"] = 1
        pinyin["shan"] = 1
        pinyin["shang"] = 1
        pinyin["shao"] = 1
        pinyin["she"] = 1
        pinyin["shei"] = 1
        pinyin["shen"] = 1
        pinyin["sheng"] = 1
        pinyin["shi"] = 1
        pf["sho"] = 1
        pinyin["shou"] = 1
        pinyin["shu"] = 1
        pinyin["shua"] = 1
        pinyin["shuai"] = 1
        pinyin["shuan"] = 1
        pinyin["shuang"] = 1
        pinyin["shui"] = 1
        pinyin["shun"] = 1
        pinyin["shuo"] = 1

        pf["zh"] = 1
        pinyin["zha"] = 1
        pinyin["zhai"] = 1
        pinyin["zhan"] = 1
        pinyin["zhang"] = 1
        pinyin["zhao"] = 1
        pinyin["zhe"] = 1
        pinyin["zhei"] = 1
        pinyin["zhen"] = 1
        pinyin["zheng"] = 1
        pinyin["zhi"] = 1
        pf["zho"] = 1
        pf["zhon"] = 1
        pinyin["zhong"] = 1
        pinyin["zhou"] = 1
        pinyin["zhu"] = 1
        pinyin["zhua"] = 1
        pinyin["zhuai"] = 1
        pinyin["zhuan"] = 1
        pinyin["zhuang"] = 1
        pinyin["zhui"] = 1
        pinyin["zhun"] = 1
        pinyin["zhuo"] = 1

        return pinyin, pf

    def split_pinyin(self, input):
        """
        Assume input is a valid pinyin sequence pre-processed.
        Split input sequence to single pinyin list
        :param input: sequence of character
        :return: list of string
        """
        two_part = False
        many_part = False
        res_list = []
        input_lis = input.split('\'')
        for idx, input in enumerate(input_lis):
            input += '$'
            length = len(input)
            tmp = ""
            i = 0
            while i < length:
                attempt = tmp + input[i]
                if attempt not in self.pinyin and attempt not in self.prefix:
                    if tmp in self.pinyin:
                        res_list.append(tmp)
                        tmp = input[i]
                    else:
                        now_idx = i
                        now_tmp = tmp
                        while len(tmp) > 0 and tmp not in self.pinyin:
                            tmp = tmp[:-1]
                            i -= 1
                        if len(tmp) == 0:
                            if idx == len(input_lis) - 1 and input[now_idx] == '$':  # 最后了
                                res_list.append(now_tmp)
                                two_part = True
                                break
                            else:
                                res_list.append(now_tmp[0])
                                i += 1
                                many_part = True

                        if many_part == False:
                            res_list.append(tmp)
                        tmp = input[i]
                else:
                    tmp = attempt
                i += 1
        if len(res_list) == 1 and res_list[0] not in self.pinyin:
            two_part = 1
        return res_list, two_part,many_part



if __name__ == '__main__':

    a = SplitPinyin()
    print(a.split_pinyin("qhdx"))
