from unittest import TestCase
from test_graph import TestGraph
from graph import Edge

__author__ = "Mattia Fanan"


class TestEdge(TestCase):
    def setUp(self) -> None:
        self.edge = TestGraph.edge13

    def test_opposite(self):
        self.assertEqual(TestGraph.node1, self.edge.opposite(TestGraph.node3),
                         "edge don't return node1 as opposite of node3 in edge13")
        self.assertEqual(TestGraph.node3, self.edge.opposite(TestGraph.node1),
                         "edge don't return node3 as opposite of node1 in edge13")

    def test_is_vertex(self):
        self.assertTrue(self.edge.has_vertex(TestGraph.node1), "Node1 should be vertex of edge13")
        self.assertFalse(self.edge.has_vertex(TestGraph.node2), "Node2 shouldn't be vertex of edge13")

    def test_equals_reflexivity(self):
        self.assertTrue(TestGraph.edge13 == TestGraph.edge13)

    def test_equals_symmetry(self):
        equivalent_edge13 = Edge(TestGraph.node1, TestGraph.node3)
        self.assertTrue(TestGraph.edge13 == equivalent_edge13 and equivalent_edge13 == TestGraph.edge13)

    def test_equals_transitivity(self):
        equivalent_edge13 = Edge(TestGraph.node1, TestGraph.node3)
        equivalent2_edge13 = Edge(TestGraph.node1, TestGraph.node3)
        if TestGraph.edge13 == equivalent_edge13 and equivalent_edge13 == equivalent2_edge13:
            self.assertTrue(TestGraph.edge13 == equivalent2_edge13)
