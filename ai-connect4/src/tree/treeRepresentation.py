def print_tree(node, indent):
    """
    Print the Minimax tree.

    :param node: Current node in the tree.
    :type node: dict
    :param indent: Current indentation level.
    :type indent: int
    """

    for key, value in node.items():
        print("  " * indent, key, ":", value["value"])
        if "children" in value:
            print_tree(value["children"], indent + 1)