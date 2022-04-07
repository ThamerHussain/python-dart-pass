def Thamer():
    ls = []
    while True:
        n = int(input("Enter X value:"))
        if n > 0 and n <= 10: X = n; break
        else: print("The number dosent achieve the condition: '0 < x <= 10' because it's higher than ten") if n > 10 else print("The number dosen't achieve the condition: '0 < x <= 10' because it's lower than or equal to zero") ; 
    
    for _ in range(X):
        num = int(input())    
        num_state = f'{num} is even' if num % 2 == 0 else f'{num} is odd'
        ls.append(num_state)
    
    print('\n'.join(ls))

Thamer()
