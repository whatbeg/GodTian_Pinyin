#! usr/bin/python
# coding=utf-8
"""
File Name: TrainMatrix.py
Description: Train three Matrix A, B, Pi from Corpus.
Date: 2016-11-13
Author: QIU HU
"""

from pypinyin import lazy_pinyin, NORMAL
import cPickle as pickle
import collections
from math import log
import os
import PinyinTrie


def isChinese(c):
    return u'\u4e00' <= c <= u'\u9fff' or c == u'〇'


def isChineseString(s):
    return any(u'\u4e00' <= c <= u'\u9fff' or c == u'〇' for c in s)


def no_pinyin(ch):
    return ' '


def train(Pi_in, trans_in, emit_in, py2chinese_in, pyintrie, dir_name):

    trans = collections.defaultdict(lambda: collections.defaultdict(float))  # A
    emit = collections.defaultdict(lambda: collections.defaultdict(float))  # B
    py2chinese = collections.defaultdict(lambda: collections.defaultdict(float))  # pinyin to chinese
    Pi = collections.defaultdict(float)  # Pi
    # 转化为defaultdict
    for key in Pi_in:
        Pi[key] = Pi_in[key]

    for key in trans_in:
        for sub_key in trans_in[key]:
            trans[key][sub_key] = trans_in[key][sub_key]

    for key in emit_in:
        for sub_key in emit_in[key]:
            emit[key][sub_key] = emit_in[key][sub_key]

    for key in py2chinese_in:
        for sub_key in py2chinese_in[key]:
            py2chinese[key][sub_key] = py2chinese_in[key][sub_key]
    print("Converted to defaultdict~")
    try:
        corpus_list = os.listdir(dir_name)
        print(corpus_list)
        for corpus in corpus_list:
            with open(dir_name + '\\' + corpus) as f:
                line_id = 0
                for line in f.readlines():
                    line_id += 1
                    if line_id % 100000 == 0:
                        print("{} -> Line {}".format(corpus, line_id))
                    if len(line.strip()) < 2:    # 长度小于等于1
                        continue
                    if not isinstance(line, unicode):    # 转为unicode
                        line = line.decode('utf8')
                    if not isChineseString(line.strip()):  # 一个汉字也没有
                        continue
                    char_list = [ch if isChinese(ch) else ' ' for ch in line.strip()]
                    sub_sentences = []
                    subs = ""
                    first = True
                    for _ in range(len(char_list)):
                        if first and char_list[_] != ' ':
                            first = False
                            subs += char_list[_]
                        elif first and char_list[_] == ' ':
                            continue
                        elif not first and char_list[_] != ' ':
                            subs += char_list[_]
                        else:
                            if len(subs) > 0:
                                sub_sentences.append(subs)
                            subs = ""
                            first = True
                    if len(subs) > 0:
                        sub_sentences.append(subs)
                    # -------------------------------
                    for sen in sub_sentences:
                        py_list = lazy_pinyin(sen, style=NORMAL, errors=no_pinyin)

                        # 初始频率
                        Pi[sen[0]] += 1

                        # 转移概率
                        for i in range(len(sen)-1):
                            if sen[i] != ' ' and sen[i+1] != ' ':
                                trans[sen[i]][sen[i+1]] += 1

                        # 输出概率
                        for i in range(len(sen)):
                            if sen[i] != ' ' and py_list[i] != ' ':
                                emit[sen[i]][py_list[i]] += 1
                                py2chinese[py_list[i]][sen[i]] += 1
                                pyintrie.add(py_list[i], sen[i])   # add in trie
                                # print(py_list[i], sen[i])
    finally:

        # # 存储频率
        # file_list = ["Pi.freq", "trans.freq", "emit.freq", "py2ch.freq"]
        # object = [dict(Pi), dict(trans), dict(emit), dict(py2chinese)]
        # for i in range(len(file_list)):
        #     with open(file_list[i], 'wb') as fout:
        #         pickle.dump(object[i], fout, True)
        #
        # # Pi 频率到概率
        # count = 0.0
        # for start in Pi:
        #     count += Pi[start]
        # for start in Pi:
        #     Pi[start] = log(Pi[start] / count)
        #
        # # A 频率到概率
        # for start in trans:
        #     count = 0.0
        #     for end in trans[start]:
        #         count += trans[start][end]
        #     for end in trans[start]:
        #         trans[start][end] = log(trans[start][end] / count)
        #
        # # B 频率到概率
        # for start in emit:
        #     count = 0.0
        #     for end in emit[start]:
        #         count += emit[start][end]
        #     for end in emit[start]:
        #         emit[start][end] = log(emit[start][end] / count)
        #
        # # 拼音转汉字 频率到概率
        # for start in py2chinese:
        #     count = 0.0
        #     for end in py2chinese[start]:
        #         count += py2chinese[start][end]
        #     for end in py2chinese[start]:
        #         py2chinese[start][end] = log(py2chinese[start][end] / count)
        #
        # # 存储概率
        # file_list = ["Pi.mat", "trans.mat", "emit.mat", "py2ch.mat"]
        # object = [dict(Pi), dict(trans), dict(emit), dict(py2chinese)]
        # for i in range(len(file_list)):
        #     with open(file_list[i], 'wb') as fout:
        #         pickle.dump(object[i], fout, True)

        pickle.dump(pyintrie, open('pyintrie.tr', 'wb'), True)

    return Pi, trans, emit, py2chinese, pyintrie


