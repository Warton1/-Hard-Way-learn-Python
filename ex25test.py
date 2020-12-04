import ex25
sentence = "All good things come to those who wait."
words = ex25.break_words(sentence)
print (words)
sorted_words = ex25.sort_words(words)
print (sorted_words)
print (ex25.print_first_word(words))
print (ex25.print_last_word(words))
print (words)
print (ex25.print_first_word(sorted_words))
print (ex25.print_last_word(sorted_words))
print (sorted_words)
sorted_words = ex25.sort_sentence(sentence)
print (sorted_words)
print (ex25.print_first_and_last(sentence))
print (ex25.print_first_and_last_sorted(sentence))
# help(ex25)
help(ex25.break_words)

# import ex25
# sentence = "All good\tthings come to those who wait."

# words = ex25.break_words(sentence)
# sorted_words = ex25.sort_words(words)

# print_first_word(words)
# print_last_word(words)
# print_first_word(sorted_words)
# print_last_word(sorted_words)
# sorted_words = ex25.sort_sentence(sentence)
# print (sorted_words)

# print_first_and_last(sentence)

# print_first_and_last_sorted(sentence) 