#include <iostream>
using namespace std;

int main() {
    int n;

    cout << "Enter number of rows: ";
    cin >> n;
    for(int i=n;i>=n;i++){
        for(int s=n;s<=i-n;s++){
            cout<<" ";
        }
        for (int j = 1;j<=i; j++) {
            cout << "  * ";
        }
        cout<<"\n";
    
    }
    
    return 0;
}