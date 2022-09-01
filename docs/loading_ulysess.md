## loading Ulysess - a dictionary for all the anagrams for the words in Ulysess

This is a fun but fiddly exercise
* Following the logic in [chapter3/03_02_loadingtext.ipynb](../chapter3/03_02_loadingtext.ipynb)
* However I want a dictionary for all the anagrams for the words in Ulysess
* Started with the just 30 lines 

### Ulysses-Jame-Joyce-1922-start

```
(base) ~/projects/Python_Data_Analysis $ head -100 docs/Ulysses-Jame-Joyce-1922.txt|tail -30 > docs/Ulysses-Jame-Joyce-1922-start.txt
(base) ~/projects/Python_Data_Analysis $ cat docs/Ulysses-Jame-Joyce-1922-start.txt 

[ 1 ]

Stately, plump Buck Mulligan came from the stairhead, bearing a bowl of
lather on which a mirror and a razor lay crossed. A yellow
dressinggown, ungirdled, was sustained gently behind him on the mild
morning air. He held the bowl aloft and intoned:

—_Introibo ad altare Dei_.

Halted, he peered down the dark winding stairs and called out coarsely:

—Come up, Kinch! Come up, you fearful jesuit!

Solemnly he came forward and mounted the round gunrest. He faced about
and blessed gravely thrice the tower, the surrounding land and the
awaking mountains. Then, catching sight of Stephen Dedalus, he bent
towards him and made rapid crosses in the air, gurgling in his throat
and shaking his head. Stephen Dedalus, displeased and sleepy, leaned
his arms on the top of the staircase and looked coldly at the shaking
gurgling face that blessed him, equine in its length, and at the light
untonsured hair, grained and hued like pale oak.

Buck Mulligan peeped an instant under the mirror and then covered the
bowl smartly.

—Back to barracks! he said sternly.

He added in a preacher’s tone:
```

### Developing loading_ulysess.py

```
(base) ~/projects/Python_Data_Analysis $ cat docs/loading_ulysess.py
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
```

and running this

