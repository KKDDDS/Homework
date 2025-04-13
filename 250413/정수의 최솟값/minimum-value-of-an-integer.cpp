#include <iostream>

using namespace std;

int a, b, c;

int main() {
    cin >> a >> b >> c;

    // Please write your code here.
    if(a<=b && a<=c){
        cout << a;
    }
    else if(b<=a && b<=c){
        cout << b;
    }
    else{
        cout << c;
    }
    return 0;
}