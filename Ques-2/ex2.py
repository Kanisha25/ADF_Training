
import csv
try:
    filename = "assesment2.csv"

    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            print(line)

except ValueError:
   print("Value Error Occured")
except (TypeError, ZeroDivisionError):
   print("Type Error has Occured")
except NameError:
    print("Variable not defined")
except IOError:
    print("IO Exception occured")
except:
    print("Something else went wrong")