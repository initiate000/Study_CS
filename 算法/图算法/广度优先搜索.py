# -*- coding:utf-8 -*-
from collections import deque

'''
广度优先算法被用来解决两类问题：
（1）从节点A出发，有前往节点B的路径吗？
（2）从节点A出发，前往节点B的最短路径是哪条？（经过的节点数最少）
'''

def person_is_seller(name):
      return name[-1] == 'm'

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def breadth_first_search(name):
    search_queue = deque() # 创建一个队列，先进先出
    search_queue += graph[name]
    searched = [] # 用来表示某个节点已经被检查过了，防止重复检查或在两个节点之间循环
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

breadth_first_search("you")
