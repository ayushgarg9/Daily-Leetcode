digits = [2,2,3]
for i in range (len(digits)-1,-1,-1):
    if digits[i]<9:
        digits[i]+=1
        print(digits)
        break
    digits[i]=0
print([1]+digits)
    