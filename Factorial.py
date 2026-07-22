Factorials=1
def factorial(num:int):
    global Factorials
    if num<=1:
        print(f"The factorial is {Factorials}")
        return
    Factorials=Factorials*num
    factorial(num-1)
    
factorial(3)