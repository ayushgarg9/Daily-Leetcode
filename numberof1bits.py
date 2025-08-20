# in c++
#include <bits/stdc++.h>
# using namespace std;
# int main(){
# #         int count = 0;
#           while(n!=0){
#               if(n&1){
#                   count++;
#                   }
#               n = n>>1;
#               }
#               return count;
#           }
# }

# in python
# take binary input as string
binary_str = input("Enter binary number: ")

# convert to integer (unsigned)
n = int(binary_str, 2)

print("As integer:", n)

count = 0
while n!=0:
    if n & 1:
        count += 1
    n >>= 1
print(count)
