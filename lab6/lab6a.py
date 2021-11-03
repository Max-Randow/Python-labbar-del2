import calc
def exec_program(arg):  #[calc,STATEMENTS]
    if(calc.is_program(arg)):
        #Vi vet att det är ett program!
        statements = calc.program_statements(arg)

        if(calc.is_statements(statements)):
            """Det finns flera statements eller endast ett då innehållet i  
            statements kommer se ut som följande oavsett: [[exp1],[exp2]] / [[exp1]] """

            exec_statements(statements)
        
        
        #Behövs nog inte
        return True
    
    #Behövs nog inte
    return False
        

def exec_statements(statements):
    #Gå igenom alla statements och kalla exec_statement för varje.
    #[1,2,3,[1,2,[3]]] skulle kunna vara statements (fast med statements istället för siffror)
    
    print("Statements!")
 
    for statement in statements:
        #Här behöver vi kalla exec_statement som sedan kollar om det är selection,assignment etc...
        exec_statement(statement)
    

def eval_condition(expression) -> bool:

    #Vi vet att det är ett condition, dvs att operatorn är en condoper, det kommer alltså alltid att returneras något
    left = calc.condition_left(expression)
    right = calc.condition_right(expression)
    operator = calc.condition_operator(expression)
    
    if(operator == "<"):
        return left < right

    if(operator == ">"):
        return left > right

    else:
        return left == right

def eval_binary(expression):
    #Samma sak som i condition...
    pass


def exec_statement(statement):
    #Kolla vilken typ av statement det är och kalla sedan eval_condition för att i t.ex selection kolla om det blir sant eller falskt
    print("Statement!")

    #Göra match här istället så det ser finare ut? Korta ner kod i efterhand.
    if(calc.is_selection(statement)):
        condition = calc.selection_condition(statement)

        if(calc.is_condition(condition)):
            evaluation = eval_condition(condition)

            if(evaluation):
                #Do true branch
                pass
            else:
                #Do false branch
                pass
                
        else:
            pass

    elif(calc.calc.is_assignment(statement)):
        pass
    
    elif(calc.is_repetition(statement)):
        pass
    
    elif(calc.is_output(statement)):
        pass
    
    elif(calc.is_input(statement)):
        pass


exec_program(['calc', ['if', [3, '>', 5], ['print', 2], ['print', 4]]])