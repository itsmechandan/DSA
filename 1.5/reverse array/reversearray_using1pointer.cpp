#include<iostream>
using namespace std;

void reverseArray(int i, int n, int arr[]) {
    if(i>=n/2) return;
    swap(arr[i],arr[n-i-1]);
    reverseArray(i+1,n,arr);
}

int main() {
    int n;
    cout << "Please enter array size: ";
    cin >> n;

    int arr[n];
    cout << "Please enter array elements: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    reverseArray(0, n, arr); // reversing array

    cout << "Reversed array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}