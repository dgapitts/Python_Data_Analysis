### Ulysess Anagrams 

Exploring the logic in the Anagrams, I've been experimenting with "Ulysess Anagrams"

```
(base) ~/projects/Python_Data_Analysis $ cat docs/ulysess_anagrams.py
import re
import collections

print ("Welcome to the ulysses anagram search - this python scripts loads ulysses into memory (collections.defaultdict) and searches for anagrams.. enjoy")
words = []
# compute the signature string for a word
def signature(word):
    return ''.join(sorted(word))



#for line in open('docs/Ulysses-Jame-Joyce-1922-start.txt', 'r'):
for line in open('docs/Ulysses-Jame-Joyce-1922.txt', 'r'):
  for word in re.split('\s+',line):
    #print(word)
    #print(re.sub('[^A-Za-z0-9]+', '', word))
    #input("Press Enter to continue...")
    words.append(re.sub('[^A-Za-z0-9]+', '', word).lower())

ulysses_words=sorted(words)
ulysses_dict = collections.defaultdict(set)
for word in ulysses_words:
  ulysses_dict[signature(word)].add(word)


def find_anagram(myword):
    mysig = signature(myword)
    results=[]
    
    for word in ulysses_words:
        if mysig == signature(word):
            results.append(word)

    # https://geekflare.com/remove-duplicate-items-from-python-lists/
    unique_results = []
    [unique_results.append(word) for word in results if word not in unique_results]

    print(myword + ": " + str(unique_results))


find_anagram('dog')
find_anagram('dave')
find_anagram('davep')
```
and the results are

```
(base) ~/projects/Python_Data_Analysis $ time python3 docs/ulysess_anagrams.py
Welcome to the ulysses anagram search - this python scripts loads ulysses into memory (collections.defaultdict) and searches for anagrams.. enjoy
dog: ['dog', 'god']
dave: ['vade']
davep: ['paved']

real	0m2.309s
user	0m2.077s
sys	0m0.103s
```
