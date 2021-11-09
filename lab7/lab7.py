from books import db
from match import match

#Deluppgift 1 - Utöka Match

print(match([["hej",["hej1",["hej3"]],"hej2"],["hej",["hej2",["hej3"]],"hej2"]],["&",["hej1", ["&"]],"&"])) 


def deep_match(seq : list, pattern : list):
    """A pattern match algorithm that checks lists in lists"""
    value = False
    for i in seq:

        #Det är en lista
        if(isinstance(seq[i],list)):
            deep_match(seq[i],pattern[i])

        #Inte är en lista
        value = match(seq[i])

    return value

#Deluppgift 2 - Sök i databas
