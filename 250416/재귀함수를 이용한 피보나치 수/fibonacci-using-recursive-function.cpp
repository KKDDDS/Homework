#include <iostream>

using namespace std;

int N;

int solution(int n){
    if(n==1 || n==2){
        return 1;
    }
    return solution(n-1)+solution(n-2);
    
}


int main() {
    cin >> N;

    // Please write your code here.
    cout << solution(N);
    return 0;
}