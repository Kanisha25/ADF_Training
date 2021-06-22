try:
    dec = int(input("Enter a decimal number: "))

    print("Decimal number", dec, "to Binary is", bin(dec))
    print("Decimal number", dec, "to Octal is", oct(dec))
    print("Decimal number", dec, "to Hexadecimal is", hex(dec))

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
