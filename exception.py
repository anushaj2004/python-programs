print("starting line")
a = [11,12,33]
try:
    a = 10 /0
    print(a[5])
    print(y)
except ZeroDivisionError:
    print("exception raised due to Zero Division Error")
except IndexError:
    print("exception raised due to Index Error")
except NameError:
    print("exception raised due to undefined variable")
except:
    print("some exception raised")
else:
    print("no exception raised,everything worked perfectly")
finally:
    print("this is final block")
print("outside try block")



