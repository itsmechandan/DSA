#include<iostream>
using namespace std;
void summ(int sum,int i){
    if(i<1){
        cout<<sum;
        return;
    }
    summ(sum+i,i-1);

}
int main(){
    int n;
    cin >>n;
    summ(0,n);
}