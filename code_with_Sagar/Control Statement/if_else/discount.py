amount=float(input("Enter amount:-"))
dis=int(input("Enter a Discount in multiple of 10(eg:- 10,20,30,40,50):-"))
if(dis==10):
    d=(amount*10)/100
    print("After",dis,"% Discount Amount to Pay is:-",amount-d)
elif(dis==20):
    d=(amount*20)/100
    print("After",dis,"% Discount Amount to Pay  is:-",amount-d)
elif(dis==30):
    d=(amount*30)/100
    print("After",dis,"% Discount Amount to Pay  is:-",amount-d)
elif(dis==40):
    d=(amount*40)/100
    print("After",dis,"% Discount Amount to Pay  is:-",amount-d)
elif(dis==50):
    d=(amount*50)/100
    print("After",dis,"% Discount Amount to Pay  is:-",amount-d)
