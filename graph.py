__author__ = "Mattia Fanan"

from collections import KeysView


class Node(object):
    def __init__(self, label=None):
        self.label = label

    def __hash__(self):
        return super().__hash__()


class NotVertexOfThisEdgeError(ValueError):
    pass


class Edge:

    def __init__(self, first_node, second_node, weight=0):
        self.first_node = first_node
        self.second_node = second_node
        self.weight = weight

    def has_vertex(self, node: Node) -> bool:
        return node == self.first_node or node == self.second_node

    def opposite(self, node: Node) -> Node:
        if not self.has_vertex(node):
            raise NotVertexOfThisEdgeError("searched for the opposite vertex of a vertex that is not in this edge")
        if node == self.first_node:
            return self.second_node
        return self.first_node

    def __eq__(self, other):
        undirected_edge_equivalence = (other.first_node == self.first_node and other.second_node == self.second_node) \
                                      or (other.first_node == self.second_node and other.second_node == self.first_node)
        return isinstance(other, Edge) and self.weight == other.weight and undirected_edge_equivalence

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.first_node) + hash(self.second_node)


class Graph:

    def __init__(self):
        self._adjacency_list = dict()

    def add_node(self, node: Node):
        # initialize adjacency list elements are node : neighborhood -> empty dict
        # neighborhood elements are neighbor : edge.weight
        self._adjacency_list[node] = dict()

    def remove_node(self, node: Node):
        # delete edges
        for neighborhood in self._adjacency_list.values():
            try:
                neighborhood.pop(node)
            except KeyError:
                pass
        # delete node
        self._adjacency_list.pop(node)

    def has_node(self, node: Node) -> bool:
        return node in self._adjacency_list

    @property
    def nodes(self) -> set:
        return set(self._adjacency_list.keys())

    def add_edge(self, edge):
        """adds an edge from one node to the other and reverse"""
        if self.has_node(edge.second_node) and self.has_node(edge.first_node):
            self._adjacency_list[edge.second_node][edge.first_node] = edge.weight
            self._adjacency_list[edge.first_node][edge.second_node] = edge.weight

    def remove_edge(self, edge: Edge):
        self._adjacency_list[edge.second_node].pop(edge.first_node)
        self._adjacency_list[edge.first_node].pop(edge.second_node)

    def has_edge(self, edge: Edge) -> bool:
        return edge.first_node in self._adjacency_list[edge.second_node] \
               and self._adjacency_list[edge.second_node][edge.first_node] == edge.weight

    @property
    def edges(self) -> set:
        return {Edge(node, neighbor, weight)
                for node, neighbors_nodes in self._adjacency_list.items()
                for (neighbor, weight) in neighbors_nodes.items()}

    def neighbors(self, node: Node) -> dict:
        return self._adjacency_list[node]
