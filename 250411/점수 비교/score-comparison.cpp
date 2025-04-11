#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A_m, A_e;
    int B_m, B_e;
    cin >> A_m >> A_e;
    cin >> B_m >> B_e;
    
    cout << (A_m > B_m && A_e > B_e);
    

    return 0;
}