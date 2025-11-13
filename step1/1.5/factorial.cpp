#include<iostream>
using namespace std;
int functions(int n){
    if(n ==0){
        return 1;
    }
    else{
        return n*functions(n-1);
    }

}
int main(){
    int n;
    cin >>n;
    cout << functions(n);




}