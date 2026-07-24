#Recursive - a function call it self directly or indirectly until base case reached
#fibonacci sequence--- F(n)=Fn-1 + Fn-2


# def ask(person):
#     behind=ask(person)
#     people=behind+1

#     return people

# a=ask(10)
# print(a.ask())


# def fib(n:int):
#     if n==1:
#         return 1
#     if n==0:
#         return 0
#     one= fib(n-1)
#     two=fib(n-2)
#     return one + two





#two pointer

# def pair_sum(arr, target):
#     left, right = 0, len(arr) - 1 

#     while left < right:
#         s = arr[left] + arr[right]
#         if s == target:
#             return (left, right)
#         elif s < target:
#             left += 1
#         else:
#             right -= 1  

#     return None

# arr = [1, 2, 3, 4, 5, 6]
# print(pair_sum(arr, 10))  



