total_bill = 5000
people= ["Alem","Selam","Robel","Liya","Amde"]
people_num = len(people)

def split_bill(total_bill, people_num, rate=0.10):
    tip= total_bill*rate
    total_with_tip = total_bill+tip
    total_per_person= total_with_tip/people_num
    return total_per_person

x=split_bill(total_bill, people_num)
for i in people:
    print(f"{i}: {x}ETB")