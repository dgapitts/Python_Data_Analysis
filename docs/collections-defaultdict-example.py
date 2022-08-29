## collections-defaultdict-example.py
import collections

def mydefault():
    return "unknown"

questions = collections.defaultdict(mydefault)

questions['The meaning of life']

print(questions)
