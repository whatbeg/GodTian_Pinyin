#! usr/bin/python
# coding=utf-8
"""
File Name: PinyinTrie.py
Description: Trie for pinyin split
Date: 2016-11-12
Author: QIU HU
"""
from Queue import PriorityQueue
import pickle as pickle


class HZ(object):
    def __init__(self, hanzi=u"", freq=0):
        self.hanzi = hanzi
        self.freq = freq

    def __cmp__(self, other):
        return cmp(self.freq, other.freq)


class Node(object):
    def __init__(self):
        self.v = {}    # ("腾", 1), ("疼", 2)
        self.child = {}


class PinyinTrie(object):
    def __init__(self):
        self.root = Node()

    def add(self, pyin, hanzi):
        # word must be a lower-case string
        cur_node = self.root
        for ch in pyin:
            if ch not in cur_node.child:
                child = Node()
                cur_node.child[ch] = child
                cur_node = child
            else:
                cur_node = cur_node.child[ch]
        if hanzi not in cur_node.v:
            cur_node.v[hanzi] = 1
        else:
            cur_node.v[hanzi] += 1

    def search(self, pyin):
        cur_node = self.root
        for ch in pyin:
            if ch not in cur_node.child:
                return None
            else:
                cur_node = cur_node.child[ch]
        return cur_node.v

    def dfs_all(self, node, hzlist):
        if node.v:
            for key in node.v:
                if key in hzlist:
                    hzlist[key] += node.v[key]
                else:
                    hzlist[key] = node.v[key]
            return
        for ch in node.child:
            self.dfs_all(node.child[ch], hzlist)

    def dfs_display(self, node, py):
        if node.v:
            # print(py + ": ")
            # for key in node.v.keys():
            #     print key,
            #     print(node.v[key])
            print(node.v)
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in node.child:
                self.dfs_display(node.child[ch], py+ch)
        return

    def display_trie(self):
        self.dfs_display(self.root, "")

    def get_totalwords_of_prefix(self, node, prefix, hzlist):
        if len(prefix) == 0:
            return self.dfs_all(node, hzlist)
        # print(node.child)
        if prefix[0] in node.child:
            return self.get_totalwords_of_prefix(node.child[prefix[0]], prefix[1:], hzlist)

if __name__ == '__main__':

    trie = PinyinTrie()
    trie.add('wo', u"我")
    trie.add('lai', u"来")
    trie.add('da', u"打")
    trie.add('ni', u"你")
    trie.display_trie()

    print(trie)
    print(trie.search('da'))
    print(trie.search('hao'))

