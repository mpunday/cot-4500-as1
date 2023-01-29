def truncate(number: float, digits: int) -> float:
    pow10 = 10 ** digits
    return number * pow10 // 1 / pow10

def absolute_error(precise:float, approximate: float):
    diff = precise - approximate
    return abs(diff)

def relative_error(precise:float, approximate: float):
    diff = absolute_error(precise, approximate)
    ratio = diff / precise
    return ratio

def function_5 (x, n):
    result = (-1)**(n+1)*((x**(n+1))/(n+1)**3)
    return result


def bisection_method(left: float, right: float, tolerance: float, function: str):
    # verify starting values are on opposite sides of root
    x = left
    intial_left = eval(function)
    x = right
    intial_right = eval(function)
    if intial_left * intial_right >= 0:
        print("Invalid inputs. Not on opposite sides of the root")
        return 0

    diff: float = abs(right - left)
    num_iterations: float = 0
    max_num_iterations: float = 20

    while ((diff >= tolerance) and (num_iterations <= max_num_iterations)):
        # find midpoint
        mid = (left + right) / 2

        # find f(mid)
        x = mid
        value_mid = eval(function)
        if value_mid == 0.0:
            break

        # find f(left)
        x = left
        value_left = eval(function)

        # find f(right)
        x = right
        value_right = eval(function)

        # replace either left or right value with mid value that is on opposite side of root
        if (value_left < 0 and value_mid > 0) or (value_left > 0 and value_mid < 0):
            right = mid
        else:
            left = mid

        # find new difference
        diff = abs(right - left)
        num_iterations += 1
    return num_iterations

def newton_raphson(initial_approximation: float, tolerance: float, function: str, function_prime: str):
    num_iterations = 0
    x = initial_approximation

    # finds f
    f = eval(function)

    # finds f'
    f_prime = eval(function_prime)

    # find approximation
    approximation: float = f / f_prime

    while (abs(approximation) >= tolerance):
        # finds f
        f = eval(function)
        # finds f'
        f_prime = eval(function_prime)
        # find approximation
        approximation = f / f_prime
        # subtraction property
        x -= approximation
        num_iterations += 1
    return num_iterations

if __name__ == "__main__":

# (1) Use double precision, calculate the resulting values (format to 5 decimal places)
# (a) 010000000111111010111001
    number: str = '010000000111111010111001'
    length: float = len(number)
    i: int = 12

    s: float = int(number[0])
    c: float = int(number[1:12],2)
    f: float = 0
    while (i < length):
        if (number[i] == '1'):
            f = f + (.5**(i-11))
        i += 1

    sol_1 = ((-1)**s)*(2**(c-1023))*(1+f)
    print(sol_1)
    print()

# (2) Repeat exercise 1 using three-digit chopping arithmetic
    sol_2 = truncate(sol_1,3-3)
    print(sol_2)
    print()

# (3) Repeat exercise 1 using three-digit rounding arithmetic
    sol_3: float = float('{:g}'.format(float('{:.{p}g}'.format(sol_1, p=3))))
    print(sol_3)
    print()

# (4) Compute the absolute and relative error with the exact value from question 1 and its 3 digit rounding
    precise: float = sol_1
    approx: float = sol_3
    print(absolute_error(precise, approx))
    print(relative_error(precise, approx))
    print()

# (5) What is the minimum number of terms needed to computer f(1) with error < 10-4?
    tolerance = .0001
    n: int = 0

    while (abs(function_5(1,n)) >= tolerance):
        n += 1
    print (n)
    print ()

# (6) Determine the number of iterations necessary to solve f(x) = x3 + 4x2 – 10 = 0
# with accuracy 10-4 using a = -4 and b = 7.
    tolerance: float = .0001
    a: float = -4
    b: float = 7
    function_6: str = "(x**3) + (4*x**2) - 10"
    function_6_prime: str = "(3*x**2) + (8*x)"

# (a) Using the bisection method
    sol_6a: float = bisection_method(a, b, tolerance, function_6)
    print(sol_6a)
    print()

# (b) Using the Newton Raphson method
    sol_6b: float = newton_raphson(a, tolerance, function_6, function_6_prime)
    print(sol_6b)
