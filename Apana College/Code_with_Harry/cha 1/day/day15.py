# day 15 task display greeting according to the time
import time
timestamp=int(time.strftime('%H'))
if(1<=timestamp<=12):
    print("Good Morning")
elif(13<=timestamp<=17):
    print("Good Afternoon")
elif(17<=timestamp<=19):
    print("Good Evening")
else:
    print("Good night")

