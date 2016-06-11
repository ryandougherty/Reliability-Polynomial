# -*- coding: utf-8 -*-

from .context import reliability

import networkx as nx

class TestEmpty():
    def test_absolute_truth_and_meaning(self):
    	s = reliability.brute_force.relpoly(nx.empty_graph())
    	assertEqual(s, [0])