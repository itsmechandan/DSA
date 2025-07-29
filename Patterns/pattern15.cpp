#include <iostream>
using namespace std;
void pattern(int n){
    for(int i=1; i<=n;i++){
        for(char ch = 'A'; ch <= 'A' +(n-i); ch++){         
            cout << ch << " ";
        }
        cout<< endl;
    }
   
}
int main(){
    int n;
    cin >> n;
    pattern(n);
    
}