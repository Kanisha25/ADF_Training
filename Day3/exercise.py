import re
import logging
import config as cfg

logging.basicConfig(
    filename="test.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
)
class A(object):
    def __init__(self, filename):
        self.filename = filename

    def readfile(self):
        f = open(self.filename)
        text = f.read()
        text = text.split()
        return text

    def writefile(self, word):
        with open(y, "a") as f1:
            f1.write(str(word) + "\n")
            f1.close()

class B(A):
    #def __init__(self, filename):
       # A.__init__(self, filename)

    def prefix(self):
        text = self.readfile()
        count = 0
        for i in text:
            if (i.startswith('To')):
                count = count + 1
        self.printMeth(count)
        self.writefile(count)
        logging.info(count)

    def suffix(self):
        text = self.readfile()
        countsuff = 0
        for i in text:
            if (i.endswith("ing")):
                countsuff = countsuff + 1
        self.printMeth(countsuff)
        self.writefile(countsuff)
        logging.info(countsuff)

    def maximum(self):
        text = self.readfile()
        countm = 0
        word = ""
        maxCount = 0
        for i in range(0, len(text)):
            countm = 1
            for j in range(i + 1, len(text)):
                if (text[i] == text[j]):
                    countm = countm + 1

            if (countm > maxCount):
                maxCount = countm
                word = text[i]
        self.printMeth(word)
        self.writefile(word)
        logging.info(word)

    def palindrome(self):
        text = self.readfile()
        pal = []
        for s in text:
            s1 = s[::-1]
            if s1 == s and s != "":
                pal.append(s)
        self.printMeth(pal)
        self.writefile(pal)
        logging.info(pal)

    def uniquewords(self):
        text = self.readfile()
        unique = []
        for word in text:
            if word not in unique:
                unique.append(word)
        self.printMeth(unique)
        self.writefile(unique)
        logging.info(unique)

    def counterindex(self):
        text = self.readfile()
        dict = {}
        dict = list(enumerate(text))
        self.printMeth(dict)
        self.writefile(dict)
        logging.info(dict)

    def splitwords(self):
        text = self.readfile()
        split = []
        for i in text:
            res = re.split('a|e|i|o|u', i)
            split.append(res)
        self.printMeth(split)
        self.writefile(split)
        logging.info(split)

    def CapitalizeCharacter(self):
        text=self.readfile()
        cap = []
        for i in text:
            a = list(i)
            a[2::3] = [x.upper() for x in a[2::3]]
            i = ''.join(a)
            cap.append(i)
        self.printMeth(cap)
        self.writefile(cap)
        logging.info(cap)

    def Capitalize5thWord(self):
        text=self.readfile()
        for i in range(4, len(text), 5):
            text[i] = text[i].upper()
        self.printMeth(text)
        self.writefile(text)
        logging.info(text)

    def ReplaceSpace(self):
        text = self.readfile()
        listToStr = ' '.join([str(i) for i in text])
        listToStr = listToStr.replace(" ", "_")
        self.printMeth(listToStr)
        self.writefile(listToStr)
        logging.info(listToStr)

    def printMeth(self, x):
        print(x)


#obj = B("inputfile3.txt")
x = cfg.names["inputfilename"]
obj = B(x)
y = cfg.names["outputfilename"]

obj.prefix()
obj.suffix()
obj.maximum()
obj.palindrome()
obj.uniquewords()
obj.counterindex()
obj.splitwords()
obj.CapitalizeCharacter()
obj.Capitalize5thWord()
obj.ReplaceSpace()
