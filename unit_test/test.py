#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/7/5 下午4:27
# @Author  : MiracleYoung
# @File    : test.py

from pprint import pprint


# 城市地图（字典的字典）
# 字典的第1个键为起点城市，第2个键为目标城市其键值为两个城市间的直接距离
# 将不相连点设为INF,方便更新两点之间的最小值
INF = 99999
G = {
    1: {1: 0, 2: 2, 3: 6, 4: 4},
    2: {1: INF, 2: 0, 3: 3, 4: INF},
    3: {1: 7, 2: INF, 3: 0, 4: 1},
    4: {1: 5, 2: INF, 3: 12, 4: 0}
}

g = [
    [0, 2, 6, 4],
    [INF, 0, 3, INF],
    [7, INF, 0, 1],
    [5, INF, 12, 0]
]

# 算法思想：
# 每个顶点都有可能使得两个顶点之间的距离变短
# 当两点之间不允许有第三个点时，这些城市之间的最短路径就是初始路径

# Floyd-Warshall算法核心语句
# 分别在只允许经过某个点k的情况下，更新点和点之间的最短路径
for k in G.keys():  # 不断试图往两点i,j之间添加新的点k，更新最短距离
    for i in G.keys():
        for j in G[i].keys():
            if G[i][j] > G[i][k] + G[k][j]:
                G[i][j] = G[i][k] + G[k][j]

pprint(G)


# dict_values([0, 2, 5, 4])
# dict_values([9, 0, 3, 4])
# dict_values([6, 8, 0, 1])
# dict_values([5, 7, 10, 0])