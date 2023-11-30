from src.state.state import *
from typing import *


class Tree:
    def __init__(self, root: Tuple[int, float]):
        self.root = root
        # state as int maps to -> children as Tuples of [child_value, child_evaluation]
        self.nodes: Dict[int, List[Tuple[int, float]]] = {}
        self.identifier = {}
        self.identifier[root[0]] = len(self.identifier) + 1

    def add_child_to_node(self, node: int, child: Tuple[int, float]):
        if child[0] not in self.identifier:
            self.identifier[child[0]] = len(self.identifier) + 1
        if node not in self.nodes:
            self.nodes[node] = []
        self.nodes[node].append(child)

    def display_tree(self):
        # print(self.nodes)
        self.display_node(self.root, "")

    def display_node(self, node: Tuple[int, float], prefix):
        print(f"{prefix}Node{self.identifier[node[0]]}: {node[1]}")
        if node[0] not in self.nodes:
            return
        for child in self.nodes[node[0]]:
            self.display_node(child, prefix + "|--")

    def set_root(self, root: Tuple[int, float]):
        self.root = root
