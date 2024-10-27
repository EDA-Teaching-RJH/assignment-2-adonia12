### Part Three -- your code goes here. 
num_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
num_list.sort()      #sorts in ascending order  
num_list = [num for num in num_list if num != 1]   #removing occurrences of number 1
num_list.extend([7,8])        #adds number 7 and 8 to the end of the list 
print(num_list)






