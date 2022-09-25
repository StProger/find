lenght = [12,13,4,16,10,1,9,35,23,6,7,4,7,6,3,8,4,9]
maxs = 0
for i in range(len(lenght)):
    for j in range(i+1,len(lenght)):
        for k in range(j+1,len(lenght)):
            a = lenght[i]
            b = lenght[j]
            c = lenght[k]
            if a+b>c and a+c>b and b+c>a:
                p = (a+b+c)/2
                s = (p*(p-a)*(p-b)*(p-c))**0.5
                if s>maxs:
                    maxs = s
print(maxs)
