#in c++
# int main(){
#         int ans = 0;
#         while(x!=0){
#             int digit = x%10;
#             if(( ans > INT_MAX/10 ) || ( ans < INT_MIN/10 )){
#                 return 0;
#             }
#             ans = (ans*10)+digit;
#             x = x/10;
#         }
#         return ans;}

#in python
x = int(input("Enter number: "))
ans = 0
sign = -1 if x < 0 else 1
x = abs(x)

while x != 0:
    digit = x % 10

    # check for 32-bit signed integer overflow
    if ans > (2**31 - 1) // 10:
        print(0)
        exit()   # stop execution like 'return 0' in C++

    ans = ans * 10 + digit
    x //= 10   # integer division

print(sign * ans)

