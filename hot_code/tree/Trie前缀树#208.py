# -*- coding: utf-8 -*-
# @Time : 2025/10/22 19:30
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : Trie前缀树#208.py
# @Project : leetcode

from typing import List, Optional


class Trie:

    def __init__(self):
        self.children = {"isEnd": True}
    def insert(self, word: str) -> None:
        node = self.children
        for char in word:
            if char not in node:
                node[char] = {"isEnd": False}
            node = node[char]
        node["isEnd"] = True
    def search(self, word: str) -> bool:
        node = self.children
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return node["isEnd"]
    def startsWith(self, prefix: str) -> bool:
        node = self.children
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True