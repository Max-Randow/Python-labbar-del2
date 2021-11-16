# TDDE23 Lab 4: Binary tree

def is_empty_tree(tree):
    return isinstance(tree, list) and not tree


def is_leaf(tree):
    return isinstance(tree, int)


def create_tree(left_tree, key, right_tree):
    return [left_tree, key, right_tree]

	
def left_subtree(tree):
    return tree[0]


def right_subtree(tree):
    return tree[2]


#Deluppgift 1
def traverse(tree):
    "Traverse a tree"

    if(is_empty_tree(tree)):
        return tree

    #Lista ut mitten
    root = tree[1]
    
    #Get subtrees / leafs
    left = left_subtree(tree)
    right = right_subtree(tree)
    
    is_left_leaf = is_leaf(left)
    is_right_leaf = is_leaf(right)

    if not is_left_leaf and not is_right_leaf:
        return traverse(left) + traverse(right)
    if not is_left_leaf:
        return traverse(left) + right
    if not is_right_leaf:
        return traverse(right) + left
    else:
        return left + right



#Deluppgift 2 

#Test funktioner
def pred_empty():
    return 0

def pred_leaf(key):
    return key**2

def pred_node(key, left_value, right_value):
    return key + left_value


def traverse(tree,node_fn,leaf_fn,empty_fn):
    "Traverse a tree"

    if(is_empty_tree(tree)):
        return empty_fn()

    if(is_leaf(tree)):
        print(is_leaf(tree))
        return leaf_fn(tree)

    #Lista ut mitten
    node = tree[1]
    
    #Get subtrees / leafs
    left = left_subtree(tree)
    right = right_subtree(tree)

    return node_fn(node,traverse(left,node_fn,leaf_fn,empty_fn),traverse(right,node_fn,leaf_fn,empty_fn))
    
    

#print(traverse([6, 7, 8],inner_node_fn,leaf_fn,empty_tree_fn))
"""
def contains_key(key, tree):

    def node_fn(node,left,right):
        print((node == key) or left or right)
        return left or right

    def leaf_fn(leaf):
        return leaf == key 
    
    def empty_fn():
        return False

    #Använder bool funktionen då det kan bli 1 eller 0 ibland
    return traverse(tree,node_fn,leaf_fn,empty_fn)"""

print(traverse([6,7,8],pred_node,pred_leaf,pred_empty))