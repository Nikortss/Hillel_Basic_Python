def word_count(sentence):
    length = len(sentence)
    word_list = len(sentence.split())
    return length, word_list


sentence = input('Enter your sentence: ')
length, word_list = word_count(sentence)
print(f'Number of characters: {length}')
print(f'Number of words: {word_list}')
