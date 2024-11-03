sp=float(input("enter selling price: "))
ogp=float(input("enter og price: "))
if sp>ogp:
    print("you got a profit")
    pro=sp-ogp
    print (f"your profit is {pro}")
else:
    print("you got a loss")
    loss=ogp-sp
    print (f"your loss is {loss}")