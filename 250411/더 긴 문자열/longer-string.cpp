#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    string A, B;
    cin >> A >> B;
    int a = A.length();
    int b = B.length();
    if(a>b){
        cout << A << " "<< a;
    }
    else if(b>a){
        cout << B <<" " <<  b;
    }
    else{
        cout << "same";
    }
    return 0;
}