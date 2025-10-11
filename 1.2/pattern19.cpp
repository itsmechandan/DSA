#include <iostream>
using namespace std;
void pattern(int n){
    int x = 0;
    for(int i=0; i<n;i++)
    {
        for(int j=1;j<=n-i;j++){
            cout <<"*";
        }
        for( int j = 0;j< x;j++){
            cout<<" ";
        }
        x = x+2;
        for( int j = 1;j<=n-i;j++){
            cout<<"*";
        }
        cout << endl;
    }
    int y =8;
    for (int i =1;i<=n;i++){
        for( int j = 1;j<=i;j++){
            cout <<"*";
        }
        for(int j =0 ; j<y;j++){
            cout <<" ";
        }
        for( int j = 1;j<=i;j++){
            cout <<"*";
        }
        y= y-2;
        cout<< endl;

    }
   
}
int main(){
    int n;
    cin >> n;
    pattern(n);
    
}