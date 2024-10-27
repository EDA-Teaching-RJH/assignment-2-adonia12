### Part Four -- your code goes here. 
import random
random_numbers = [random.randint(1, 100) for _ in range(10)]       #generates a lsit form 1-100
print(random_numbers)
index = 0        #initialize index for while loop and use while loop to remoes even even numbers from lsit 
while index < len(random_numbers):
    if random_numbers[index] % 2 == 0:
        random_numbers.pop(index)     #removes even number 
    else:
        index += 1     #moves to next number if odd 
print("odd number list:",random_numbers)