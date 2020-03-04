from unittest import TestCase
from graph import *


class TestGraph(TestCase):
    node1 = Node("node1")
    node2 = Node("node2")
    node3 = Node("node3")
    nodes = [node1, node2, node3]
    edge12 = Edge(nodes[0], nodes[1])
    edge13 = Edge(nodes[0], nodes[2])
    edges = [edge12, edge13]

    def setUp(self) -> None:
        self.graph = Graph()

    def _add_nodes_setup(self):
        for node in TestGraph.nodes:
            self.graph.add_node(node)

    def _add_edges_setup(self):
        for edge in TestGraph.edges:
            self.graph.add_edge(edge)

    def _complete_setup(self):
        self._add_nodes_setup()
        self._add_edges_setup()

    def test_get_nodes(self):
        self._add_nodes_setup()

        graph_nodes = self.graph.nodes()
        # retrieves only the inserted
        for node in graph_nodes:
            assert node in TestGraph.nodes, "retrieved but not inserted"
        # all inserted are retrieved
        for node in TestGraph.nodes:
            assert node in graph_nodes, "inserted but not retrieved"

    def test_get_edges(self):
        self._complete_setup()

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

    def test_get_neighbors(self):
        self._complete_setup()

        for node in self.graph.neighbors(TestGraph.node1):
            assert node == TestGraph.node2 or node == TestGraph.node3

        neighbors = self.graph.neighbors(TestGraph.node2)
        assert len(neighbors) == 1 and neighbors[0] == TestGraph.node1

        neighbors = self.graph.neighbors(TestGraph.node3)
        assert len(neighbors) == 1 and neighbors[0] == TestGraph.node1



