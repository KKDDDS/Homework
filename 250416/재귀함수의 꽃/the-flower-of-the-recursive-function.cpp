#include <iostream>

using namespace std;

int N;

void solution(int N){
    if(N==0){
        return;
    }
    cout << N << " ";
    solution(N-1);
    cout << N << " ";
}

int main() {
    cin >> N;

    // Please write your code here.
    solution(N);
    return 0;
}