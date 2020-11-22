# -*- coding:utf-8 -*-

'''
贪婪算法一般用来解决集合覆盖问题,在所有station中, 用尽可能少的station，覆盖所有的states。
如：旅行家问题：从某个城市出发，经过n个城市，所走的路程最少。本质上是n个城市的排列组合问题，问题的规模随城市的增加以阶乘的方式增大。
贪婪算法寻找局部最优解，企图以这种方式获得全局最优解。
对于NP完全问题，最佳的做法是使用近似算法；而贪婪算法是易于实现、运行速度快，是不错的近似算法。
'''

# 需要被覆盖的states
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# station对应的states
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# 最终选择的stations
final_stations = set()

while states_needed:
    best_station = None # 覆盖了最多的未覆盖的states的station
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station # 需要被覆盖的states与每个station能覆盖的states的交集
        if len(covered) > len(states_covered): # 选择能覆盖最多的未覆盖的states的station
            best_station = station
            states_covered = covered
    states_needed -= states_covered # 剔除已经覆盖的states
    final_stations.add(best_station)
    # print(best_station,states_covered)

print(final_stations)