def first_train():
    trans = collections.defaultdict(lambda: collections.defaultdict(float))  # A
    emit = collections.defaultdict(lambda: collections.defaultdict(float))   # B
    py2chinese = collections.defaultdict(lambda: collections.defaultdict(float))  # pinyin to chinese
    Pi = collections.defaultdict(float)     # Pi
    pyintrie = PinyinTrie.PinyinTrie()
    dir_name = os.getcwd() + '\\SogouQ'
    return train(Pi, trans, emit, py2chinese, pyintrie, dir_name)




'''
def train2Test(emit_in, py2chinese_in):
    emit_in = pickle.load(open('emit.freq', 'rb'))
    py2chinese_in = pickle.load(open('py2ch.freq', 'rb'))

    emit = collections.defaultdict(lambda: collections.defaultdict(float))  # B
    py2chinese = collections.defaultdict(lambda: collections.defaultdict(float))  # pinyin to chinese
    # 转化为defaultdict

    for key in emit_in:
        for sub_key in emit_in[key]:
            emit[key][sub_key] = emit_in[key][sub_key]

    for key in py2chinese_in:
        for sub_key in py2chinese_in[key]:
            py2chinese[key][sub_key] = py2chinese_in[key][sub_key]

    py2chinese2 = collections.defaultdict(lambda: collections.defaultdict(float))  # pinyin to chinese

    for py in py2chinese:
        for hanzi in py2chinese[py]:
            py2chinese2.setdefault(py[0],{})
            py2chinese2[py[0]].setdefault(hanzi,0)
            py2chinese2[py[0]][hanzi] += 1'''


def incremental_training(dir_name=os.getcwd() + '\\PLUS'):

    Pi = pickle.load(open('Pi.freq', 'rb'))
    trans = pickle.load(open('trans.freq', 'rb'))
    emit = pickle.load(open('emit.freq', 'rb'))
    py2chinese = pickle.load(open('py2ch.freq', 'rb'))
    pyintrie = pickle.load(open('pyintrie.tr', 'rb'))
    return train(Pi, trans, emit, py2chinese, pyintrie, dir_name)

def train_new():
    fopen = open("dictword","rb")
    py_dict = {}
    for line in fopen:
        line = line.decode("utf-8")

        line = line.split(" ")
        if len(line)>1:
            line1 = line[0]
            freq = line[1]
            py_list = lazy_pinyin(line, style=NORMAL, errors=no_pinyin)
            res = ""
            for pyl in py_list:
                res += pyl[0][0]
            res = res
            py_dict.setdefault(res,{})
            py_dict[res].setdefault(line1,0)
            py_dict[res][line1] += int(freq)

        #py_dict.setdefault(py_res,{})
        #py_dict[py_res].append(line)

    pickle.dump(py_dict, open('pyall.tr', 'wb'), True)


if __name__ == '__main__':

    #Pi, trans, emit, py2ch, pyintrie = first_train()
    train_new()
    # Pi, trans, emit, py2ch = incremental_training()
    # print("Training Done~")
    # Pi = pickle.load(open('Pi.mat', 'rb'))
    # emit = pickle.load(open('emit.mat', 'rb'))
    # trans = pickle.load(open('trans.mat', 'rb'))
    # print(emit[u'尼'])
    # print(emit[u'你'])
    # print(trans[u'你'][u'好'])
    # s = trans[u'你']
    # print(type(s))
    # t = sorted(s.items(), key=lambda x: x[1], reverse=True)
    # for r in t[:10]:
    #     print r[0],
    #     print r[1]
    # print(Pi[u'你'])
    # pyintrie = pickle.load(open('pyintrie.tr', 'rb'))
    #pyintrie.display_trie()

