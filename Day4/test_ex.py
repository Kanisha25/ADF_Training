"""Day 4"""
import re
import logging
import config4 as cfg

logging.basicConfig(
    filename="test.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

class TestBase():
    """ This is base class """
    #def __init__(self, filename):
     #   self.filename = filename
    filename = "inputfile4.txt"

    def readfile(self):
        """ This is readfile method """
        f_name = open(self.filename)    # pylint: disable=consider-using-with
        text = f_name.read()
        text = text.split()
        return text

    def writefile(self, word):       # pylint: disable=no-self-use
        """ This is writefile method """
        with open(Y, "a") as flag1:
            flag1.write(str(word) + "\n")
            flag1.close()


class TestChild(TestBase):                  #pylint: disable=too-many-public-methods
    """ This is Derived class """
    # def __init__(self, filename):
    # A.__init__(self, filename)

    def prefix(self):
        """ This is prefix method """
        text = self.readfile()
        count = 0
        for i in text:
            if i.startswith('To'):
                count = count + 1
        self.printmeth(count)
        self.writefile(count)
        logging.info(count)
        return count

    # def test_prefix(self):
    #     """ This is test method for prefix method """
    #     te_1 = self.prefix()
    #     t_1 = 2
    #     assert te_1 == t_1


    def suffix(self):
        """ This is suffix method """
        text = self.readfile()
        countsuff = 0
        for i in text:
            if i.endswith("ing"):
                countsuff = countsuff + 1
        self.printmeth(countsuff)
        self.writefile(countsuff)
        logging.info(countsuff)
        return countsuff

    # def test_suffix(self):
    #     """ This is test method for suffix method """
    #     te_1 = self.suffix()
    #     assert te_1 == 1

    def maximum(self):
        """ This is maximum method """
        text = self.readfile()
        countm = 0
        word = ""
        max_count = 0
        for i in range(0, len(text)):                       # pylint: disable=consider-using-enumerate
            countm = 1
            for j in range(i + 1, len(text)):
                if text[i] == text[j]:
                    countm = countm + 1

            if countm > max_count:
                max_count = countm
                word = text[i]
        self.printmeth(word)
        self.writefile(word)
        logging.info(word)
        return word

    # def test_maximum(self):
    #     """ This is test method for max method """
    #     te_1 = self.maximum()
    #     assert te_1 =='is'

    def palindrome(self):
        """ This is palindrome method """
        text = self.readfile()
        pal = []
        for s_rev in text:
            s1_rev = s_rev[::-1]
            if s1_rev == s_rev and s_rev != "":
                pal.append(s_rev)
        self.printmeth(pal)
        self.writefile(pal)
        logging.info(pal)
        return pal

    # def test_palindrome(self):
    #     """ This is test method for palindrome method """
    #     te_1=self.palindrome()
    #     assert te_1 == ['u', 'a', 'a', 'madam']


    def uniquewords(self):
        """ This is uniquewords method """
        text = self.readfile()
        unique = []
        for word in text:
            if word not in unique:
                unique.append(word)
        self.printmeth(unique)
        self.writefile(unique)
        logging.info(unique)
        return unique

    # def test_uniquewords(self):
    #     """ This is test method for unique method """
    #     te_1 = self.uniquewords()
    #     assert te_1 == ['hi', 'my', 'name', 'is', 'kanisha.', 'hope', 'u', 'are',
    #                  'fine', 'Today.', 'this', 'a', 'python', 'practice', 'file.',
    #                  'where', 'the', 'problem', 'statement', 'to', 'find', 'unique', 'texts',
    #                  'in', 'To','today', 'tomorrow', 'walking', 'madam', 'day', 'three.']

    def counterindex(self):
        """ This is counterindex method """
        text = self.readfile()
        dict_name = {}
        dict_name = list(enumerate(text))
        self.printmeth(dict_name)
        self.writefile(dict_name)
        logging.info(dict_name)
        return dict_name

    # def test_counterindex(self):
    #     """ This is test method for counter index method """
    #     te_1 = self.counterindex()
    #     assert te_1 == [(0, 'hi'), (1, 'my'), (2, 'name'), (3, 'is'), (4, 'kanisha.'), (5, 'hope'),
    #                  (6, 'u'), (7, 'are'), (8, 'fine'), (9, 'Today.'), (10, 'this'), (11, 'is'),
    #                  (12, 'a'), (13, 'python'), (14, 'practice'), (15, 'file.'), (16, 'where'),
    #                  (17, 'the'), (18, 'problem'), (19, 'statement'), (20, 'is'), (21, 'to'),
    #                  (22, 'find'), (23, 'unique'), (24, 'texts'), (25, 'in'), (26, 'a'),
    #                  (27, 'file.'),
    #                  (28, 'To'), (29, 'today'), (30, 'tomorrow'), (31, 'walking'), (32, 'madam'),
    #                  (33, 'today'), (34, 'is'), (35, 'day'), (36, 'three.')]

    def splitwords(self):
        """ This is splitwords method """
        text = self.readfile()
        split = []
        for i in text:
            res = re.split('a|e|i|o|u', i)
            split.append(res)
        self.printmeth(split)
        self.writefile(split)
        logging.info(split)
        return split

    # def test_splitwords(self):
    #     """ This is test method for split words method """
    #     te_1 = self.splitwords()
    #     assert te_1 == [['h', ''], ['my'], ['n', 'm', ''], ['', 's'], ['k', 'n', 'sh', '.'],
    #                  ['h', 'p', ''], ['', ''], ['', 'r', ''], ['f', 'n', ''], ['T', 'd', 'y.'],
    #                  ['th', 's'], ['', 's'], ['', ''], ['pyth', 'n'], ['pr', 'ct', 'c', ''],
    #                  ['f', 'l', '.'], ['wh', 'r', ''], ['th', ''], ['pr', 'bl', 'm'],
    #                  ['st', 't', 'm', 'nt'], ['', 's'], ['t', ''], ['f', 'nd'],
    #                  ['', 'n', 'q', '', ''],
    #                  ['t', 'xts'], ['', 'n'], ['', ''], ['f', 'l', '.'], ['T', ''], ['t', 'd', 'y'],
    #                  ['t', 'm', 'rr', 'w'], ['w', 'lk', 'ng'], ['m', 'd', 'm'], ['t', 'd', 'y'],
    #                  ['', 's'], ['d', 'y'], ['thr', '', '.']]


    def capitalizecharacter(self):
        """ This is capilalize method """
        text = self.readfile()
        cap = []
        for i in text:
            a_name = list(i)
            a_name[2::3] = [x.upper() for x in a_name[2::3]]
            i = ''.join(a_name)
            cap.append(i)
        self.printmeth(cap)
        self.writefile(cap)
        logging.info(cap)
        return cap

    # def test_capitalizecharacter(self):
    #     """ This is test method for Caitalize method """
    #     te_1 = self.capitalizecharacter()
    #     assert te_1 == ['hi', 'my', 'naMe', 'is', 'kaNisHa.', 'hoPe', 'u', 'arE', 'fiNe', 'ToDay.',
    #                'thIs', 'is', 'a', 'pyThoN', 'prActIce', 'fiLe.', 'whEre', 'thE', 'prOblEm',
    #                'stAteMenT', 'is', 'to', 'fiNd', 'unIquE', 'teXts', 'in', 'a', 'fiLe.', 'To',
    #                'toDay', 'toMorRow', 'waLkiNg', 'maDam', 'toDay', 'is', 'daY', 'thRee.']

    def capitalize5thword(self):
        """ This is capitalize 5th word method """
        text = self.readfile()
        for i in range(4, len(text), 5):
            text[i] = text[i].upper()
        self.printmeth(text)
        self.writefile(text)
        logging.info(text)
        return text

    # def test_capitalize5thword(self):
    #     """ This is test method for capitalize 5th word method """
    #     te_1 = self.capitalize5thword()
    #     assert te_1 == ['hi', 'my', 'name', 'is', 'KANISHA.', 'hope', 'u', 'are', 'fine', 'TODAY.',
    #                 'this', 'is', 'a', 'python', 'PRACTICE', 'file.', 'where', 'the', 'problem',
    #                 'STATEMENT', 'is', 'to', 'find', 'unique', 'TEXTS', 'in', 'a', 'file.', 'To',
    #                 'TODAY', 'tomorrow', 'walking', 'madam', 'today', 'IS', 'day', 'three.']

    def replacespace(self):
        """ This is Replace Space method """
        text = self.readfile()
        list_to_str = ' '.join([str(i) for i in text])
        list_to_str = list_to_str.replace(" ", "_")
        self.printmeth(list_to_str)
        self.writefile(list_to_str)
        logging.info(list_to_str)
        return list_to_str

    # def test_replacespace(self):
    #     """ This is test method for Replace Space method """
    #     te_1 = self.replacespace()
    #     t_1 ="hi_my_name_is_kanisha._hope_u_are_fine_Today._this_is_a_python_practice_file." \
    #         "_where_the_problem_statement_is_to_find_unique_texts_in_a_file._" \
    #         "To_today_tomorrow_walking_madam_today_is_day_three."
    #     assert te_1 == t_1

    def printmeth(self, x_name):                # pylint: disable=no-self-use
        """ This is print method """
        print(x_name)


# obj = B("inputfile3.txt")
X = cfg.names["inputfilename"]
obj = TestChild()
Y = cfg.names["outputfilename"]

obj.prefix()
obj.suffix()
obj.maximum()
obj.palindrome()
obj.uniquewords()
obj.counterindex()
obj.splitwords()
obj.capitalizecharacter()
obj.capitalize5thword()
obj.replacespace()
