// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;

int main() {
    // Write C++ code here
    int n,arr[20],i,j=0,count=1;
    cout << "Enter the Size of the Array";
    cin >> n;
    cout << "Enter the elements";
    for(int i = 0;i<n;i++){
        cin >> arr[i];
    }
    j = arr[0];
    for(int i = 0;i< n;i++){
        if(arr[i]>j){
            j = arr[i];
            count++;
        }
    }
    
    cout << count;
    
}