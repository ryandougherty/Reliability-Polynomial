from sympy.parsing.sympy_parser import parse_expr

p = sympy.symbols('p')

def relpoly(G):
	rel = _recursive(G)
	return parse_expr(rel)

def _recursive(G):
	if len(G.nodes()) <= 1:
		return '(1)'
	elif nx.number_connected_components(G) > 1:
		return None
	else:
		e = random.choice(G.edges())
		H = G.copy()
		H.remove_edge(*e)
		H1 = nx.contracted_edge(G,e)
		print(len(G.nodes()), len(H1.nodes()))
		first = _recursive(H1)
		second = _recursive(H)
		if first and second:
			return '(p*'+first+')+(1-p)*('+second+')'
		elif first:
			return '(p*'+first+')'
		elif second:
			return '(1-p)*('+second+')'
		else:
			return ''