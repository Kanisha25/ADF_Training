import time
try:
    num=2
    while(num>0):
          if num > 1:
              for i in range(2, num):
                  if (num % i) == 0:
                      break

              else:
                  print(num)
                  time.sleep(5)
              num=num+1

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
