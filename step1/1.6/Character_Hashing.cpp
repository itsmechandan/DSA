#include<iostream>
using namespace std;
int main(){
    string s;
    cout << "Enter the string" << endl;
    cin >> s;
    
    int hasharray[256]={0};
    for(int i =0;i<s.size();i++){
        hasharray[s[i]]+=1;
    }
    // Creating hash Array which would include the count of Digits.
    int q;
    cin >>q;
    cout <<" Enter your quiery"<< endl;
    while(q--){
        char c;
        cin >> c;
        cout << hasharray[c]<<endl;
    }
    return 0;

}