sentence = input().split(' ')

sentence[:] = (f'{word[1:]}{word[0]}ay' for word in sentence)

print(' '.join(sentence))
