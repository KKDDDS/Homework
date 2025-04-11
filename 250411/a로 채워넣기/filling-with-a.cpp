#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    string A;
    cin >> A;
    A[1] = 'a';
    A[A.size()-2] = 'a';
    cout << A;
    
    return 0;
}