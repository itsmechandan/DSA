#include <iostream>
using namespace std;
void pattern(int n){
    int i,j;
    int space = 2*n -2;
    for(i = 1;i<=2*n-1;i++){
    int stars = i;
        if(i>n){
            stars = 2*n-i;
        }
        for(j=1;j<=stars;j++){
        cout <<"*";
    }
    for (j=1;j<= space;j++){
        cout <<" ";
    }

        for(j=1;j<=stars;j++){
        cout <<"*";
    }
    if(i<n){
        space = space -2;    
    }
    else{
        space = space +2;
    }
    cout<< endl;

   }
   
}
int main(){
    int n;
    cin >> n;
    pattern(n);
    
}