#include <iostream>

using namespace std;

int N;

void solution(int n){
    if(n == 0){
        return;
    }
    solution(n-1);
    cout << "HelloWorld" << endl;
}

int main() {
    cin >> N;

    // Please write your code here.
    solution(N);

    return 0;
}