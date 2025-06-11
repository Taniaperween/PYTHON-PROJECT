try:
    a =int(input("enter the first number:"))
    b =int(input("enter the first number:"))
    print("what kind of operation do you want to perform.press + for addition\n,press - for subtraction\n,press / for division\n,press * for multiplication\n")
    o=input("enter operation:")
    if o=="+":
            print(f"the result is :{a+b}")
    elif o=="-":
            print(f"the result is :{a-b}")
    elif o=="*":
            print(f"the result is :{a*b}")
    elif o=="/":        
            print(f"the result is :{a/b}")
    else:
            print(f"this was an error")
except Exception as e:
    print("enter a valid of a and b")                
                 
    