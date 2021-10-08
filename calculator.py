import math
while True:

    print("MENU:")
    print("1: sum")
    print("2: sub")
    print("3: multiply")
    print("4: division")
    print("5: sinus")
    print("6: cosine")
    print("7: tangent")
    print("8: cotangent")
    print("9: log")
    print("10: exit")

    op= int(input('operation:'))

    if 0<op<5:
        print(" For operators 1 to 4 please enter two number:")
        num1= int(input('num1='))
        num2= int(input('num2='))

        if op == 1:
            
            print('num1 + num2 =', num1+num2)
        
        elif op == 2:
            print('num1 - num2 =', num1-num2)
        
        elif op == 3:
            print('num1 * num2 =', num1*num2)
        
        elif op == 4:
            if num2!=0:
                print('num1 / num2 =', num1/num2)
            else: 
                print('cannot divide by zero')
    
    elif 4<op<10:
        print(" For operators 5 to 9 please enter one number:")
        num= int(input('num='))
        
        if op == 5:
            radian= num/180*math.pi
            print('sinus num =', float(math.sin(radian)))

        elif op == 6:
            radian= num/180*math.pi
            print('cosine num =', float(math.cos(radian)))
            
        elif op == 7:
            radian= num/180*math.pi
            print('tangent num =', float(math.tan(radian)))
        elif op == 8:
            radian= num/180*math.pi
            print('cotangent num =', float(math.atan(radian)))

        elif op == 9:
            print('log num =', float(math.log(num)))

        
    else:
        op == 10 
        print('command not found')
        break

