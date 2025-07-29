#include <iostream>
using namespace std;
void pattern7(int n)
{
    for (int i =0;i<n;i=i+1){
        for (int j =0;j<n-i-1;j=j+1){
            cout <<" ";
        }
        for (int j = 0; j<2*i+1;j++){
            cout<<"*";
        }
        for (int j =0;j<n-i-1;j=j+1){
            cout <<" ";
        }
        cout<< endl;
    }
}
void pattern8(int n){
    for (int i =0;i<n;i=i+1){
        for (int j =0;j<i;j=j+1){
            cout <<" ";
        }
        for (int j = 0; j<2*n-(2*i+1);j++){
            cout<<"*";
        }
        for (int j =0;j<i;j=j+1){
            cout <<" ";
        }
        cout<< endl;
    }
}
int main(){
    int n;
    cin >> n;
    pattern7(n);
    pattern8(n);
    return 0;
    
}