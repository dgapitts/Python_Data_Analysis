import re
words = []
for line in open('docs/Ulysses-Jame-Joyce-1922.txt', 'r'):
  for word in re.split('\s+',line):
    print(word)
    print(re.sub('[^A-Za-z0-9]+', '', word))
    input("Press Enter to continue...")
    words.append(word)

