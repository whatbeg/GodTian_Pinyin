#! usr/bin/python
# coding=utf-8
"""
File Name: GodTian_Pinyin.py
Description: GodTian_Pinyin main function, with veterbi algorithm
Date: 2016-11-13
Author: QIU HU
"""

import cPickle as pickle
from Priotityset import PrioritySet
import SplitPinyin as sp
import re
import os
from pypinyin import lazy_pinyin
MIN_PROB = -500.0  # after log
import time
import collections


def trans_a_b(trans, a, b):
    if a in trans:
        if b in trans[a]:
            return max(trans[a][b], MIN_PROB)
    return MIN_PROB


def Pi_state(Pi, state):
    if state in Pi:
        return max(Pi[state], MIN_PROB)
    else:
        return MIN_PROB


def emit_a_b(emit, a, b):
    if a in emit:
        if b in emit[a]:
            return max(emit[a][b], MIN_PROB)
    return MIN_PROB

def emit_a_b_many(emit,hanyu,pinyin):
    if hanyu in emit:
        judge = 0
        max_pinyin = -9999
        max_i = -1
        for val in emit[hanyu]:
            for i in range(0,len(val)):
                if pinyin == val[:i]:
                    judge = 1
                    if emit[hanyu][val] > max_pinyin:
                        max_pinyin = emit[hanyu][val]
        if judge == 1:
            return max(max_pinyin, MIN_PROB)
    return MIN_PROB

def serch_in_dict(pyl,dict):
    res = ""
    ii = 15
    for i in pyl:
        if i!=" ":
            res += i
    res += "  "
    if res in dict:
        list =  PrioritySet(15)
        s = sorted(dict[res].iteritems(), key=lambda d: d[1], reverse=True)
        mm = 0
        for j in s:
            list1 = []
            for o in j[0]:
                list1.append(o)
            list.put(j[1],list1)
            mm += 1
        return list
    else:
        return []


