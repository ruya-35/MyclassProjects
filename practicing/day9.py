# def max_sum_windoow(arr, k):
#     n=len(arr)
#     best=float('-inf')
#     for i in range(n-k+1):
#         window_sum=0
#         for j in range(i,i+k):
#             window_sum+=i
        

#Binary Tree
class Node:
    def __init__(self, value):  
        self.value = value      
        self.left = None
        self.right = None

root = Node("Grand father")
root.left = Node("father")
root.right = Node("child")

#binart search tree
#   Left<right


#pre order-- Root L R
#Inorder -- L Root R
#PostOrder-- L R Root




#focus for exam
# depth first search  Root L R   use stack
# level search 
