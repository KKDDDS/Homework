#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    if(3000<=n){
        cout << "book";
    }
    else if  (1000<=n){
        cout << "mask";
    }
    else{
        cout << "no";
    }
    return 0;
}