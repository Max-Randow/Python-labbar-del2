# TDDE23 Lab 4: Binary tree

def is_empty_tree(tree):
    return isinstance(tree, list) and not tree

def is_leaf(tree):
    return isinstance(tree, int)
	
def left_subtree(tree):
    return tree[0]


def right_subtree(tree):
    return tree[2]

#Pred funktioner
def pred_empty():
    return 0

def pred_leaf(key):
    return key**2

def pred_node(key, left_value, right_value):
    return key + left_value


def traverse(tree,node_fn,leaf_fn,empty_fn):
    """Traverse a tree with predicates
    ::param:: tree is a binary tree
    ::param:: node_fn contains the parameters key,left_value,right_value
    ::param:: leaf_fn contains the parameter key
    ::param:: empty_fn contains no parameters
    """

    #Base cases
    if(is_empty_tree(tree)):
        return empty_fn()

    if(is_leaf(tree)):
        return leaf_fn(tree)

    #Get the node
    node = tree[1]
    
    #Get subtrees / leafs
    left = left_subtree(tree)
    right = right_subtree(tree)

    return node_fn(node,traverse(left,node_fn,leaf_fn,empty_fn),traverse(right,node_fn,leaf_fn,empty_fn))
    


def contains_key(key, tree):

    def node_fn(node,left,right):
        return (node == key) or left or right

    def leaf_fn(leaf):
        return leaf == key 
    
    def empty_fn():
        return False

    return traverse(tree,node_fn,leaf_fn,empty_fn)

#print(contains_key(7,[3,6,[7,6,3]]))