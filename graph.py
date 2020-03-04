class Graph:

    def __init__(self):
        self._edges = list()
        self._nodes = list()

    def add_node(self, node):
        self._nodes.append(node)

    def has_node(self, node) -> bool:
        return node in self._nodes

    def add_edge(self, edge):
        if self.has_node(edge.second_node) and self.has_node(edge.first_node):
            self._edges.append(edge)

    def edges(self) -> list:
        return self._edges

    def nodes(self) -> list:
        return self._nodes


class Node(object):
    def __init__(self, label=None):
        self.label = label


class Edge:
    def __init__(self, first_node, second_node):
        self.first_node = first_node
        self.second_node = second_node
