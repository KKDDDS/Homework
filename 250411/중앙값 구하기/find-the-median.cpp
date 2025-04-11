#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B, C;
    cin >> A >> B >> C;
    if((A<B && B <C) ||(C<B && B<A)){
        cout << B;
    }
    else if((B<A && A<C)|| (C<A && A<B)){
        cout << A;
    }
    else{
        cout << C;
    }
    return 0;
}