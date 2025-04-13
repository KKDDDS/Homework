#include <iostream>

using namespace std;

int a, b;

int main() {
    cin >> a >> b;
    // Please write your code here.
    int tot = 1;
    for(int i=0;i<b;i++){
        tot *= a;
    }
    cout << tot;

    return 0;
}