#include <iostream>

using namespace std;

int N;
int cnt=-1;

int solution(int n){
    cnt += 1;
    if(n==1){
        return 0;
    }
    if(n%2==0){
        return solution(n/2);
    }
    else{
        return solution(n/3);
    }
}

int main() {
    cin >> N;

    // Please write your code here.
    solution(N);
    cout << cnt;
    return 0;
}