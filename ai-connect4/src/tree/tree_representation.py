from src.state.state import *
from typing import *


class Tree:
    """
        A class used to represent and visualize the minimax tree of the AI agent algorithm.

        Attributes:
        - root (Tuple[int, float]): The root node of the tree (initial state).
        - nodes (Dict[int, List[Tuple[int, float]]]): Mapping of nodes to their children.
        - identifier (Dict[int, int]): Mapping of node values to their identifiers (Ordering is neglected).
    """
    def __init__(self, root: Tuple[int, float]):
        """
            Initializes a Tree instance.

            :param root: The root node of the tree, that is, the initial state
            :type root: Tuple[int, float]
        """
        self.root = root
        # state as int maps to -> children as Tuples of [child_value, child_evaluation]
        self.nodes: Dict[int, List[Tuple[int, float]]] = {}
        self.identifier = {}
        self.identifier[root[0]] = len(self.identifier) + 1

    def add_child_to_node(self, node: int, child: Tuple[int, float]):
        """
            Adds a child node to a given node.

            :param node: The node to which the child will be added. (The parent node)
            :type node: int (integer representation of the parent node)
            :param child: The child node to be added.
            :type child: Tuple[int, float]
        """
        if child[0] not in self.identifier:
            self.identifier[child[0]] = len(self.identifier) + 1
        if node not in self.nodes:
            self.nodes[node] = []
        self.nodes[node].append(child)

    def display_tree(self):
        self.display_node(self.root, "")

    def display_node(self, node: Tuple[int, float], prefix):
        """
            Recursively displays the node and its children.

            :param node: The node to be displayed.
            :type node: Tuple[int, float]
            :param prefix: Prefix string for formatting display.
            :type prefix: str
        """
        print(f"{prefix}Node{self.identifier[node[0]]}: {node[1]}")
        if node[0] not in self.nodes:
            return
        for child in self.nodes[node[0]]:
            self.display_node(child, prefix + "|--")

    def set_root(self, root: Tuple[int, float]):
        """
            Sets a new root for the tree.

            :param root: The new root node.
            :type root: Tuple[int, float]
        """
        self.root = root

    def no_of_nodes_expanded(self):
        return len(self.identifier)
