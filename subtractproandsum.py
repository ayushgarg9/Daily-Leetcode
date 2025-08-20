# in c++
#include <bits/stdc++.h>
# using namespace std;
# int main(){
#     int n;
#     cout << "enter n: " <<endl;
#     cin>> n;
#     int pro1 = 1,sum1 = 0;
#     int digit;
#     while(n>1){
#         digit = n%10;
#         pro1 *= digit;
#         digit = n%10;
#         sum1 += digit;
#         n = n/10;
#     }
#     cout << pro1-sum1 << endl;
# }

# in pyhton
n = int(input("enter n: "))
pro = 1
sum1 = 0
while n>0:
    digit = n%10
    pro *= digit
    sum1 += digit
    n =int(n/10)        
print(pro-sum1)