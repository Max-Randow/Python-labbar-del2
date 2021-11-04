import calc
import copy
def exec_program(args : list):  #[calc,STATEMENTS]
    if(calc.is_program(args)):
        #Vi vet att det är ett program!
        statements = calc.program_statements(args)

        if(calc.is_statements(statements)):

            variables = {}
            exec_statements(statements,variables)
 
def exec_statements(statements : list, variables : dict):
    copy_variables = copy.deepcopy(variables)

    #Rekursion
    if(not calc.empty_statements(statements)):
        #Gå igenom alla statements
        first = calc.first_statement(statements)
        rest = calc.rest_statements(statements)

        copy_variables = exec_statement(first, copy_variables)
        exec_statements(rest,copy_variables)
    

def eval_condition(expression : list, variables : dict) -> bool:

    #Vi vet att det är ett condition, dvs att operatorn är en condoper, det kommer alltså alltid att returneras något av följande
    left = calc.condition_left(expression)

    #Kolla om left är ett binary expression?
    if(calc.is_binaryexpr(left)):
        left = eval_binary(left)

    right = calc.condition_right(expression)

    #Kolla om right är ett binary expression?
    if(calc.is_binaryexpr(right)):
        right = eval_binary(right)

    operator = calc.condition_operator(expression)
    
    if(operator == "<"):
        return left < right

    elif(operator == ">"):
        return left > right

    else:
        return left == right

def eval_binary(expression : list, variables : dict) -> bool:
    # [[5, +, 5], + ,5]
    #Vi vet att det är ett binary expression, dvs att operatorn är en binary operator, det kommer alltså alltid att returneras något av följande
    left = calc_expression(calc.binaryexpr_left(expression),variables)
 
    right = calc_expression(calc.binaryexpr_right(expression),variables)

    
    operator = calc.binaryexpr_operator(expression)
    
    if(operator == "+"):
        return left + right

    elif(operator == "-"):
        return left - right

    elif(operator == "*"):
        return left * right
    
    else:
        return left / right



def exec_statement(statement : list, variables : dict):
    #Kolla vilken typ av statement det är och kalla sedan eval_condition för att i t.ex selection kolla om det blir sant eller falskt

    copy_variables = copy.deepcopy(variables)

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
        copy_variables = exec_assignment(statement,copy_variables)

    elif(calc.is_repetition(statement)):
        pass
    

    elif(calc.is_output(statement)):
        expression = calc.output_expression(statement)
        print(expression)
    

    elif(calc.is_input(statement)):
       #Numeriskt värde m.h.a input()
       expression = calc.input_variable(statement)


    return copy_variables


def exec_assignment(statement : list,variables : dir):
    #Använd dictionary
    variables_copy = copy.deepcopy(variables)

    variable = calc.assignment_variable(statement)
    value = calc_expression(calc.assignment_expression(statement),variables)

    if(calc.is_constant(value)):
        variables_copy[variable] = value
    
    else:
        #Throw error
        pass

    return variables_copy

def calc_expression(expression : list, variables : dict):
    if(calc.is_binaryexpr(expression)):
        return eval_binary(expression)
    
    elif(calc.is_variable(expression)):
        return variables[expression]

    elif(calc.calc.is_constant(expression)):
        return expression

    else:
        pass
        #Throw error

#exec_program(['calc', ['if', [6, '>', 5], ['print', 2], ['print', 4]]])

exec_program(['calc', ['if', [[5,"+",[5,"-",5]], '>', 5], ['print', 2], ['print', 4]]])