# Python Program: 
# CSC505: Principles of Software Development
# Module 6: Critical Thinking
# Professor: Dr. Bingdong Li 
# Created by Mukul Mondal
# Saturday, Aug 23, 2025

'''
Problem statement:
-- Stepwise Refinement Approach --

Apply a “stepwise refinement approach” to develop three 
different levels of procedural abstractions for the  programs:
Iteratively solve for the roots of a transcendental equation.
'''


from os import system, name
import math


# This is just a helper function to clear the screen
# This is not required, per problem statement.
def clearScreen():
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    return

# original function from the equation to solve
def f(x):
    return math.cos(x) - x

# derivative of the original function
def df(x):
    return -math.sin(x) - 1

# function for final solution
def solve_root(x0: float, tol:float=1e-6, max_iter:int=100)->float:
    x: float = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Derivative is zero. No convergence.")
        x_new = x - fx / dfx
        if abs(fx) < tol:
            return x_new
        x = x_new
    raise ValueError("Did not converge within max iterations.")


# Caller of the solution function
def execute_module6_ct_Level3_LowLevel_CodeImplementation():
    r0: float = 0.5 # default initial guess of the root
    
    # Just provide option to the user for entering better guess for the initial root.
    # If 'user input' is not better than 0.5(default initial guess of the root), I'll proceed with the default initial value.
    try:
        r0 = float(input('Enter assumed initial root(optional input): '))     # for 'float' data types
    except ValueError:
        r0 = 0.5
    if r0 < 0.5:
        r0 = 0.5
    elif r0 > 0.7:
        r0 = 0.5
    
    root = solve_root(r0)
    print(f"Approximate root: {root}")
    return


if __name__ == "__main__":
    clearScreen()
    print("=== Module 6: Critical Thinking. Stepwise Refinement Approach to solve: transcendental equation ===")    
    execute_module6_ct_Level3_LowLevel_CodeImplementation()
