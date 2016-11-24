# ! usr/bin/python
# coding=utf-8
"""
File Name: PinyinTrie.py
Description: Trie for pinyin split
Date: 2016-11-12
Author: QIU HU
"""
import collections
from Queue import PriorityQueue
import pickle

if __name__ == "__main__":
    dict = pickle.load(open("pyall.tr","rb"))
    i = ""
    for k in dict:
        i = k
        print i
        for j in k:
            print j
        break




