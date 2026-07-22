// Online C++ compiler to run C++ program online
#include <iostream>
#include <algorithm>
#include <numeric>
using namespace std;

int main() {
    // Write C++ code here
    int n,arr[20],i,j,loki=0,totpow=0;
    cout << "Enter the Size of the Array";
    cin >> n;
    cout << "Enter the elements";
    for(int i = 0;i<n;i++){
        cin >> arr[i];
    }
    sort(arr, arr+n,greater<int>());
    totpow = accumulate(arr, arr+n,0);
    totpow = totpow-arr[0];
    loki = loki + arr[0];
    for(i = 1;i<n;i++){
        
        if (loki > totpow){
            cout << loki;
            break;
        }else{
            totpow = totpow-arr[i];
            loki = loki + arr[i];
        }
    }
    
    
    
}