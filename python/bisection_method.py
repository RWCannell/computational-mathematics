def f(x):
    return x**3 + 3*x**2 - x - 1

def bisection_method(start_of_interval, end_of_interval, tolerance):
    a = start_of_interval
    b = end_of_interval
    maximum_number_of_iterations = 10

    number_of_iterations = 1
    f_a = f(a)

    message = f"Method failed after {number_of_iterations} iterations. Could not find root in interval [{start_of_interval}, {end_of_interval}]."

    while number_of_iterations <= maximum_number_of_iterations:
        c = (a + b)/2
        f_c = f(c)
        if f_c == 0 or (b - a)/2 < tolerance:
            message = f"Found root at point x={c} in interval [{start_of_interval}, {end_of_interval}] after {number_of_iterations} iterations."
            break
        
        number_of_iterations += 1
        if f_a*f_c > 0:
            a = c
            f_a = f_c
        else:
            b = c

    return message

if __name__ == "__main__":
    approximate_solution = bisection_method(0, 1, 0.01)
    print(f"{approximate_solution}")
    