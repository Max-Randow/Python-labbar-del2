#-- Imports --
import calc
import copy

#-- Main functions --
"""These functions are the core to the program. These functions call sub-functions called "Statement functions" and "Evaluation functions". """

def exec_program(args : list, variables = None) -> dict: 
    """Runs a Calc program, args. You can also use your own premade variables with the second parameter."""

    if(variables == None):
        #This only changes the "memory slot" that the variable is pointing to, thus not destructive.
        variables = {}
    #We know that it's a program as the first element is "calc"
    if(calc.is_program(args)):
        
        statements = calc.program_statements(args)

        #If the program has any statements, run the second function
        if(calc.is_statements(statements)):
            
            return exec_statements(statements,variables)
        
def exec_statements(statements : list, variables : dict) -> dict:
    """Execute the statements of the program, returns a (maybe) modified dictionary"""

    #If there are any statements left in statements, go through them recursively
    if(not calc.empty_statements(statements)):

        #Grab the first element and the rest
        first = calc.first_statement(statements)
        rest = calc.rest_statements(statements)

        #Go through the first statement and re-run the function with the rest.
        variables = exec_statement(first, variables)
        return exec_statements(rest, variables)

    #There are no statements left, return the variables
    return variables

def exec_statement(statement : list, variables : dict) -> dict:
    """Executes a statement no matter what type it is, returns a (maybe) modified dictionary"""
 
    #Here we have distributed the code throughout multiple functions in order to make the code more readable.

    #Selection
    if(calc.is_selection(statement)):
        variables = exec_selection(statement,variables)
  
    #Assignment
    elif(calc.is_assignment(statement)):
        variables = exec_assignment(statement,variables)

    #Repetition
    elif(calc.is_repetition(statement)):
        variables = exec_repetition(statement,variables)
    #Output
    elif(calc.is_output(statement)):
        exec_output(statement,variables)
    
    #Input
    elif(calc.is_input(statement)):
        variables = exec_input(statement,variables)
   
    #Return the (maybe) modified copy
    return variables


#-- Execute statement functions ()

"""These functions are used within the exec_statement function"""

def exec_repetition(statement : list, variables : dict) -> dict:
    """Executes a repetition statement and returns a (maybe) modified dictionary"""
    
    #Grab the condition and the statements from the current statement
    loop_condition = calc.repetition_condition(statement)
    loop_statements = calc.repetition_statements(statement)
    
    #While the condition is true, execute the loop_statements
    while eval_condition(loop_condition,variables):
        
        #Return the new copy_variables
        variables = exec_statements(loop_statements, variables)

    return variables

def exec_selection(statement : list,variables : dict) -> dict:
    """Executes a selection statement and returns a (maybe) modified dictionary"""

    #Grab the selection condition
    condition = calc.selection_condition(statement)

    #Check if it's an actual condition, if not throw an error
    if(calc.is_condition(condition)):
        
        #Use the eval_condition function (which returns if a condition is T/F) to see if the selection condition is true
        evaluation = eval_condition(condition,variables)

        #If it's true, get the true branch
        if(evaluation):
            #True Branch!
            true_branch = calc.selection_true_branch(statement)
            
            #Execute and return the true_branch statement
            return exec_statement(true_branch,variables)
        else:
            #Else, check if the statement has a false branch
            if(calc.selection_has_false_branch(statement)):
                #False Branch!
                false_branch = calc.selection_false_branch(statement)
                
                #Execute and return the false_branch statement
                return exec_statement(false_branch,variables)  

    else:
        raise TypeError("The condition provided in the selection is not an actual condition")
    
    #Return the  (maybe) modified copy_variables
    return variables

def exec_input(statement : list,variables : dict) -> dict:
    """Executes an input statement and returns a modified dictionary"""

    #Create a copy in order to avoid a destructable function
    copy_variables = copy.deepcopy(variables)

    #Grab the variable that is to be modified
    variable = calc.input_variable(statement)
    
    #If the input is not a number (float or int), throw an error
    try:
        #Get the user input
        
        user_input = input("Enter value for " + variable + ": ")
        
        #Update the dictionary
        if('.' in user_input):
            copy_variables[variable] = float(user_input)

        else:
            copy_variables[variable] = int(user_input)

        #Return the modified dictionary.
        return copy_variables

    #Throw error if the datatype is not correct
    except ValueError:
        raise TypeError("The input provided by the user was not a number")
        

def exec_output(statement : list,variables : dict):
    """Executes an output statement and does not return anything"""

    #Grab the output_expression, which we will use if and only if it's a variable.
    output_expression = calc.output_expression(statement)
    expression = eval_expression(output_expression,variables)

    #If it is a variable, print which variable is equal to the output.
    if(calc.is_variable(output_expression)):
        print(output_expression + " = " + str(expression))
    else:
        print(expression)

