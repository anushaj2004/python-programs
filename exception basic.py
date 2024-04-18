print("starting line")

try:
    a = 10/0
except:
    print("some exception raised")
else:
    print("no exception raised")
finally:
    print("this is a final block")
print("outside try block")

