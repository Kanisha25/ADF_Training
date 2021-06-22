import re
try:
    class day2:
        def prefix(self, a):
            count = 0
            for i in a:
                if (i.startswith("To")):
                    count = count + 1
            print(count)
            with open("output1.txt", "a") as f1:
                f1.write("The number of words having prefix with To in the input file is " + str(count)+"\n")
                f1.close()

        def suffix(self, words):
            countsuff = 0
            for i in words:
                if (i.endswith("ing")):
                    countsuff = countsuff + 1
            print(countsuff)
            with open("output1.txt", "a") as f1:
                f1.write("The number of words ending with ing in the input file is " + str(countsuff)+"\n")
                f1.close()

        def maximum(self,words):
            countm = 0;
            word = "";
            maxCount = 0;
            for i in range(0, len(words)):
                countm = 1;
                for j in range(i + 1, len(words)):
                    if (words[i] == words[j]):
                        countm = countm + 1;

                if (countm > maxCount):
                    maxCount = countm;
                    word = words[i];
            print("Most repeated word: " + word);
            with open("output1.txt", "a") as f1:
                f1.write("The word that was repeated maximum number of times " + word+"\n")
                f1.close()

        def palindrome(self,words):
            pal = []
            for s in words:
                s1 = s[::-1]
                if s1 == s and s != "":
                    pal.append(s)
            print(pal)
            with open("output1.txt", "a") as f1:
                f1.write("The palindrome present in the file "+str(pal)+"\n")
                f1.close()

        def uniquewords(self,words):
            unique = []
            for word in words:
                if word not in unique:
                    unique.append(word)
            print(unique)
            with open("output1.txt", "a") as f1:
                f1.write("All words into unique list is " + str(unique)+"\n")
                f1.close()

        def counterindex(self,words):
            dict = {}
            dict = list(enumerate(words))
            print(dict)
            with open("output1.txt", "a") as f1:
                f1.write("List by using enumeration and counter index is " + str(dict)+"\n")
                f1.close()

        def splitwords(self,words):
            split = []
            for i in words:
                res = re.split('a|e|i|o|u', i)
                split.append(res)
            print("The splitted string : " + str(split))
            with open("output2.txt", "a") as f2:
                f2.write("Splitted text based on vowels is " + str(split)+"\n")
                f2.close()

        def CapitalizeCharacter(self,words):
            cap = []
            for i in words:
                a = list(i)
                a[2::3] = [x.upper() for x in a[2::3]]
                i = ''.join(a)
                cap.append(i)
            print(cap)
            with open("output2.txt", "a") as f2:
                f2.write("Splitted text based on vowels is " + str(cap)+"\n")
                f2.close()

        def Capitalize5thWord(self, words):
            for i in range(4, len(words), 5):
                words[i] = words[i].upper()
            print(words)
            with open("output2.txt", "a") as f2:
                f2.write("Capitalized every 5th word " + str(words)+"\n")
                f2.close()

        def ReplaceSpace(self, words):
            listToStr = ' '.join([str(i) for i in words])
            listToStr = listToStr.replace(" ", "_")
            print(listToStr)
            with open("output2.txt", "a") as f2:
                f2.write("Replaced Space with String is " + str(listToStr)+"\n")
                f2.close()



    x = input("Enter file name ")
    text_file = open(x, 'r')
    text = text_file.read()
    words = text.split()
    words = [word.strip('.,!;()[]') for word in words]
    words = [word.replace("'s", '') for word in words]

    obj = day2()
    obj.prefix(words)
    obj.suffix(words)
    obj.maximum(words)
    obj.palindrome(words)
    obj.uniquewords(words)
    obj.counterindex(words)
    obj.splitwords(words)
    obj.CapitalizeCharacter(words)
    obj.Capitalize5thWord(words)
    obj.ReplaceSpace(words)

except IOError :
    print("File not found")