#include <iostream>
using namespace std;
void pattern(int n){
    int star = 0;
    for(int i=1; i<=n;i++){
        for(int j =1; j<=i;j++){         
            star = star +1;
            cout<< star;
        }
        cout<< endl;
    }
   

}
int main(){
    int n;
    cin >> n;
    pattern(n);
    
}