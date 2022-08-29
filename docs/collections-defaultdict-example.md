## Collections default-dict

> There's another variant of dict that remains useful, collections default dict. The point here is to define a default for values that will be returned if we ask for a key for which there was no entry. More precisely, we have to provide a function that returns that default. 

Simple demo code
```
~/projects/Python_Data_Analysis $ cat docs/collections-defaultdict-example.py
## collections-defaultdict-example.py
import collections

def mydefault():
    return "unknown"

questions = collections.defaultdict(mydefault)

questions['The meaning of life']

print(questions)
```
and running this:

```
~/projects/Python_Data_Analysis $ python3 docs/collections-defaultdict-example.py
defaultdict(<function mydefault at 0x7fd25daa4c10>, {'The meaning of life': 'unknown'})
```