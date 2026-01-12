sentence = input("Enter the sentence: ")
words = sentence.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

for word, count in freq.items():
    print(f"{word} : {count}")