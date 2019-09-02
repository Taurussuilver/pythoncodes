lst = []                                                      #intializing an empty list
num = int(input('How many numbers: '))                       #taking input of total no of numbers to be entered by user
total = 0                                                    #intializing total to zero
for n in range(num):                                         #using a for loop, so that it will read each and every number
    numbers = float(input('Enter number : '))                #taking one input at a time
    total = total + numbers                                  #adding the numbers given as input
    avg = total / num                                         #taking average of all numbers in the list
    lst.append(numbers)                                       #The append() method appends an element to the end of the list.
                                                              #print the values...
print('Average of all', num, ' numbers is :', avg)  
print('total sum of all numbers is:', total)
print("Maximum element in the list is :", max(lst))
print("Minimum element in the list is :", min(lst))
