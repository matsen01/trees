from methods import reconstruct_tree

pre_order_list = [1, 2, 4, 5, 8, 3, 6, 7]
post_order_list = [4, 8, 5, 2, 6, 7, 3, 1]

print(reconstruct_tree(pre_order_list, post_order_list))
