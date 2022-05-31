go = True
while go == True:
    num = input("Enter number to factorise: ")
    num = int(num)
    print("The factors of", num,"are:")
    for x in range(1,num):
        for i in range(1,num):
            if x*i == num:
                print(x,"|",i)
            else:
                continue


