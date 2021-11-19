from books import db

#Deluppgift 1 - Utöka Match
def deep_match(seq : list, pattern : list):
    """A pattern match algorithm"""
    
    if not pattern:
        return not seq
    
    if pattern[0] == '--':
        if deep_match(seq, pattern[1:]):
            return True
        elif not seq:
            return False
        else:
            return deep_match(seq[1:], pattern)
    elif not seq:
        return False
    elif pattern[0] == '&':
        return deep_match(seq[1:], pattern[1:])
    elif seq[0] == pattern[0]:
        return deep_match(seq[1:], pattern[1:])
    elif(isinstance(seq[0],list) and isinstance(pattern[0],list)):
        return deep_match(seq[0],pattern[0]) and deep_match(seq[1:],pattern[1:])
    else:
        return False

#Deluppgift 2 - Sök i databas

def search(pattern : list, db : list):
    """Search for a pattern in a database"""
    if(not db):
        return []

    if(not deep_match(db[0],pattern) ):
        return search(pattern,db[1:])

    return db[0] + search(pattern,db[1:])

def test():
    assert(search(["--",["år",2009],"--"],db)) == [['författare', ['john', 'zelle']], ['titel', ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']], ['år', 2009]]
    assert(search(["--", ["titel", ["programmering", "i", "lisp"]], "--"],db)) == [['författare', ['anders', 'haraldsson']],['titel', ['programmering', 'i', 'lisp']],['år', 1993]]
    assert(search(["--", ["titel", ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']], "&","hej"],db)) == []

    print("Passed all tests!")

test()

