for i in range(1,1000):
    sum=0
    for divisor in range(1,(i//2)+1):
        if i%divisor==0:
            sum+=divisor
    if i==sum:
        print(i,"is a perfect number")