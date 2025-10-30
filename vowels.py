n = int(input())
for i in range (n) :
    str = input()
    v = 0
    c = 0 
    for ch in str :
        if ch.lower() in 'aeiou':
            v+=1
        else :
            c+=1
    print({v} , {c})