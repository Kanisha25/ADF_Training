try:
    name=input("Enter the name ")
    age=int(input("Enter age "))
    gender=input("Enter gender ")
    salary=float(input("Enter the salary "))
    state=input("Enter state ")
    city=input("Enter city ")
    print("Name is ", name)
    print("Age is ", age)
    print("Gender is ", gender)
    print("Salary is ", salary)
    print("State is ", state)
    print("City is ", city)

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