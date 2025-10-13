#include <iostream>
#include <set>
using namespace std;

int main() {
    int n = 7;
    int arr[7] = {1, 1, 2, 2, 2, 3, 3};
    int i = 0;
    for( int j =1; j<n;j++){
        if( arr[j]!= arr[i]){
            arr[i+1]=arr[j];
            i++;
        }
    }
    cout << i+1;

    return 0;
}