#include <iostream>

using namespace std;

int N;

int solution(int n){
    if(n==1 | n==2){
        return n;
    }
    return n+solution(n-2);
}

int main() {
    cin >> N;

    // Please write your code here.
    cout << solution(N);
    return 0;
}