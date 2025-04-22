input1=int(input("Enter the value 1: "))
input2=int(input("Enter the value 2: "))

op=input("choose the operator(+,_,/,*,%):")
match op:
    case '+':
        print(input1+input2)
    case '-':
        print(input1-input2)
    case '*':
        print(input1*input2)
    case '/':
        if input2 ==0:
            print("invaild")
        else:
            print(input1/input2)
    
                  