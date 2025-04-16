#include <iostream>

using namespace std;

int N;

int solution(int n){
    if(n==1){
        return 2;
    }
    if(n==2){
        return 4;
    }
    return (solution(n-1)*solution(n-2))%100;
}

int main() {
    cin >> N;

    // Please write your code here.
    cout << solution(N);
    return 0;
}