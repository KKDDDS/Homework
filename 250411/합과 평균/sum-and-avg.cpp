#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B;
    cin >> A >> B;
    double tot = A+B;
    cout << fixed;
    cout.precision(1);
    cout << A+B << " " << tot/2;
    return 0;
}