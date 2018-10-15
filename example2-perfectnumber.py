#question:
"""Write a function perfect that determines if a number given as a parameter is a perfect number or not. Use this function in a program that determines and prints all the perfect numbersbetween 1 and 1000.
Perfect Number:An integer number is said to be a perfect number if its factors, including 1 (butnot the number itself), sum to the number. For example, 6 is a perfect number because 6 =1 + 2 + 3."""


#solition:
for i in range(1,1000):
    sum=0
    for divisor in range(1,(i//2)+1):
        if i%divisor==0:
            sum+=divisor
    if i==sum:
        print(i,"is a perfect number")
