best_time= eval(input("Enter the best case scenario time- ")) 
avg_time= eval(input("Enter the avg case scenario time- ")) 
worst_time= eval(input("Enter the worst8 case scenario time- ")) 
b= (best_time+4*avg_time+worst_time)/6
print("Estimated time using bell curve- ", b)