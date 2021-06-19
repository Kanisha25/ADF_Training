try:
    c = input("Enter a character: ")

    print("The ASCII value of", c, "is", ord(c))

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