first_8 = 'Captain Ruby'[:8]
new_str = first_8 + 'Python'
print(new_str)      # Captain Python

all_words = 'Captain Ruby'.split(' ')
first_word = all_words[0]
new_str = first_word + ' Python'
print(new_str)      # Captain Python

new_str = 'Captain Ruby'.replace('Ruby', 'Python')
print(new_str)      # Captain Python