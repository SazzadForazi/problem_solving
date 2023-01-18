s = "i like this program very much"
print(s)
words=s.split(' ')
print(words)
string = []
for word in words:
    string.append(word)
    #  print(word)

    # string.insert(0,word)
print(" ".join(string))
