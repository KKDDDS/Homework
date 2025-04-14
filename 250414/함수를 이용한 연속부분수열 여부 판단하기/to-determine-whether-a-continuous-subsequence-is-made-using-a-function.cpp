#include <iostream>

using namespace std;

int n1, n2;
int a[100], b[100];

int main() {
    cin >> n1 >> n2;

    for (int i = 0; i < n1; i++) cin >> a[i];

    for (int i = 0; i < n2; i++) cin >> b[i];

    // Please write your code here.
    bool right = false;
    for(int i=0;i<n1-n2;i++){
        if(a[i]==b[0]){
            for(int j=0;j<n2;j++){
                if(a[i+j]==b[j]){
                    right = true;
                    continue;
                }
                else{
                    right = false;
                    break;
                }
            }
        if(right){
            cout << "Yes";
            return 0;
        }
        }
    }
    cout << "No";
    return 0;
}