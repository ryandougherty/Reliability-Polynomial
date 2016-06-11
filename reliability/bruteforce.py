import functools
import math
import networkx as nx
import random
import sympy

p = sympy.symbols('p')

def relpoly(G):
	H = nx.MultiGraph(G)
	rel = _recursive(H)
	return sympy.simplify(rel)

def _complete(G):
	n = len(set(G.nodes()))
	return _complete_helper(n)

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

@functools.lru_cache(maxsize=None)
def _complete_helper(n):
	if n == 1:
		return sympy.Poly(1, p)
	else:
		s = sympy.Poly(0, p)
		for j in range(1, n):
			s += nCr(n-1, j-1)*_complete_helper(j)*sympy.Poly(1-p)**(j*(n-j))
		return 1-sympy.simplify(s)

def is_multigraph_complete_no_parallel(G):
	# Return true if G is a multigraph
	# that has no parallel edges
	n = len(G.nodes())
	for v in G.nodes():
		if G.degree(v) != n-1:
			return False
	return True

def _recursive(G):
	# If the graph is not connected, then it has a rel poly of 0
	if not nx.is_connected(G):
		return sympy.Poly(0, p)
	
	# Check if the graph is multigraph complete
	#  and has no parallel edges
	if is_multigraph_complete_no_parallel(G):
		return _complete(G)

	# if # edges > 0, then we perform the two subcases of the 
	# 	Factoring theorem.
	if len(G.edges()) > 0:
		e = random.choice(G.edges())
		contracted = nx.contracted_edge(G, e, self_loops=False)
		G.remove_edge(*e)
		rec_deleted = _recursive(G)
		rec_contracted = _recursive(contracted)
		s = sympy.Poly(p)*(rec_contracted) + sympy.Poly(1-p)*(rec_deleted)
		return s

	# Otherwise, we only have 0 edges and 1 vertex, which is connected,
	# 	so we return 1.
	return sympy.Poly(1, p)

print(relpoly(nx.petersen_graph()))