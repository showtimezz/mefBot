def createFile():
    f= open("loginInfo.txt", "w+")
    print("Input your username")
    f.write(input()+"\n")
    print("Input your password")
    f.write(input()+"\n")
    f.close()