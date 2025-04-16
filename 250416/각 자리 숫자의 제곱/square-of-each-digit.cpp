#include <iostream>

using namespace std;

int N;
int solution(int n){
    if(n<10){
        return n*n;
    }
    return solution(n/10)+((n%10)*(n%10));
}

int main() {
    cin >> N;

    // Please write your code here.
    cout << solution(N);

    return 0;
}