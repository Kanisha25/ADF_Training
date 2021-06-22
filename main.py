# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


text_file = open('assesment1.txt', 'r')
text = text_file.read()

#cleaning
text = text.lower()
words = text.split()
words = [word.strip('.,!;()[]') for word in words]
words = [word.replace("'s", '') for word in words]

#finding unique
unique = []
for word in words:
    if word not in unique:
        unique.append(word+str(len(word)))

#sort
unique.sort(key = len)

#print
print(unique)
with open("assesment1write.txt", "w") as f1:
    for l in unique:
        f1.write(l+" ")

