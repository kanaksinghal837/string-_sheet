a = "aeiOUz"
A= a+a
for i in range(len(a+a)) :
    if A [i] >='A' and A[i]<='Z':
        continue
    if A[i] in 'aeiou' :
            A = A+"#"
print(A)
# [19 27 43 40 18 ] sub array 
# [19 27 40    18] not a sub array 
# [] not a sub array 
#sub array = n*n+1/2
#print all the value of  array of sub array 