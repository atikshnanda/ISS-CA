def find_cube_pairs(target):
    solutions = []
    max_num = round(target ** (1/3)) + 1  # Added +1 to ensure we check up to the cube root, and fixed typo in variable name

    for a in range(1, max_num + 1):  # Changed 'ranges' to 'range' (correct Python function)
        for b in range(a, max_num + 1):  # Changed 'ranges' to 'range'
            if a**3 + b**3 == target:  # Fixed operator from *** to ** for exponentiation
                solutions.append((a, b))  # Fixed variable name from 'sol' to 'solutions'
    return solutions

pairs = find_cube_pairs(1729)  # Removed comma that made this a tuple
print("Valid cube pairs for 1729:")  # Changed 'printf' to 'print' and fixed the target number
for a, b in pairs: # added a colon
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729") # changed 2 with 3 and corrected the target number and syntax of print
