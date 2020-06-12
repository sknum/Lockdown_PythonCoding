lower = int(input("enter the lower interval:"))
upper = int(input("enter the upper interval:")) 
for val in range(lower, upper + 1): 
 if val > 1:
  for n in range(2, val): 
   if (val % n) == 0 :  
    break
  else:   
    print(val) 
