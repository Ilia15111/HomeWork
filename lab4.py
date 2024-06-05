word = "автограф"
word_set = set(word)

dict = []
file = open("nouns.txt")

for line in file:  

    ll = len(line.rstrip())
    i = 0
    while ll > i:
        a = line[i]
        if word.find(a) >= 0:
            i+=1
        else:
            break
    if i == ll:
        dict.append(line)
    i = 0

sort_key = lambda s: (-len(s), s)
dict.sort(key=sort_key)


for i in range(len(dict)):
    print(i+1, " = ", dict[i])
