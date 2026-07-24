#First Question
# def fizzbuzz(n:int):
#     for i in range(1,n+1):
#         if i%3==0 and i%5==0:
#             print(f"FizzBuzz")
#         elif i%3==0:
#             print(f"Fizz")
#         elif i%5==0:
#             print(f"Buzz")
#         else:
#             print(f"{i}")
        
# fizzbuzz(15)



#Second Question
def count_vowel(s:str):
    vowels=s.lower()
    holder=[]
    count=0

    for char in vowels:
        holder.append(char)
    for char in holder:
        if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
            count+=1
        else:
            continue
    print(f"The number of vowel in {s} are {count}")

count_vowel("Hello World")
count_vowel("PYTHON")
count_vowel("gym")