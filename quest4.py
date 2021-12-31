text = input("Введи  предложение: ")
word = []
number = 1
for element in range(text.count(' ') + 1):
    word = text.split()
    if len(str(word)) <= 10:
        print(f" {number} {word [element]}")
        number += 1
    else:
        print(f" {number} {word [element] [0:10]}")
        number += 1