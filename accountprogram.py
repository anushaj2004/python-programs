currentpassword = int(input())
acutalpassword = 2387
n=3
for i in range(3):
    if acutalpassword ==  currentpassword:
        print("successfully logged in")
        break
    else:
        if n == 1:
            print("your account blocked,try after 24 hrs")
        else:
            print("incorrect password, you are left with ",n-1,"attempts")
    n -= 1
