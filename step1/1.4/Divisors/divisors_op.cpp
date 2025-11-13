#include<iostream>
using namespace std;
void divisor(int n){
    vector<int>v;
    for(int i =1;i<=sqrt(n);i++){
        if(n%i==0){
            v.push_back(i);
            if((n/i)!=i){
                v.push_back((n/i));
            }
        }
    }
    sort(v.begin(),v.end());
    for(auto i:v){
        cout << i <<" ";
    }
    
}
 
int main(){
    int n;
    cout<<" Enter a Number: ";
    cin>>n;
    divisor(n);
    return 0;
}