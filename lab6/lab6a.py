import calc
def exec_program(arg):  #[calc,STATEMENTS]
    if(calc.is_program(arg)):
        #Vi vet att det är ett program!
        statements = calc.program_statements(arg)

        if(calc.is_statements(statements)):

            exec_statements(statements)
 
def exec_statements(statements):

    #Rekursion
    if(not calc.empty_statements(statements)):
        #Gå igenom alla statements
        first = calc.first_statement(statements)
        rest = calc.rest_statements(statements)

        exec_statement(first)
        exec_statements(rest)
    

def eval_condition(expression) -> bool:

    """Vad händer om man har [[5, + ,[5 + 5]],=,15] ?? """

    #Vi vet att det är ett condition, dvs att operatorn är en condoper, det kommer alltså alltid att returneras något av följande
    left = calc.condition_left(expression)
    #Kolla om left är ett binary expression?
    right = calc.condition_right(expression)
    #Kolla om right är ett binary expression?
    operator = calc.condition_operator(expression)
    
    if(operator == "<"):
        return left < right

    elif(operator == ">"):
        return left > right

    else:
        return left == right

def eval_binary(expression):

    #Vi vet att det är ett binary expression, dvs att operatorn är en binary operator, det kommer alltså alltid att returneras något av följande
    left = calc.binaryexpr_left(expression)
    #Kolla om left är ett binary expression?
    right = calc.binaryexpr_right(expression)
    #Kolla om right är ett binary expression?
    operator = calc.binaryexpr_operator(expression)
    
    if(operator == "+"):
        return left + right

    elif(operator == "-"):
        return left - right

    elif(operator == "*"):
        return left * right
    
    else:
        return left / right

def exec_statement(statement):
    #Kolla vilken typ av statement det är och kalla sedan eval_condition för att i t.ex selection kolla om det blir sant eller falskt
    print(statement)

    #Göra match här istället så det ser finare ut?

    #Selection
    if(calc.is_selection(statement)):

        condition = calc.selection_condition(statement)
        #Kolla om det faktiskt är ett condition / binary expression, annars går det ju inte!
        if(calc.is_condition(condition)):
            #Kolla om expressionet är sant
            evaluation = eval_condition(condition)

            #Om conditionet / binary expr. stämmer så hämtar vi true branchen annars false branchen.
            if(evaluation):
                #True Branch!
                true_branch = calc.selection_true_branch(statement)
                #True branch kan vara ett till statement Typ som [set, 'a', 7], rekurera
                exec_statement(true_branch)
            else:
                #False Branch!
                false_branch = calc.selection_false_branch(statement)
                #False branch kan vara ett till statement Typ som [set, 'a', 7], rekurera
                exec_statement(false_branch)  
    
        else:
            #Kasta error!
            pass

  
    #Assignment
    elif(calc.is_assignment(statement)):
        #Får man använda ett dictionary som är globalt här eller hur ska man spara värden?
        pass
    

    elif(calc.is_repetition(statement)):
        pass
    

    elif(calc.is_output(statement)):
        expression = calc.output_expression(statement)
        print(expression)
    

    elif(calc.is_input(statement)):
        #Får man använda ett dictionary som är globalt här eller hur ska man läsa värden?
        expression = calc.input_variable(statement)



exec_program(['calc', ['if', [6, '>', 5], ['print', 2], ['print', 4]]])

#exec_program(['calc', ['if', [[10,"+",5], '>', 5], ['print', 2], ['print', 4]]])