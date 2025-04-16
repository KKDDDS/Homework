#include <iostream>

using namespace std;

int n;
int cnt = 0;
int solution(int n, int &cnt){
    if(n==1){
        return 1;
    }
    if(n%2==0){
        cnt += 1;
        return solution(n/2, cnt);
    }
    else{
        cnt += 1;
        return solution(3*n+1, cnt);
    }
}

int main() {
    cin >> n;

    // Please write your code here.
    solution(n, cnt);
    cout << cnt;

    return 0;
}