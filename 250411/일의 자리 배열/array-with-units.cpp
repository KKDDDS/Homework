#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n, m;
    cin >> n >> m;
    int i = 8;
    cout << n << " " << m << " ";
    while(i>0){
        int temp = n+m;
        n = m;
        m = temp%10;
        cout << m << " ";
        i--;
    }
    return 0;
}