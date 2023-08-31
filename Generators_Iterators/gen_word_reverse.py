def word_reverser(word):
    # for c in word[::-1]:
    #     if c.lower() in 'aeiou':
    #         yield c
    return (word[i] for i in range(len(word) - 1, -1, -1) if word[i].lower() in "aeiouy")

     
for c in word_reverser("Study"):
    print(c, end=" ")