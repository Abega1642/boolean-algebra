import re
import itertools
from utils.tools import boolean_value, negation_form, assign_variables
    


def logical_function_boolean_value(logical_function_input, variables):
    for var, val in variables.items():
        logical_function_input = re.sub(
            r'\bnot_{}\b'.format(re.escape(var)),
            'not {}'.format(var),
            logical_function_input
        )
        logical_function_input = re.sub(
            r'\bnot\s+{}'.format(re.escape(var)),
            'not {}'.format(var),
            logical_function_input
        )
        logical_function_input = re.sub(
            r'\b{}\b'.format(re.escape(var)),
            str(val), logical_function_input
        )

    return boolean_value(eval(logical_function_input))


def first_canonic_form_function(values, result,variables) :
    expression = []
    for value, letter in zip(values, variables):
        if value == 0:
            expression.append(f"(not {letter})")
        else:
            expression.append(letter)
    expression_str = '*'.join(expression)
    result.append(expression_str)

def second_canonic_form_function(values, result, variables):
    expression = []
    for value, letter in zip(values, variables):
        if value == 0:
            expression.append(f"(not {letter})")
        else:
            expression.append(letter)
    expression_str = '*'.join(expression)
    expression_str = negation_form(expression_str)
    expression_str = f'[{expression_str}]'
    result.append(expression_str)

def possible_values(variables_number):
    return list(itertools.product([1, 0], repeat=variables_number))

def table_of_truth() :
    variables_number = int(input("\nPlease enter the number of variable of your logical function ?  → "))

    variables = []
    for i in range(variables_number):
        nom_variable = input(f"Please, enter the name of the variable number {i+1}: ").strip()
        variables.append(nom_variable)

    logical_function_input = input(
        "Please enter your logical function. ('not' or 'not_' : negation, 'and', 'or')\n\t ==> f({}) = "
        .format(",".join(variables))
    )
    
    print('\n\t==== TABLE OF TRUTH --- TABLE DE VERITE ==== \n')
    line_one = "  ||  ".join([f"{i}" for i in variables] + [f'f({",".join(variables)}) = {logical_function_input}'])  
    print(line_one)
    print("=" * len(line_one))
    
    first_canonic_form = []
    second_canonic_form = []
    
    for values in possible_values(variables_number):
        lines = "  ||  ".join(str(value) for value in values)
        boolean_value_of_the_function = boolean_value(
            logical_function_boolean_value(logical_function_input, assign_variables(variables, values))
        )
        if boolean_value_of_the_function == 1:
            first_canonic_form_function(values, first_canonic_form, variables)   
        else :
            second_canonic_form_function(values, second_canonic_form,variables)
        print(f"{lines}  ||         {boolean_value_of_the_function}")
    
    first_canonic_form = " + ".join(first_canonic_form)
    second_canonic_form = " * ".join(second_canonic_form)
    
    print(
        '\n==> The first canonic form of the logical function is : f({}) = : {}'
        .format(",".join(variables), first_canonic_form)
    )

    print(
        '\n==> The second canonic form of the logical function is f({}) = : {}\n'
        .format(",".join(variables), second_canonic_form)
    )
table_of_truth()