class GodTian_Pinyin(object):

    def __init__(self):
        self.Pi = pickle.load(open('Pi.mat', 'rb'))
        self.emit = pickle.load(open('emit.mat', 'rb'))
        self.trans = pickle.load(open('trans.mat', 'rb'))
        self.py2ch = pickle.load(open('py2ch.mat', 'rb'))
        self.pt = pickle.load(open('pyintrie.tr', 'rb'))
        self.dict = pickle.load(open("pyall.tr", "rb"))

        self.pat = re.compile("\d*\.*\d+")
        if "cache.cc" in os.listdir(os.curdir):
            self.cache = pickle.load(open('cache.cc', 'rb'))
        else:
            self.cache = {}
        self.memo = collections.defaultdict(lambda: collections.defaultdict(PrioritySet))
        if "memo.mm" in os.listdir(os.curdir):
            memo = pickle.load(open('memo.mm', 'rb'))
            for key1 in memo:
                for key2 in memo[key1]:
                    self.memo[key1][key2] = memo[key1][key2]
        self.sp = sp.SplitPinyin()

    def newviterbi(self, pylist, top=15):
        V = [{} for _ in range(2)]
        t = 0
        idx = 0
        cur_obs = pylist[t]  #

        topp =100

        prefix_ans = {}
        self.pt.get_totalwords_of_prefix(self.pt.root,pylist[0], prefix_ans)
        sorted_pf_ans = sorted(prefix_ans.items(), key=lambda x: x[1], reverse=True)
        words = [hz_freq[0] for hz_freq in sorted_pf_ans[:topp]]
        cur_cand_states = words  # 可能状态
        for i in cur_cand_states:
            print(i)

        prepyseq = "".join(pylist[:-1])
        pylislen = len(pylist)
        START = 1

        for state in cur_cand_states:
            tao = Pi_state(self.Pi, state) + emit_a_b_many(self.emit, state, cur_obs)
            _path = [state]
            V[0].setdefault(state, PrioritySet(top))
            V[0][state] = PrioritySet(top)
            V[0][state].put(tao, _path)

        for t in range(START, pylislen):
            cur_obs = pylist[t]
            print "---------------"
            print pylist,t,pylist[t]
            idx = t % 2
            V[idx] = {}
            prev_states = cur_cand_states

            prefix_ans = {}
            self.pt.get_totalwords_of_prefix(self.pt.root, cur_obs, prefix_ans)
            sorted_pf_ans = sorted(prefix_ans.items(), key=lambda x: x[1], reverse=True)
            words = [hz_freq[0] for hz_freq in sorted_pf_ans[:topp]]
            cur_cand_states = words  # 可能状态
            for i in cur_cand_states:
                print(i)

            for state in cur_cand_states:  # 此时状态
                V[idx].setdefault(state, PrioritySet(top))
                for prev in prev_states:  # 前一个状态
                    for cand in V[(idx + 1) % 2][prev]:  # 前一个状态为prev, cand的概率
                        tao = trans_a_b(self.trans, prev, state) + emit_a_b_many(self.emit, state, cur_obs)
                        new_tao = tao + cand.score
                        _p = cand.path + [state]
                        V[idx][state].put(new_tao, _p)
        results = PrioritySet(top)
        for last_state in V[idx]:
            for item in V[idx][last_state]:
                results.put(item.score, item.path)
        results = [item for item in results]
        return sorted(results, key=lambda x: x.score, reverse=True)

    def viterbi(self, pylist, top=15, words=[]):

        V = [{} for _ in range(2)]
        t = 0
        idx = 0
        cur_obs = pylist[t]  # 现在的观察
        cur_cand_states = self.py2ch[cur_obs]  # 可能状态
        prepyseq = "".join(pylist[:-1])
        pylislen = len(pylist)
        START = 1
        TAG = 0
        if prepyseq in self.memo:
            TAG = 1
            start = time.time()
            T = pylislen-1   # Last one's index
            cur_cand_states = []
            for state in self.memo[prepyseq]:
                cur_cand_states.append(state)
                V[pylislen % 2][state] = self.memo[prepyseq][state]
            START = T
            end = time.time()
            print("READ MEMORY COST {}".format(end-start))
        else:
            for state in cur_cand_states:
                tao = Pi_state(self.Pi, state) + emit_a_b(self.emit, state, cur_obs)
                _path = [state]
                V[0].setdefault(state, PrioritySet(top))
                V[0][state] = PrioritySet(top)
                V[0][state].put(tao, _path)
        # Iteration T > 0
        start = time.time()
        for t in range(START, pylislen):
            cur_obs = pylist[t]
            idx = t % 2
            V[idx] = {}
            prev_states = cur_cand_states
            if not words:
                cur_cand_states = self.py2ch[cur_obs]
            else:
                cur_cand_states = words
            for state in cur_cand_states:  # 此时状态
                V[idx].setdefault(state, PrioritySet(top))
                for prev in prev_states:   # 前一个状态
                    for cand in V[(idx+1) % 2][prev]:  # 前一个状态为prev, cand的概率
                        tao = trans_a_b(self.trans, prev, state) + emit_a_b(self.emit, state, cur_obs)
                        new_tao = tao + cand.score
                        _p = cand.path + [state]
                        V[idx][state].put(new_tao, _p)
        end = time.time()
        print("RUN VITERBI COST： {}".format(end-start))
        start = time.time()
        results = PrioritySet(top)
        for last_state in V[idx]:
            self.memo["".join(pylist)][last_state] = V[idx][last_state]  # 记住拼音串所有最后状态的Priority集
            for item in V[idx][last_state]:
                results.put(item.score, item.path)
        results = [item for item in results]
        end = time.time()
        print("LAST PROCESSING: {}".format(end-start))
        return sorted(results, key=lambda x: x.score, reverse=True)

    def save_memo_and_cache(self):

        pickle.dump(self.cache, open('cache.cc', 'wb'), True)
        pickle.dump(dict(self.memo), open('memo.mm', 'wb'), True)

    def handle_current_input(self, input, topv=15, topp=15):
        input = input.lower()
        if self.pat.findall(input):   # 全数字，直接返回
            return input
        pyl, two_part,may_parts = self.sp.split_pinyin(input)
        print(pyl, two_part,may_parts)
        if two_part == True and may_parts == False:
            prefix_ans = {}
            start = time.time()
            self.pt.get_totalwords_of_prefix(self.pt.root, pyl[-1], prefix_ans)
            sorted_pf_ans = sorted(prefix_ans.items(), key=lambda x: x[1], reverse=True)
            end = time.time()
            print("GET PREFIX COST: {}".format(end-start))
            words = [hz_freq[0] for hz_freq in sorted_pf_ans[:topp]]
            # -------------------------
            best_viterbi_ans = []
            pinyins = map(lambda x: lazy_pinyin(x)[0], words)
            viterbi_ans = []
            start = time.time()
            for _, py in enumerate(pinyins):
                pyl[-1] = py
                viterbi_ans = self.viterbi(pyl, topv, [words[_]])  # self.momo["".join(pyl[:-1]][state...] =
            end = time.time()
            print("VITERBI COST: {}".format(end-start))
            best_viterbi_ans.extend(viterbi_ans)
            return best_viterbi_ans, two_part
        elif may_parts:
            new_viterbi_ans = serch_in_dict(pyl,self.dict)
            print new_viterbi_ans
            if new_viterbi_ans ==[]:
               new_viterbi_ans = self.newviterbi(pyl, topv)
            return new_viterbi_ans,two_part
        else:
            viterbi_ans = self.viterbi(pyl, topv, [])
            print viterbi_ans
            return viterbi_ans, two_part




# if __name__ == '__main__':
#
#     a = sp.SplitPinyin()
#     godtian = GodTian_Pinyin()
#
#     while True:
#         input2 = input("input: ")
#         if input2 in ['Q', 'q']:
#             break
#         res1, two_part = godtian.handle_current_input(input2, 100, 100)
#         for _ in range(0, min(len(res1), 10)):
#             r = res1[_]
#             for i in r.path:
#                 print (i)
#             print("")


