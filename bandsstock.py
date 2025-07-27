prices = [7,2,1,5,6,4,8]
max_pro = 0
n = len(prices)
for i in range(n):
    for j in range(i+1,n):
        if prices[j]>prices[i]:
            p = prices[j]-prices[i]
            max_pro = max(max_pro,p)
print(max_pro)
