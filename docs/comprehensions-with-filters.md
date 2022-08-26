## Comprehensions with Filters

TLDR `squares2 = [i**2 for i in range(1, 11) if (i**2)%4==0]`

> We can also filter the list of elements that we are creating by adding an if clause. For instance, we may want to collect only the squares that are divisible by four, which in fact, I need to do with the modulus operator.  

and running
```
~/projects/Python_Data_Analysis $ cat docs/comprehensions-with-filters.py
print("Rerunning using comprehensions (more pythonic)")
squares = [i**2 for i in range(1, 11)]
print(squares) 
 
# comprehensions (more pythonic) 
print("Rerunning using comprehensions with filter (square is divisible by 4 )")
squares2 = [i**2 for i in range(1, 11) if (i**2)%4==0]
```

gives
```
~/projects/Python_Data_Analysis $ python3 docs/comprehensions-with-filters.py
Rerunning using comprehensions (more pythonic)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Rerunning using comprehensions with filter (square is divisible by 4 )
[4, 16, 36, 64, 100]
```