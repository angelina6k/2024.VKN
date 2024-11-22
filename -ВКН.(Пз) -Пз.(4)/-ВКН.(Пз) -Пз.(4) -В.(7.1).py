import math

def calculate_f(x):
    try:
        numerator = math.exp(x**2)  
        denominator = math.cos(x + x**4)
        if denominator == 0:
            raise ValueError("Division by zero encountered in the denominator.")
        term1 = numerator / denominator  
        term2 = x**(1/4)  
        term3 = x**3 

      
        result = term1 - term2 + term3
        return result
    except ValueError as e:
        return f"Error: {e}"


x = 1.5
print(f"f({x}) = {calculate_f(x)}")