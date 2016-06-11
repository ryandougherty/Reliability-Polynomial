import networkx as nx
import random
import sympy

p = sympy.symbols('p')

def relpoly(G):
	H = nx.MultiGraph(G)
	rel = _recursive(H)
	return sympy.simplify(rel)

def _recursive(G):
	# If the graph is not connected, then it has a rel poly of 0
	if not nx.is_connected(G):
		return sympy.Poly(0, p)

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