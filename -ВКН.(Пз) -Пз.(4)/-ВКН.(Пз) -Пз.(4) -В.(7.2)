import math

def calculate_z(x, y, a, t):
    try:
        pi_factor = 2.33 * math.pi

        
        term1 = x * math.sin(y) 
        term2 = y * math.cos(a)  
        term3 = math.exp(a * t)  

        z = pi_factor * (term1 + term2) + term3
        return z
    except Exception as e:
        return f"Error: {e}"


x = 1.0
y = 1.0
a = 0.5
t = 2.0
print(f"Z = {calculate_z(x, y, a, t)}")