import math

def calc_math_expression(num1, num2, operator):
    
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == ":":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return None
    else:
        return None

def calc_math_expression_from_str(string):
    contents = string.split()
    number_1 = float(contents[0])
    number_2 = float(contents[2])
    operator = contents[1]
    return(calc_math_expression(number_1,number_2,operator))

def find_largest_and_smallest_numbers(num1,num2,num3):
    num_array = []
    num_array.append(num1)
    num_array.append(num2)
    num_array.append(num3)
    num_array.sort()
    return(num_array[2],num_array[0])

def quadratic_equation_solver(a, b, c):
    d = (b**2) - (4*a*c)
    try:
        sol1 = (-b-math.sqrt(d))/(2*a)
        sol2 = (-b+math.sqrt(d))/(2*a)
        if sol1 == sol2:
            return (sol1,None)
        else:
            return(sol2,sol1)
    except ValueError:
        return(None,None)    
    
def quadratic_equation_solver_from_user_input():
    
    get_input = input("Input the Variables")
    constants = get_input.split(" ")
    a = float(constants[0])
    b = float(constants[1])
    c = float(constants[2])
    return (quadratic_equation_solver(a,b,c))

def temp_checker(min_temp, temp_1, temp_2, temp_3):
    if temp_1 > min_temp or temp_2 >min_temp or temp_3 > min_temp:
        return True
    else:
        return False
