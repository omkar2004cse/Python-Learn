try:
    file=open('D:\git and github\Python-Learn\code_with_Sagar\OOP\car_.py')
    r=file.read()
    print(r)
except FileNotFoundError:
    print("file not found")

finally:
    file.close()
    print("File close")