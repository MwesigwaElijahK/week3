list1 = [4,2,8,1,9]
missing = []

for x in range(1,11):
    if x not in list1:
        missing.append(x)

print(missing)        
