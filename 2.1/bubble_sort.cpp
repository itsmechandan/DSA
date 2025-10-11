//adjacent swapping
#include<iostream>
using namespace std;
void bubblesort(int arr[],int n){
    for( int i = n-1;i>=1;i--){
        int didswap =0;
        for( int j = 0; j<=i-1;j++){
            if(arr[j]>arr[j+1]){
                swap(arr[j],arr[j+1]);
                didswap = 1;
            }

        }
        if(didswap ==0){
            break;
        }
    }
    

}
int main(){
    int n;
    cout<< "Enter the NUmber of Elements :";
    cin >> n;
    int arr[n];
    cout<<" Enter the values of array";
    for( int i =0;i<n;i++){
        cin >>arr[i];
    }
    bubblesort(arr,n);
    cout<<" Sorted array";
    for( int i =0;i<n;i++){
        cout <<arr[i]<<endl;
    }
    return 0;
}