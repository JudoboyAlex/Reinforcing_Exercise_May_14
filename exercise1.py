#Define a function that accepts a list of numbers as an argument and returns the sum of the odd numbers in the list.

def odd_num(numbers):
    odds =[]
    for num in numbers:
        if num % 2 != 0: 
            odds.append(num)
    return sum(odds)

print(odd_num([2,3,4,5,6,7]))



