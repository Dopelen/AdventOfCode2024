import os
from collections import defaultdict

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input 46.txt"
file_path = os.path.join(desktop, file_name)
groups = defaultdict(set)
multiplayer = list()

with open(file_path, "r", encoding="utf-8") as file:
    connections = list(file)
    for connect in connections:
        first, second = connect.strip().split("-")
        groups[first].add(second)
        groups[second].add(first)


    def find_cliques(graph):
        #  Oh, you don't know the Bron–Kerbosch algorithm?
        #  What a pity, it's not a big deal, if you think about it, you can derive it yourself
        def bron_kerbosch(R, P, X):
            if not P and not X:
                cliques.append(R)
                return
            for v in list(P):
                bron_kerbosch(R | {v}, P & set(graph[v]), X & set(graph[v]))
                P.remove(v)
                X.add(v)

        cliques = []
        bron_kerbosch(set(), set(graph.keys()), set())
        return cliques


    def largest_clique(graph):
        cliques = find_cliques(graph)
        return max(cliques, key=len)


    print(",".join(sorted(largest_clique(groups))))
