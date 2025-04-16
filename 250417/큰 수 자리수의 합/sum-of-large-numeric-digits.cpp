#include <iostream>

using namespace std;

int a, b, c;

int solution(int n){
    if(n<10){
        return n;
    }
    return solution(n/10)+solution(n%10);
}

int main() {
    cin >> a >> b >> c;

    // Please write your code here.
    int temp = a*b*c;
    cout << solution(temp);
    return 0;
}