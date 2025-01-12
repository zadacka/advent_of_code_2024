from collections import defaultdict

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

    N = {k: set(v) - {k} for k, v in computer_connections.items()}

    def BronKerbosch1(P, R=None, X=None):
        """credit: Kron-Kerbosch
        ... and Mykola from https://stackoverflow.com/questions/13904636/implementing-bron-kerbosch-algorithm-in-python"""
        P = set(P)
        R = set() if R is None else R
        X = set() if X is None else X
        if not P and not X:
            yield R
        while P:
            v = P.pop()
            yield from BronKerbosch1(
                P=P.intersection(N[v]), R=R.union([v]), X=X.intersection(N[v]))
            X.add(v)

    # problem "find the maximal cliques in an undirected graph" ...
    P = N.keys()
    result = list(BronKerbosch1(P))
    max_len = max(len(r) for r in result)
    result = [x for x in result if len(x) == max_len]
    result = result[0]
    print(result)
    print(','.join(sorted(result)))