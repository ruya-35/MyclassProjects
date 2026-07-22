Factorials=1
def factorial(num:int):
    global Factorials
    if num==0:
        print(f"The factorial is 1")
        return
    if num<=1:
        print(f"The factorial is {Factorials}")
        return
        
    Factorials=Factorials*num
    factorial(num-1)
    
factorial(5)
