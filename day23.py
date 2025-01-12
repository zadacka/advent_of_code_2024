from collections import defaultdict
from itertools import combinations

test_input = """\
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""

if __name__ == '__main__':
    # connections = test_input.splitlines()
    connections = open("input23.txt").read().splitlines()
    computer_connections = defaultdict(list)
    connection_pairs = set()
    for connection in connections:
        c1, c2 = connection.split('-')
        computer_connections[c1].append(c2)
        computer_connections[c2].append(c1)
        connection_pairs.add((c1, c2))
        connection_pairs.add((c2, c1))

    # sort values so cluster order is alphabetic
    computer_connections = {k: sorted(v) for k, v in computer_connections.items()}
    computer_names = list(sorted(computer_connections.keys()))

    clusters = set()

    for potential_cluster in combinations(computer_names, 3):
        if all(pair in connection_pairs for pair in combinations(potential_cluster, 2)):
            clusters.add(tuple(sorted(potential_cluster)))

    filtered_clusters = [
        cluster for cluster in clusters if any(computer.startswith('t') for computer in cluster)
    ]
    print(filtered_clusters)
    print(len(filtered_clusters))
