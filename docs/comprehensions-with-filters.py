print("Rerunning using comprehensions (more pythonic)")
squares = [i**2 for i in range(1, 11)]
print(squares) 
 
# comprehensions (more pythonic) 
print("Rerunning using comprehensions with filter (square is divisible by 4 )")
squares2 = [i**2 for i in range(1, 11) if (i**2)%4==0]
print(squares2) 