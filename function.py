print("hello function")

def SolveIt2():
    print("this i dfirst line getting executed")
    print("this is line 123")

print("iam not getting printed")

def SolveIt4():
    print("iam solve it4")
    print("this s getting exectued")
    SolveIt2()
    print("second line is getting executed")

def SolveIt():
    print("this is line 111")
    print("this is line 112")
    SolveIt4()
    print("solve it4 havent completed its execution")

def SumOfTwoNumbers(num1,num2):
    print("after exectuion")
    SolveIt()
    print("ntg gets printed")
    result = num1 + num2
    print("before execution")
    return result


print("last line is getting printed")
num1 = int(input())
num2 = int(input())
result = SumOfTwoNumbers(num1,num2)
print(result)
