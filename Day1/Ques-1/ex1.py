try:
    x=input("Enter file name")
    text_file = open(x, 'r')
    text = text_file.read()

    text = text.lower()
    words = text.split()
    words = [word.strip('.,!;()[]') for word in words]
    words = [word.replace("'s", '') for word in words]

    unique = []
    for word in words:
        if word not in unique:
            unique.append(word+str(len(word)))

    unique=list(set(unique))
    unique.sort(key=len)
    print(unique)
    with open("assesment1write.txt", "w") as f1:
        for l in unique:
            f1.write(l+" ")

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