```
(base) ~/projects/Python_Data_Analysis $ python3 docs/loading_ulysess.py
*** words:227
['', '', '', '1', '', '', '', '', 'stately', 'plump', 'buck', 'mulligan', 'came', 'from', 'the', 'stairhead', 'bearing', 'a', 'bowl', 'of', '', 'lather', 'on', 'which', 'a', 'mirror', 'and', 'a', 'razor', 'lay', 'crossed', 'a', 'yellow', '', 'dressinggown', 'ungirdled', 'was', 'sustained', 'gently', 'behind', 'him', 'on', 'the', 'mild', '', 'morning', 'air', 'he', 'held', 'the', 'bowl', 'aloft', 'and', 'intoned', '', '', '', 'introibo', 'ad', 'altare', 'dei', '', '', '', 'halted', 'he', 'peered', 'down', 'the', 'dark', 'winding', 'stairs', 'and', 'called', 'out', 'coarsely', '', '', '', 'come', 'up', 'kinch', 'come', 'up', 'you', 'fearful', 'jesuit', '', '', '', 'solemnly', 'he', 'came', 'forward', 'and', 'mounted', 'the', 'round', 'gunrest', 'he', 'faced', 'about', '', 'and', 'blessed', 'gravely', 'thrice', 'the', 'tower', 'the', 'surrounding', 'land', 'and', 'the', '', 'awaking', 'mountains', 'then', 'catching', 'sight', 'of', 'stephen', 'dedalus', 'he', 'bent', '', 'towards', 'him', 'and', 'made', 'rapid', 'crosses', 'in', 'the', 'air', 'gurgling', 'in', 'his', 'throat', '', 'and', 'shaking', 'his', 'head', 'stephen', 'dedalus', 'displeased', 'and', 'sleepy', 'leaned', '', 'his', 'arms', 'on', 'the', 'top', 'of', 'the', 'staircase', 'and', 'looked', 'coldly', 'at', 'the', 'shaking', '', 'gurgling', 'face', 'that', 'blessed', 'him', 'equine', 'in', 'its', 'length', 'and', 'at', 'the', 'light', '', 'untonsured', 'hair', 'grained', 'and', 'hued', 'like', 'pale', 'oak', '', '', '', 'buck', 'mulligan', 'peeped', 'an', 'instant', 'under', 'the', 'mirror', 'and', 'then', 'covered', 'the', '', 'bowl', 'smartly', '', '', '', 'back', 'to', 'barracks', 'he', 'said', 'sternly', '', '', '', 'he', 'added', 'in', 'a', 'preachers', 'tone', '', '', '']
*** ulysses_words:227
['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '1', 'a', 'a', 'a', 'a', 'a', 'about', 'ad', 'added', 'air', 'air', 'aloft', 'altare', 'an', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'arms', 'at', 'at', 'awaking', 'back', 'barracks', 'bearing', 'behind', 'bent', 'blessed', 'blessed', 'bowl', 'bowl', 'bowl', 'buck', 'buck', 'called', 'came', 'came', 'catching', 'coarsely', 'coldly', 'come', 'come', 'covered', 'crossed', 'crosses', 'dark', 'dedalus', 'dedalus', 'dei', 'displeased', 'down', 'dressinggown', 'equine', 'face', 'faced', 'fearful', 'forward', 'from', 'gently', 'grained', 'gravely', 'gunrest', 'gurgling', 'gurgling', 'hair', 'halted', 'he', 'he', 'he', 'he', 'he', 'he', 'he', 'head', 'held', 'him', 'him', 'him', 'his', 'his', 'his', 'hued', 'in', 'in', 'in', 'in', 'instant', 'intoned', 'introibo', 'its', 'jesuit', 'kinch', 'land', 'lather', 'lay', 'leaned', 'length', 'light', 'like', 'looked', 'made', 'mild', 'mirror', 'mirror', 'morning', 'mountains', 'mounted', 'mulligan', 'mulligan', 'oak', 'of', 'of', 'of', 'on', 'on', 'on', 'out', 'pale', 'peeped', 'peered', 'plump', 'preachers', 'rapid', 'razor', 'round', 'said', 'shaking', 'shaking', 'sight', 'sleepy', 'smartly', 'solemnly', 'staircase', 'stairhead', 'stairs', 'stately', 'stephen', 'stephen', 'sternly', 'surrounding', 'sustained', 'that', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'then', 'then', 'thrice', 'throat', 'to', 'tone', 'top', 'towards', 'tower', 'under', 'ungirdled', 'untonsured', 'up', 'up', 'was', 'which', 'winding', 'yellow', 'you']
*** ulysses_dict:123
defaultdict(<class 'set'>, {'': {''}, '1': {'1'}, 'a': {'a'}, 'abotu': {'about'}, 'ad': {'ad'}, 'addde': {'added'}, 'air': {'air'}, 'aflot': {'aloft'}, 'aaelrt': {'altare'}, 'an': {'an'}, 'adn': {'and'}, 'amrs': {'arms'}, 'at': {'at'}, 'aagiknw': {'awaking'}, 'abck': {'back'}, 'aabckrrs': {'barracks'}, 'abeginr': {'bearing'}, 'bdehin': {'behind'}, 'bent': {'bent'}, 'bdeelss': {'blessed'}, 'blow': {'bowl'}, 'bcku': {'buck'}, 'acdell': {'called'}, 'acem': {'came'}, 'accghint': {'catching'}, 'acelorsy': {'coarsely'}, 'cdlloy': {'coldly'}, 'cemo': {'come'}, 'cdeeorv': {'covered'}, 'cdeorss': {'crossed'}, 'ceorsss': {'crosses'}, 'adkr': {'dark'}, 'addelsu': {'dedalus'}, 'dei': {'dei'}, 'addeeilpss': {'displeased'}, 'dnow': {'down'}, 'degginnorssw': {'dressinggown'}, 'eeinqu': {'equine'}, 'acef': {'face'}, 'acdef': {'faced'}, 'aefflru': {'fearful'}, 'adforrw': {'forward'}, 'fmor': {'from'}, 'eglnty': {'gently'}, 'adeginr': {'grained'}, 'aeglrvy': {'gravely'}, 'egnrstu': {'gunrest'}, 'gggilnru': {'gurgling'}, 'ahir': {'hair'}, 'adehlt': {'halted'}, 'eh': {'he'}, 'adeh': {'head'}, 'dehl': {'held'}, 'him': {'him'}, 'his': {'his'}, 'dehu': {'hued'}, 'in': {'in'}, 'ainnstt': {'instant'}, 'deinnot': {'intoned'}, 'biinoort': {'introibo'}, 'ist': {'its'}, 'eijstu': {'jesuit'}, 'chikn': {'kinch'}, 'adln': {'land'}, 'aehlrt': {'lather'}, 'aly': {'lay'}, 'adeeln': {'leaned'}, 'eghlnt': {'length'}, 'ghilt': {'light'}, 'eikl': {'like'}, 'dekloo': {'looked'}, 'adem': {'made'}, 'dilm': {'mild'}, 'imorrr': {'mirror'}, 'gimnnor': {'morning'}, 'aimnnostu': {'mountains'}, 'demnotu': {'mounted'}, 'agillmnu': {'mulligan'}, 'ako': {'oak'}, 'fo': {'of'}, 'no': {'on'}, 'otu': {'out'}, 'aelp': {'pale'}, 'deeepp': {'peeped'}, 'deeepr': {'peered'}, 'lmppu': {'plump'}, 'aceehprrs': {'preachers'}, 'adipr': {'rapid'}, 'aorrz': {'razor'}, 'dnoru': {'round'}, 'adis': {'said'}, 'aghikns': {'shaking'}, 'ghist': {'sight'}, 'eelpsy': {'sleepy'}, 'almrsty': {'smartly'}, 'ellmnosy': {'solemnly'}, 'aaceirsst': {'staircase'}, 'aadehirst': {'stairhead'}, 'airsst': {'stairs'}, 'aelstty': {'stately'}, 'eehnpst': {'stephen'}, 'elnrsty': {'sternly'}, 'dginnorrsuu': {'surrounding'}, 'adeinsstu': {'sustained'}, 'ahtt': {'that'}, 'eht': {'the'}, 'ehnt': {'then'}, 'cehirt': {'thrice'}, 'ahortt': {'throat'}, 'ot': {'to'}, 'enot': {'tone'}, 'opt': {'top'}, 'adorstw': {'towards'}, 'eortw': {'tower'}, 'denru': {'under'}, 'ddegilnru': {'ungirdled'}, 'dennorstuu': {'untonsured'}, 'pu': {'up'}, 'asw': {'was'}, 'chhiw': {'which'}, 'dgiinnw': {'winding'}, 'ellowy': {'yellow'}, 'ouy': {'you'}})
(base) ~/projects/Python_Da
```



