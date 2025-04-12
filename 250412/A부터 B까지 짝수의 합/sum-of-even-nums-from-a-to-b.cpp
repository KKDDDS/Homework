#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B;
    cin >> A >> B;
    int tot=0;
    for(A; A<=B; A++){
        if(A%2==0){
            tot += A;
        }
    }
    cout << tot;
    return 0;
}