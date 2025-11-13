// THoda complicated tho hain
// Given that the Maximum Value of the element stored in the array is 12.
// fyi, inside Main function, the max value that can be stored is 10^6
// GLobally we can declare at 10^7 but not 10^9
#include<iostream>
using namespace std;
int main(){
    int n;
    cout << " Enter the Size of the Array"<< endl;
    cin >> n;
    int arr[n];
    cout << "Enter the elements of the Array" << endl;
    for(int i =0;i<n;i++){
        cin >> arr[i];
    }
    int hasharray[13]={0};
    for(int i =0;i<n;i++){
        hasharray[arr[i]]+=1;
    }
    // Creating hash Array which would include the count of Digits.
    int q;
    cout <<" Enter your quiery"<< endl;
    while(q--){
        cin >> q;
        cout << hasharray[q];
    }
    return 0;

}