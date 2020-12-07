# -*- coding:utf-8 -*0

'''
Dijkstra's algorithm
广度优先搜索找出了段数最少（经过的节点最少）的路径，但并不一定是权值最小的路径。
狄克斯特拉算法能找出加权图中前往X的最短路径（权值之和最小），只适用于有向无环图，且不包含负权边。
对于包含负权边的图，可使用Bellman-Ford算法。

1、找出最便宜的节点。
2、更新该节点的邻居的开销。
3、重复1和2，直到对所有的节点都计算过了。
4、计算最终路径。
'''

# 图
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['end'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5

graph['end'] = {}
# print(graph)

# 花费表，the cost table,记录到每一个节点的开销
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['end'] = float('inf') # 初始化为无穷大

# 父节点表，记录每一个节点的父节点
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['end'] = None

# 记录已经处理过的节点，对于同一个节点，不应该处理多次
processed_nodes = []

'''
while node not in processed_nodes:
    获取离起点最近的节点
    更新其邻居的开销
    如果有邻居的开销被更新，同时更新其父节点
    将该节点标记为处理过
'''

def find_lowest_cost_node(costs):
    '找出开销最低的节点'
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        if node not in processed_nodes:
            cost = costs[node]
            if cost < lowest_cost:
                lowest_cost = cost
                lowest_cost_node = node
    return lowest_cost_node


def dijkstra(node):
    while node:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed_nodes.append(node)
        node = find_lowest_cost_node(costs)

if __name__ == "__main__":
    node = find_lowest_cost_node(costs)
    dijkstra(node)
    print("cost from start to each node:")
    print(costs)
