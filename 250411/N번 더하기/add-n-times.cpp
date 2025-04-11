#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, N;
    cin >> A >> N;
    int i;
    for(i=0; i<N; i++){
        A = A+N;
        cout << A << "\n";
    }
    return 0;
}