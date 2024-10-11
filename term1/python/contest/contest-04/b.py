words = input().split()
word_frequency = {}
for i in words:
    if i in word_frequency:
        word_frequency[i] += 1
    else:
        word_frequency[i] = 1
word_frequency_key = list(word_frequency.keys())
word_frequency_key.sort()
for i in word_frequency_key:
    print(f'{i} {word_frequency[i]}')
