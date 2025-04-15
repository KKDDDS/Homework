#include <iostream>

using namespace std;

int n;
void solution(int n){
    if(n==0){
        return;
    }
    solution(n-1);
    for(int i=0;i<n;i++){
        cout << "*";
    }
    cout << endl;
}

int main() {
    cin >> n;

    // Please write your code here.
    solution(n);
    return 0;
}