def exec_assignment(statement : list, variables : dict) -> dict:
    """Executes an assignment statement and returns a modified dictionary"""

    #Create a copy in order to avoid the function from being destructive
    variables_copy = copy.deepcopy(variables)

    #Grab the variable and it's soon to be value
    variable = calc.assignment_variable(statement)
    value = eval_expression(calc.assignment_expression(statement),variables)
    
    #Check if the value is a constant, if not - cast an error
    if(calc.is_constant(value)):
        variables_copy[variable] = value
        #Return the modified copy
        return variables_copy

    #Throw error
    raise TypeError("Not a constant")

#-- Evaluate functions --

"""These functions evaluate conditions and expressions and are heavily used within the functions above."""

def eval_condition(expression : list, variables : dict) -> bool:
    """When we know that it in fact is a condition we can calculate it's value with this function"""
    try:
        #Grab the left side of the expression and get it's "true" value
        left = calc.condition_left(expression)
        left = eval_expression(left,variables)

        #Grab the right side of the expression and get it's "true" value
        right = calc.condition_right(expression)
        right = eval_expression(right,variables)

        #Get the operator
        operator = calc.condition_operator(expression)
       
        #Return a different value depending on the operator
        if(operator == "<"):
            return left < right

        elif(operator == ">"):
            return left > right

        else:
            return left == right
            
    except(TypeError):
        raise TypeError("The condition does not contain the correct datatypes/operators")

def eval_binary(expression : list, variables : dict) -> bool:
    """When we know that it's a binary expression, we can use this function to calculate it's value"""
    
    #Grab left side of the expression
    left = eval_expression(calc.binaryexpr_left(expression),variables)
    
    #Grab the right side of the expression
    right = eval_expression(calc.binaryexpr_right(expression),variables)

    #Grab the operator 
    operator = calc.binaryexpr_operator(expression)
    
    #Return a different value depending on the operator
    if(operator == "+"):
        return left + right

    elif(operator == "-"):
        return left - right

    elif(operator == "*"):
        return left * right
    
    else:
        return left / right

def eval_expression(expression : list, variables : dict):
    """This function 'calculates' all expressions. It can: return a variables value, return the value of a binary expression, return a constant"""
    if(calc.is_binaryexpr(expression)):
        return eval_binary(expression,variables)
    
    elif(calc.is_variable(expression)):
        return eval_variable(expression,variables)

    elif(calc.is_constant(expression)):
        return eval_constant(expression)

    #If none of the above worked, throw an error as it isn't an expression
    raise TypeError("The expression of type list is not an expression")

def eval_constant(expression : str):
    """Returns the value of the constant"""
    return expression

def eval_variable(expression : str,variables : dict):
    """Returns the variable's value"""
    
    try:
        #Look up so that the variable in fact is in the dictionary before grabbing it's value.
        if(expression in variables.keys()):
            return variables[expression]
    
    #If it's not in the dictionary, throw an error.
    except KeyError:
        print(f"Key does not exist in {variables}")

    

#-- Code to run the program --#

#exec_program(['calc', ['if', [6, '>', 5], ['print', 2], ['print', 4]]])

#exec_program(['calc', ['if', [[5,"+",[5,"-",5]], '>', 5], ['print', 2], ['print', 4]]])

"""print(exec_program(['calc',["set","n",7], ["while", ["n",">",5],
           ["set","n",["n","-",1]],["print","n"]]]))"""

"""print(exec_program([
        "calc",
        ["read", "x"],
        ["if", ["x", ">", 0], ["set", "a", 1], ["set", "a", -1]],
        ["if", ["x", "=", 0], ["set", "a", 1.5]],
    ]))"""

print(exec_program(["calc",["set","n",True],["print","n"]]))
"""print(exec_program([
    "calc",
    ["read", "n"],
    ["set", "sum", 1],
    [
        "while",
        [["n", "-", 1], ">", 0],
        ["set", "sum", ["sum", "*", "n"]],
        ["set", "n", ["n", "-", 1]],
    ],
    ["print", "sum"],
]))"""

#-- Error code --#
"""print(exec_program([
        "calc",
        ["read", "x"],
        ["if", ["he", ">", 0], ["set", "a", 1], ["set", "a", -1]],
        ["if", ["x", "=", 0], ["set", "a", 0]],
    ]))"""


"""print(exec_program([
        "calc",
        ["set", "x", 5],
        ["if", [[5,"%",5], "=", 5], ["set", "a", 1], ["set", "a", -1]],
        ["if", ["x", "=", 0], ["set", "a", 0]],
    ]))"""

    