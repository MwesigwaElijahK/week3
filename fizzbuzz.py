list1 = [1,2,3,4,5,78,98,65]
list2 = [6,7,8,9,10,11,45]
def fizzbuzz(list1, list2):
    
    total_length = len(list1) + len(list2)
    
    
    
    if (total_length) % 3 == 0 and (total_length) % 5 == 0:
        return ('FizzBuzz')
    elif (total_length) % 3 == 0: 
        return ('Fizz')
    elif (total_length) % 5 == 0:
        return ('Buzz')
    else: 
        return (total_length) 


        

print(fizzbuzz(list1, list2))  