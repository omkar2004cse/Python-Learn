# write that can be create the file if not exist or use if exist
f=open('/git and github/Python-Learn/code_with_Sagar/files/demo.py','w')
content=input("Enter a text to update in the file:-")
f.write(content)
print("Data is added sucessful")
f.close()