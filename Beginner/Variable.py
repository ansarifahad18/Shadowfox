# -----------------------------------------
# Question 1: Store 22/7 in a variable pi and check its type
# -----------------------------------------

pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))


# -----------------------------------------
# Question 2: Try creating a variable named 'for'
# -----------------------------------------

print("\nQuestion 2:")
print("We cannot create a variable named 'for' because it is a reserved keyword in Python.")
# The following line would cause an error:
# for = 4
# SyntaxError: invalid syntax

# To show the list of all Python keywords,
import keyword
print("Python keywords:", keyword.kwlist)


# Question 3: Calculate Simple Interest
# Formula: SI = (P * R * T) / 100

P = 10000   
R = 5       
T = 3       

SI = (P * R * T) / 100

print("\nSimple Interest Calculation:")
print("Principal (P):", P)
print("Rate of Interest (R):", R)
print("Time (T):", T)
print("Simple Interest:", SI)
