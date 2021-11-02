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
    

def exec_statement(statement):
    #Kolla vilken typ av statement det är och kalla sedan eval_condition för att i t.ex selection kolla om det blir sant eller falskt
    print("Statement!")

def eval_condition(expression):
    if(calc.is_condition(expression)):
        #Vi vet att det är ett condition, dvs att operatorn är en condoper
        left = calc.condition_left(expression)
        right = calc.condition_right(expression)
        operator = calc.condition_operator(expression)
        
        if(operator == "<"):
            return left < right
        elif(operator == ">"):
            return left > right
        else:
            return left == right
        
    #Annars kasta error

def eval_binary(expression):
    #Samma sak som i condition...
    pass



exec_program(['calc', ['if', [3, '>', 5], ['print', 2], ['print', 4]]])