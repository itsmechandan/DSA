#include <iostream>
using namespace std;
void pattern(int n){
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
    pattern(n);
    
}