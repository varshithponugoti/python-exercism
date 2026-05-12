def is_armstrong_number(number):
    no_of_digits=len(str(number))
    total=0
    for char in str(number):
        total+=int(char) ** no_of_digits
    return total==number
        
    
