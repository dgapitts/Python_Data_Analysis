import re
import collections

words = []
# compute the signature string for a word
def signature(word):
    return ''.join(sorted(word))



for line in open('docs/Ulysses-Jame-Joyce-1922-start.txt', 'r'):
#for line in open('docs/Ulysses-Jame-Joyce-1922.txt', 'r'):
  for word in re.split('\s+',line):
    #print(word)
    #print(re.sub('[^A-Za-z0-9]+', '', word))
    #input("Press Enter to continue...")
    words.append(re.sub('[^A-Za-z0-9]+', '', word).lower())

ulysses_words=sorted(words)
ulysses_dict = collections.defaultdict(set)
for word in ulysses_words:
  ulysses_dict[signature(word)].add(word)


print("*** words:" + str(len(words)))
print(words)
print("*** ulysses_words:" + str(len(ulysses_words)))
print(ulysses_words)
print("*** ulysses_dict:" + str(len(ulysses_dict)))
print(ulysses_dict)



