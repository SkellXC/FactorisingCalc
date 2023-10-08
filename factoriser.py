while True:
    num = int(input("Enter number to factorise: "))
    print(f"The factors of {num} are:")
    for x in range(1,num):
        for i in range(1,num):
            if x*i == num:
                print(x,"|",i)



