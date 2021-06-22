try:
    def hcf(x, y):
        if x > y:
            smaller = y
        else:
            smaller = x
        for i in range(1, smaller + 1):
            if ((x % i == 0) and (y % i == 0)):
                hcf = i
        return hcf


    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The H.C.F. is", hcf(num1, num2))


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
