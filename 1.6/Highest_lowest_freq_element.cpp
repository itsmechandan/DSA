#include <iostream>
#include <unordered_map>
using namespace std;
int main(){
    int n;
    cout << " Enter The Number of Elements: " << endl;
    cin >> n;
    int arr[n];
    cout<< " Enter the Digits of Array" <<endl;
    for(int i = 0;i<n;i++){
        cin >> arr[i];
    }
    unordered_map<int,int> mpp;
    for(int i =0;i<n;i++){
        mpp[arr[i]]++;
    }
    int maxFreq = 0;
    int minFreq = n;
    int maxelement = 0;
    int minelement = 0;

    for(auto it:mpp){
        int element = it.first;
        int count = it.second;
        
        if(count > maxFreq){
            maxFreq = count;
            maxelement = element;
        }
        if(count < minFreq){
            minFreq = count;
            minelement = element;
        }


    }
    cout << "Maximum Frequency element :"<< maxelement;
    cout << "Minmum Frequency element :"<< minelement;

    return 0;

}