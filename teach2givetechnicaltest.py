# Question 1 
# Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for
# multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print
# "FizzBuzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Question 2: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100.
# Function to generate Fibonacci sequence up to a certain limit
        
def fibonacci_sequence(limit):
    fibonacci_sequence = [0, 1]  # Initializing with the first two numbers of the given Fibonacci sequence

    while True:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_number > limit:
            break
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

# Generate Fibonacci sequence up to 100
fibonacci_sequence_up_to_100 = fibonacci_sequence(100)
print("Fibonacci sequence up to 100:", fibonacci_sequence_up_to_100)


# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.
# Examples:
# 8=> returns true
# 6=> returns false

def is_power_of_two(n):
    return n > 0 and bin(n).count('1') == 1
num = int(input("Enter an integer: "))
if is_power_of_two(num):
    print("True")
else:
    print("False")

# Question 4: Capitalize Words
# Write a program that accepts a string as input, capitalizes the first letter of each word in the
# string, and then returns the result string.
# Examples:
# "hi"=> returns "Hi"
# "i love programming"=> returns "I Love Programming"

def capitalize_words(input_str):
    return input_str.title()

# Example usage:
input_str = "i love programming"
result = capitalize_words(input_str)
print(result)  


# Question 5: Reverse Integer
# Write a program that takes an integer as input and returns an integer with reversed digit
# ordering.
# Examples:
# For input 500, the program should return 5.
# For input -56, the program should return -65.
# For input -90, the program should return -9.
# For input 91, the program should return 19.

def reverse_integer(num):
    # Convert integer to string
    num_str = str(num)
    
    # To handle negative sign if present
    if num_str[0] == '-':
        reversed_str = '-' + num_str[:0:-1]
    else:
        reversed_str = num_str[::-1]
    
    # Convert the reversed string back to an integer
    reversed_num = int(reversed_str)
    
    return reversed_num


# Question 6: Count Vowels
# Write a program that counts the number of vowels in a sentence.
# eg " Hello World " => returns 2
def count_vowels(sentence):
    # Defining the set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Convert the sentence to lowercase to handle both lowercase and uppercase vowels
    sentence = sentence.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Iterate through each character in the sentence
    for char in sentence:
        # Check if the character is a vowel
        if char in vowels:
            count += 1
    
    return count

# Example of "Hello world":
sentence = "Hello World"
print(count_vowels(sentence))  