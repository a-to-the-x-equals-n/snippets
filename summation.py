from sympy import symbols, summation

# Define the variable and expression for the summation
k, n = symbols('k n')
expression = 4*k + 1

# Calculate the summation
summation_expr = summation(expression, (k, 0, n))
print(summation_expr.simplify())