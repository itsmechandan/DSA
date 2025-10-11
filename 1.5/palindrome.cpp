#include<iostream>
using namespace std;

bool checkpalindrome(int i, int n, string &str) {
    if (i >= n / 2) return true;
    if (str[i] != str[n - i - 1]) return false;
    return checkpalindrome(i + 1, n, str); // ⬅️ Added return here
}

int main() {
    string str;
    cout << "Please enter string elements: ";
    cin >> str;
    int n = str.length();

    if (checkpalindrome(0, n, str)) {
        cout << "Yes, it is a palindrome.";
    } else {
        cout << "No, it is not a palindrome.";
    }

    return 0;
}