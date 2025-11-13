#include <iostream>
#include <climits> 
using namespace std;

void checkpalindrome(int x) {
    int y = x;
    long long rev = 0;

    while (x != 0) {
        int digit = x % 10;
        rev = rev * 10 + digit;
        x /= 10;
    }

    if(rev == y){
        cout<< true;
    }
    else{ 
        cout<< false;
    }


}

int main() {
    int number;
    cout << "Enter an integer: ";
    cin >> number;
    checkpalindrome(number);
    return 0;
}