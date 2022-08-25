## Regular iterator loop vs comprehensions ("more pythonic")


Some notes from [chapter2/02_04_comprehensions.ipynb](../chapter2/02_04_comprehensions.ipynb), to demo this I've used regular python

```
~/projects/Python_Data_Analysis $ cat docs/regular-iterator-loop-vs-comprehensions.py

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
```

and as expected
```
~/projects/Python_Data_Analysis $ python3 docs/regular-iterator-loop-vs-comprehensions.py
First using regular iterator
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Rerunning using comprehensions (more pythonic)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```