#converts binary number to decimal
def binary_to_decimal(binary:float):
    decimal: float = 0
    i = 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal

#finds absolute error
def absolute_error(precise:float, approximate: float):
    sub_operation = precise - approximate
    return abs(sub_operation)

#finds relative error
def relative_error(precise: float, approximate: float):
    sub_operation = absolute_error(precise, approximate)
    div_operation = sub_operation / precise
    return div_operation





# bisection method
def bisection_method(left: float, right: float, given_function: str):
    x = left
    intial_left = eval(given_function)
    x = right
    intial_right = eval(given_function)
    if intial_left * intial_right >= 0:
        print("Invalid inputs. Not on opposite sides of the function")
        return
    tolerance: float = .003
    diff: float = right - left
    max_iterations = 20
    iteration_counter = 0
    while (diff >= tolerance and iteration_counter <= 20):
        iteration_counter += 1
        # find function(midpoint)
        mid_point = (left + right) / 2
        x = mid_point
        evaluated_midpoint = eval(given_function)
        if evaluated_midpoint == 0.0:
            break

        # find function(left)
        x = left
        evaluated_left_point = eval(given_function)

        # this section basically checks if we have crossed the origin point another way
        # to describe this is if f(midpoint) * f(left_point) changed signs)
        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint > 0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint< 0
        if first_conditional or second_conditional:
            right = mid_point
        else:
            left = mid_point

        diff = abs(right - left)

#Newton Raphson method using iteration
def f (x: float):
    solution = (x**3) + (4*x**2) - 10
    return solution

def dfdx (x: float):
    solution = (3*x**2) + (8*x)
    return solution

def newton_raphson (x0: float, tol: float):
    num_iterations: float = 0
    approximation: float = x0

    while (abs(f(approximation)) > tol):
        xi = approximation - (f(approximation) / dfdx(approximation))
        approximation = xi
        num_iterations += 1

    return num_iterations

if __name__ == "__main__":

# 1) Use double precision, calculate the resulting values (format to 5 decimal places)
# (a) 010000000111111010111001
    solution_1 = binary_to_decimal(10000000111111010111001)
    print(solution_1)
    print()

# 2) Repeat exercise 1 using three-digit chopping arithmetic

#xxx

# 3) Repeat exercise 1 using three-digit rounding arithmetic

#xxx

# 4) Compute the absolute and relative error with the exact value from question 1 and its 3 digit rounding

#xxx

# 5) What is the minimum number of terms needed to computer f(1) with error < 10-4?

#xxx

# 6) Determine the number of iterations necessary to solve f(x) = x3 + 4x2 – 10 = 0 with
# accuracy 10-4 using a = -4 and b = 7.
    tolerance = 1E-4

# (a) Using the bisection method
    left: float = -4
    right: float = 7
    function: str = "(x**3) + (4*x**2) - 10"
    num: float = bisection_method(left, right, function)

    print("Number of Iterations for bisection: ",num)
    print()

# (b) Using the Newton Raphson method
    initial_approximation: float = -4
    a: float = newton_raphson(initial_approximation, tolerance)

    initial_approximation: float = 7
    b: float = newton_raphson(initial_approximation, tolerance)

    print(a)
    print(b)