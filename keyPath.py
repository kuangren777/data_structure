# -*- coding: utf-8 -*-
# @Time    : 2024/6/4 9:35
# @Author  : KuangRen777
# @File    : keyPath.py
# @Tags    :
import networkx as nx


def critical_path_method(tasks):
    # 创建有向图
    G = nx.DiGraph()

    for task in tasks:
        G.add_node(task['name'], duration=task['duration'])
        for dependency in task['dependencies']:
            G.add_edge(dependency, task['name'])

    # 计算所有节点的最早开始时间和最晚开始时间
    earliest_start = {}
    latest_start = {}
    for node in nx.topological_sort(G):
        earliest_start[node] = max(
            [earliest_start.get(pred, 0) + G.nodes[pred]['duration'] for pred in G.predecessors(node)], default=0)

    for node in reversed(list(nx.topological_sort(G))):
        latest_start[node] = min(
            [latest_start.get(succ, float('inf')) - G.nodes[node]['duration'] for succ in G.successors(node)],
            default=earliest_start[node])

    # 计算关键路径
    critical_path = [node for node in G.nodes if earliest_start[node] == latest_start[node]]

    return critical_path, earliest_start, latest_start


# 示例任务数据
tasks = [
    {'name': 'A', 'duration': 3, 'dependencies': []},
    {'name': 'B', 'duration': 2, 'dependencies': ['A']},
    {'name': 'C', 'duration': 4, 'dependencies': ['A']},
    {'name': 'D', 'duration': 1, 'dependencies': ['B', 'C']},
    {'name': 'E', 'duration': 2, 'dependencies': ['D']},
]

# 计算关键路径
critical_path, earliest_start, latest_start = critical_path_method(tasks)

print(f"Critical Path: {critical_path}")
print(f"Earliest Start Times: {earliest_start}")
print(f"Latest Start Times: {latest_start}")
