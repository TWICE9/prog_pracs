# text = "this is a collection of words of nice words this is a fun thing it is"

words_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    amount = words_to_count.get(word, 0)
    words_to_count[word] = amount + 1

words = list(words_to_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, words_to_count[word]))
