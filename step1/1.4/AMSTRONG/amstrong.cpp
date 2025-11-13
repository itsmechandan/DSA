#include<iostream>
using namespace std;
void amstrong(int n){
    int y;
    y=n;
    int x;
    int sum = 0;
    while(n!=0){
        x= n%10;
        sum = sum + (x*x*x);
        n = n/10;
    }
    if( sum == y ){
        cout<<"amstrong";
    }
    else{
        cout<<"not";
    }

}
int main(){
    int n;
    cout<<" Enter a Number: ";
    cin>>n;
    amstrong(n);
    return 0;
}
