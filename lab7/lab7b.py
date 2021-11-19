# TDDE23 Lab 4: Binary tree

def is_empty_tree(tree):
    return isinstance(tree, list) and not tree

def is_leaf(tree):
    return isinstance(tree, int)
	
def left_subtree(tree):
    return tree[0]


def right_subtree(tree):
    return tree[2]

##########################

#Deuppgift 1 & 2
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
    
#Deluppgift 2

def contains_key(key, tree):
    """Checks if a key is contained a binary tree"""
    def node_fn(node,left,right):
        return (node == key) or left or right

    def leaf_fn(leaf):
        return leaf == key 
    
    def empty_fn():
        return False

    return traverse(tree,node_fn,leaf_fn,empty_fn)

#print(contains_key(7,[[7,7,7],7,7]))


#Deluppgift 3

def tree_size(tree):
    """Return the size of a binary tree"""
    def node_fn(node,left,right):
        return 1 + left + right 

    def leaf_fn(leaf):
        return 1
    
    def empty_fn():
        return 0

    return traverse(tree,node_fn,leaf_fn,empty_fn)


#print(tree_size(  [[[7,9,8],7,[1,-1,4]],5,[[1,4,5],6,[6,7,-9]]]  )) #Should be 15, returns 15


#Deluppgift 4
def tree_depth(tree):
    """Returns the depth of a binary tree"""
    def node_fn(node,left,right):
        return 1 + max(left,right)

    def leaf_fn(leaf):
        return 1

    def empty_fn():
        return 0

    return traverse(tree,node_fn,leaf_fn,empty_fn)

print(tree_depth([1,5,[10,7,15]]))


#---- Test ----#
def test():
    """Test function"""
    #Vi testar traverse() i deluppgifterna 2,3 och 4.
    #Test för contains_key()
    assert(contains_key(7,[1,2,[4,5,7]])) == True
    assert(contains_key(1,[1,3,[4,1,-1]])) == True
    assert(contains_key(10,[-1,3,[4,5,7]])) == False

    #Test för tree_size()
    assert(tree_size([1,2,[4,6,767676]])) == 5
    assert(tree_size([1,2,[4,6,[5,4,3]]])) == 7
    assert(tree_size([[1,2,3],2,[4,6,-1]])) == 7

    #Test för tree_depth()
    assert(tree_depth([1,2,3])) == 2
    assert(tree_depth(1)) == 1
    assert(tree_depth([[1,2,3],2,[1,2,[1,2,[1,2,3]]]])) == 5

    print("Passed all the tests!")


test()