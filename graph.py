__author__ = "Mattia Fanan"


class Node(object):
    def __init__(self, label=None):
        self.label = label


class NotVertexOfThisEdgeError(ValueError):
    pass


class Edge:
    def __init__(self, first_node, second_node, weight=None):
        self.first_node = first_node
        self.second_node = second_node
        self.weight = weight

    def is_vertex(self, node: Node) -> bool:
        return node == self.first_node or node == self.second_node

    def opposite(self, node: Node) -> Node:
        if not self.is_vertex(node):
            raise NotVertexOfThisEdgeError("searched for the opposite vertex of a vertex that is not in this edge")
        if node == self.first_node:
            return self.second_node
        return self.first_node


class Graph:

    def __init__(self):
        self._edges = list()
        self._nodes = list()

    def add_node(self, node: Node):
        self._nodes.append(node)

    def has_node(self, node) -> bool:
        return node in self._nodes

    def nodes(self) -> list:
        return self._nodes

    def add_edge(self, edge):
        if self.has_node(edge.second_node) and self.has_node(edge.first_node):
            self._edges.append(edge)

    def remove_edge(self, edge: Edge):
        self._edges.remove(edge)

    def edges(self) -> list:
        return self._edges

    def neighbors(self, node: Node) -> list:
        neighbors_list = list()
        for edge in self.edges():
            try:
                neighbors_list.append(edge.opposite(node))
            except NotVertexOfThisEdgeError:
                pass
        return neighbors_list
