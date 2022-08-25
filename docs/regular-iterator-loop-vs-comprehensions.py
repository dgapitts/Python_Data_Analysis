
# regular iterator loop vs comprehensions
# list of the squares from 1^2 to 10^2; note power is ** in Python

# regular iterator
print("First using regular iterator")
squares = []
for i in range(1, 11):
    squares.append(i**2)
print(squares) 

# comprehensions (more pythonic) 
print("Rerunning using comprehensions (more pythonic)")
squares2 = [i**2 for i in range(1, 11)]
print(squares2) 