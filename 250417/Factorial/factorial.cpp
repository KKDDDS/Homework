#include <iostream>

using namespace std;

int N;

int solution(int n){
    if(n==0){
        return 1;
    }
    return n*solution(n-1);
}
int main() {
    cin >> N;

    // Please write your code here.
    cout << solution(N);
    return 0;
}