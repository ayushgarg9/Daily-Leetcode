accounts = [[1,2,3],[3,2,1]]

maxwealth = 0
for i in range(len(accounts)):
    totalwealth = sum(accounts[i])
    maxwealth = max(maxwealth,totalwealth)
print(maxwealth)