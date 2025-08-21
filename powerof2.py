# #include <iostream>
# #include <cmath>
# using namespace std;

# int main() {
#     int n;
#     cin >> n;

#     bool isPowerOfTwo = false;

#     int i = 0;
#     while (i <= 30) {  // check 2^0 to 2^30
#         int ans = pow(2, i);
#         if (n == ans) {
#             isPowerOfTwo = true;
#             break;  // no need to check further
#         }
#         i++;
#     }

#     cout << boolalpha << isPowerOfTwo; // prints true or false
#     return 0;
# }

#in py
n = int(input())

i = 0
while i <= 30:
    ans = 2 ** i   # same as pow(2, i)
    if n == ans:
        print(True)
        break
    i += 1
else:   # this runs only if loop finishes without break
    print(False)
