#DATA TYPES
#Strings
#(Subscripting)
print("Hello World"[0]) #H
print("Hello World"[1]) #e

print("123" + "456") #123456

#Integer
print(123 + 456) #579
123_456_789 #Python allows underscores in numbers for readability

#Float
print(3.14159) #3.14159

#Boolean
print(True) #True
print(False) #False

#Type Error, Type Checking and Type Conversion
num_char = len(input("What is your name? "))
new_num_char = str(num_char) #Convert integer to string
# print(type(num_char)) #<class 'int'>
print("Your name has " + new_num_char + " characters.")

#Math Operations
print(3 + 5) #8
print(7 - 4) #3
print(3 * 2) #6
print(6 / 3) #2.0, division always returns a float 
print(2 ** 3) #8 (Exponentiation)
print(3 * (3 + 3)) #18 (Order of operations)
#PEMDAS: 
# Parentheses (), 
# Exponents **, 
# Multiplication/Division /*, 
# Addition/Subtraction +-
print(3 * 3 + 3 / 3 - 3) #7.0 (Order of operations) start with multiplication and division, then addition and subtraction. Because of the order of operations, this will be 9 + 1 - 3 = 7.0
#How can we change the problent to return 3? 
print(3 * (3 + 3) / 3 - 3) #3.0 (Order of operations) start with parentheses, then multiplication and division, then addition and subtraction. Because of the order of operations, this will be 18 / 3 - 3 = 6 - 3 = 3.0 

#Rounding Numbers
print(round(8 / 3)) #3 (rounds to nearest integer)
print(round(8 / 3, 2)) #2.67 (rounds to 2 decimal places)
print(8 // 3) #2 (Floor division, rounds down to nearest integer)
result = 4 / 2
print(result) #2.0 (result is a float)
result /= 2 #result = result / 2
print(result) #1.0 (result is still a float)
score = 0
score += 1 #score = score + 1
print(score) #1 (score is an integer)
score -= 1 #score = score - 1
print(score) #0 (score is still an integer)
score *= 2 #score = score * 2
print(score) #0 (score is still an integer)

#F-Strings
score = 0
height = 1.8 #1.8 meters
isWinning = True
print(f"Your score is {score}, your height is {height}, and you are winning is {isWinning}.") #Your score is 0, your height is 1.8, and you are winning is True.