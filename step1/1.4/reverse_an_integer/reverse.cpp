#include <iostream>
#include <climits> 
using namespace std;

int reverseInteger(int x) {
    long long rev = 0;

    while (x != 0) {
        int digit = x % 10;
        rev = rev * 10 + digit;
        x /= 10;
    }

    // Check 32-bit overflow
    if (rev < INT_MIN || rev > INT_MAX)
        return 0;

    return (int)rev;
}

int main() {
    int number;
    cout << "Enter an integer: ";
    cin >> number;

    int result = reverseInteger(number);
    cout << "Reversed integer: " << result << endl;

    return 0;
}