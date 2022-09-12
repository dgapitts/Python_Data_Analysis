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




