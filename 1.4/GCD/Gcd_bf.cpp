#include<iostream>
using namespace std;
void gcd(int n1, int n2){
    for(int i = min(n1,n2);i>=1;i--){
        if(n1%i == 0 & n2%i == 0){
            cout<< i;
            break;         
        }
        
    }



}
int main(){
    int n1, n2;
    cout<<" Enter 2 Number: ";
    cin>>n1>>n2;
    gcd(n1,n2);
    return 0;
}