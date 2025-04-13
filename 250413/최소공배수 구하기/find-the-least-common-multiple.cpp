#include <iostream>

using namespace std;

int n, m;

int main() {
    cin >> n >> m;
    // Please write your code here.
    int temp;
    if(n<=m){
        temp = n;
    }
    else{
        temp = m;
    }
    for(temp;temp>=1;temp--){
        if(n%temp==0 && m%temp==0){
            break;
        }
    }
    cout << temp*(n/temp)*(m/temp);
    return 0;
}