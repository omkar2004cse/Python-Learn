with open('D:/git and github/Python-Learn/code_with_Sagar/files/demo.py','w+') as f:
    con=input("Write the text")
    f.write(con)
    r=f.read()
    print(r)