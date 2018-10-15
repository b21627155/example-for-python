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