#Question:
"""Write a function that determines if the given input string is a palindrome or is not
A palindrome is a sequence of characters which reads the same backward as forward"""

#solition:
def palindrome():
    string=input("enter string")
    string1=string[::-1]
    x=0
    while x <len(string)//2:
        if string[x]==string1[x]:
            x+=1
            return "it is palindrome"
        else:
            return "it's not palindrome"
            break
print(palindrome())
