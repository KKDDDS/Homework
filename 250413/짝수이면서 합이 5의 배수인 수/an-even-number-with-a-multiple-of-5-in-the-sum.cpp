#include <iostream>

using namespace std;

int n;

int main() {
    cin >> n;

    // Please write your code here.
    int a = n/10;
    int b = n%10;
    if(b%2==0 && (a+b)%5==0){
        cout << "Yes";
    }
    else{
        cout << "No";
    }

    return 0;
}