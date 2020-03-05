from unittest import TestCase
from graph import *
from graph_algorithms import *


class TestGraphAlgorithms(TestCase):

    def setUp(self) -> None:
        self.graph = Graph()
        self.solution = [3]

    def test_dijkstra(self):
        self.assertEqual(dijkstra_path(self.graph), self.solution)

    def test_a_star(self):
        self.assertEqual(a_star_path(self.graph), self.solution)
