import numpy as np

file = open("rt-pol.txt",'r')
N = 0
all_word = []
for line in file:
    ar = line.rstrip('\n').split(" ")
    all_word += ar
    print ar 
    N +=1
all_word = list(set(all_word))
print all_word
print len(all_word)

print all_word.index("and")

t = np.zeros([N,len(all_word)])

for i, line in enumerate(open("rt-pol.txt",'r')):
    ar = line.rstrip("\n").split(" ")
    for w in ar:
        print w
        t[i][all_word.index(w)] += 1

print t