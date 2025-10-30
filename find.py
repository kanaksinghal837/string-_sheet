a = "abobc"
count = 0 
for i in range (len(a)) :
    if( a[i]=='b' and a[i+1]=='o' and a[i+2]=='b'):
        count =count+1
print(count)