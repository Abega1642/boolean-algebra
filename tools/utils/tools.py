def boolean_value(val) :
    return 1 if val == True else 0

def negation_form(expression) :
    expression = expression.split("*")
    expression = [f"(not {e})" if len(e) == 1 else e[len(e) - 2] for e in expression]
    return " + ".join(expression)

def assign_variables(variables, values):
    return {var: val for var, val in zip(variables, values)}