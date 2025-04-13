#include <iostream>

using namespace std;

int N;

int main() {
    cin >> N;

    // Please write your code here.
    int tot = 0;
    for(int i=1;i<=N;i++){
        tot += i;
    }
    cout << tot/10;
    return 0;
}