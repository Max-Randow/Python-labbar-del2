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
        #Yolo lösning till while loopar
        return copy_variables
    else:
        pass
        #kasta error

def eval_condition(expression : list, variables : dict) -> bool:
    """Fixa calc_expression"""
    #Vi vet att det är ett condition, dvs att operatorn är en condoper, det kommer alltså alltid att returneras något av följande
    left = calc.condition_left(expression)

    left = eval_expression(left,variables)

    right = calc.condition_right(expression)

    right = eval_expression(right,variables)

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
    left = eval_expression(calc.binaryexpr_left(expression),variables)
 
    right = eval_expression(calc.binaryexpr_right(expression),variables)

    
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
            evaluation = eval_condition(condition,copy_variables)

            #Om conditionet / binary expr. stämmer så hämtar vi true branchen annars false branchen.
            if(evaluation):
                #True Branch!
                true_branch = calc.selection_true_branch(statement)
                #True branch kan vara ett till statement Typ som [set, 'a', 7], rekurera
                exec_statement(true_branch,copy_variables)
            else:
                #False Branch!
                false_branch = calc.selection_false_branch(statement)
                #False branch kan vara ett till statement Typ som [set, 'a', 7], rekurera
                exec_statement(false_branch,copy_variables)  
    
        else:
            #Kasta error!
            pass

  
    #Assignment
    elif(calc.is_assignment(statement)):
        copy_variables = exec_assignment(statement,copy_variables)

    #Repetition
    elif(calc.is_repetition(statement)):

        loop_condition = calc.repetition_condition(statement)
        loop_statements = calc.repetition_statements(statement)
        
        while eval_condition(loop_condition,copy_variables):
            copy_variables = exec_statements(loop_statements, copy_variables)


    elif(calc.is_output(statement)):
        expression = eval_expression(calc.output_expression(statement),copy_variables)
        print(expression)
    

    elif(calc.is_input(statement)):
        #Numeriskt värde m.h.a input()
        variable = calc.input_variable(statement)

        try:
            user_input = int(input("Enter a numerical value: "))

            copy_variables[variable] = user_input

        except TypeError:
            pass
            #Throw error


    return copy_variables


def exec_assignment(statement : list, variables : dir):
    #Använd dictionary
    variables_copy = copy.deepcopy(variables)

    variable = calc.assignment_variable(statement)
    value = eval_expression(calc.assignment_expression(statement),variables)

    #Kolla om det är ett numeriskt värde?
    if(calc.is_constant(value)):
        variables_copy[variable] = value
    
    else:
        #Throw error
        pass

    return variables_copy

def eval_expression(expression : list, variables : dict):
    if(calc.is_binaryexpr(expression)):
        return eval_binary(expression,variables)
    
    elif(calc.is_variable(expression)):
        return eval_variable(expression,variables)

    elif(calc.is_constant(expression)):
        return eval_constant(expression)

    else:
        pass
        #Throw error


def eval_constant(expression):
    return expression

def eval_variable(expression,variables):
    if(expression in variables.keys()):
        return variables[expression]
    else:
        #Throw error?
        pass

#exec_program(['calc', ['if', [6, '>', 5], ['print', 2], ['print', 4]]])

exec_program(['calc', ['if', [[5,"+",[5,"-",5]], '>', 5], ['print', 2], ['print', 4]]])

#exec_program(['calc',["set","n",7], ["while", [14,">","n"],
             #["set","n",["n","+",1]],["print","n"]]])
