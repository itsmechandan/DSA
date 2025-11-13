#include <iostream>
#include <set>
using namespace std;

int main() {
    int n = 7;
    int arr[7] = {1, 1, 2, 2, 2, 3, 3};

    set<int> st;
    for (int i = 0; i < n; i++) {
        st.insert(arr[i]);
    }
//in the brute force approach, we copy elements back from the set into the original array
// the other elements other than the unique values do not matter.

    int index = 0;
    for (auto it : st) {
        arr[index] = it;  // copy unique elements back into array
        index++;
    }

    cout << "Unique elements: ";
    for (int i = 0; i < index; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}

// Time → O(n log n)
// (because inserting into a set takes log n per element).
// Space → O(n)
// (extra memory for the set).