from unittest import TestCase
from test_graph import TestGraph
from graph import Edge

__author__ = "Mattia Fanan"


class TestEdge(TestCase):
    equivalent_edge13 = Edge(TestGraph.node3, TestGraph.node1, TestGraph.edge13.weight)

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
        self.assertTrue(self.edge == self.edge)

    def test_equals_symmetry(self):
        equivalent_edge = TestEdge.equivalent_edge13

        self.assertTrue(self.edge == equivalent_edge and equivalent_edge == self.edge)

    def test_equals_transitivity(self):
        equivalent_edge = TestEdge.equivalent_edge13
        equivalent_edge2 = Edge(TestGraph.node1, TestGraph.node3)

        if self.edge == equivalent_edge and equivalent_edge == equivalent_edge2:
            self.assertTrue(self.edge == equivalent_edge2)

    def test_hash(self):
        equivalent_edge13 = TestEdge.equivalent_edge13

        self.assertTrue(hash(equivalent_edge13) == hash(TestGraph.edge13))

    def test_false_equals(self):
        self.assertFalse(self.edge == Edge(self.edge.first_node, self.edge.second_node, self.edge.weight + 5))
