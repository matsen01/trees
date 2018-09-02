def find_left_node(pre_order_list):
    if len(pre_order_list) >= 1:
        left = pre_order_list[0]
    else:
        left = None
    return left


def find_right_node(post_order_list):
    if len(post_order_list) >= 1:
        right = post_order_list[-1]
    else:
        right = None
    return right


def find_node(pre_order_list, post_order_list):
    root = pre_order_list[0]
    index_root_post = post_order_list.index(root)
    reduced_post_order_list = post_order_list[:index_root_post]
    reduced_pre_order_list = pre_order_list[1:len(reduced_post_order_list)+1]
    left = find_left_node(reduced_pre_order_list)
    right = find_right_node(reduced_post_order_list)
    return root, left, right


def reconstruct_tree(pre_order_list, post_order_list):
    node_list = []
    root_list = pre_order_list[:]
    for node in root_list:
        node_list.append(tuple(find_node(pre_order_list, post_order_list)))
        pre_order_list.remove(node)
        post_order_list.remove(node)
    return node_list
