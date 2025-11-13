//insert karo 
#include<iostream>
using namespace std;
void insertion(int arr[],int n){
    for(int i =0;i<n;i++){
        int j =i;
        while(j>0 && (arr[j-1]>arr[j])){
            swap(arr[j-1],arr[j]);
            j--;
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
    insertion(arr,n);
    cout<<" Sorted array";
    for( int i =0;i<n;i++){
        cout <<arr[i]<<endl;
    }
    return 0;
}