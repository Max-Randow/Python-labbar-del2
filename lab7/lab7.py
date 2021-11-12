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
"""
print(deep_match([[["hej1","hej2"],["hej2",["hej3"]]]],
                 [["--",["hej2",["&"]]]])) 
"""

def search(pattern : list, db : list):
    """Seatch for a pattern in a database"""
    if(not db):
        return []

    if(not deep_match(db[0],pattern)):
        return search(pattern,db[1:])

    return db[0] + search(pattern,db[1:])

print(search([['författare', ['&', 'zelle']], ['titel', ['--', 'python', '--']], ['år', '&']], db))
#Deluppgift 2 - Sök i databas
