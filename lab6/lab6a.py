import calc
def exec_program(arg):  #[calc,STATEMENTS]
    if(calc.is_program(arg)):
        #Vi vet att det är ett program!
        statements = calc.program_statements(arg)

        print(statements)
        if(calc.is_statements(statements)):
            #Det finns flera statements
            exec_statements(statements)
        elif(calc.is_statement(statements)):
            #Det finns bara ett statement
            exec_statement(statements)
        
        #Behövs nog inte
        return True
    
    #Behövs nog inte
    return False
        

def exec_statements(statements):
    #Gå igenom alla statements och kalla exec_statement för varje.
    #[1,2,3,[1,2,[3]]] skulle kunna vara statements (fast med statements istället för siffror)
    #Vi måste alltså göra rekursion.
    print("Statements!")

    pass
    

def exec_statement(statement):
    print("Statement!")


print(exec_program(['calc', ['if', [3, '>', 5], ['print', 2]]]))