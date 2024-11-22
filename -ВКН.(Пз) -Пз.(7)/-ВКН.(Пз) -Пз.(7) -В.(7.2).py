N = int(input("Введіть кількість слів: "))

words = []
for _ in range(N):
    word = input("Введіть слово: ")
    spaced_word = ' '.join(word)
    words.append(spaced_word)


result = ', '.join(words)


print("Результат:", result)
