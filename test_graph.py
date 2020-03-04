from unittest import TestCase
from graph import *


class TestGraph(TestCase):
    node1 = Node("node1")
    node2 = Node("node2")
    nodes = [node1, node1]
    edges = [Edge(nodes[0], nodes[1])]

    def setUp(self) -> None:
        self.graph = Graph()

    def test_get_nodes(self):

        for node in TestGraph.nodes:
            self.graph.add_node(node)

        graph_nodes = self.graph.nodes()

        # retrieves only the inserted
        for node in graph_nodes:
            assert node in TestGraph.nodes, "retrieved but not inserted"
        # all inserted are retrieved
        for node in TestGraph.nodes:
            assert node in graph_nodes, "inserted but not retrieved"

    def test_get_edges(self):
        nodes = [Node("node1"), Node("node2")]

        for node in TestGraph.nodes:
            self.graph.add_node(node)

        self.graph.add_edge(TestGraph.edges[0])

        graph_edges = self.graph.edges()

        # retrieves only the inserted
        for edge in graph_edges:
            assert edge in TestGraph.edges
        # all inserted are retrieved
        for edge in TestGraph.edges:
            assert edge in graph_edges

    def test_has_node(self):
        node1 = TestGraph.node1
        assert not self.graph.has_node(node1)
        self.graph.add_node(node1)
        assert self.graph.has_node(node1)
