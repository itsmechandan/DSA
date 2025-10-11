#include<iostream>
using namespace std;
void divisor(int n){
   int i;
   for(i=1;i<=n;i++){
        if(n%i==0){
            cout<< i<<endl;
        }
   }
}
int main(){
    int n;
    cout<<" Enter a Number: ";
    cin>>n;
    divisor(n);
    return 0;
}