word = input("input the word :")
word_list = list(word)

result = []

for _ in range(len(word_list)):
    result.append(word_list.pop())

print(word[::-1])
