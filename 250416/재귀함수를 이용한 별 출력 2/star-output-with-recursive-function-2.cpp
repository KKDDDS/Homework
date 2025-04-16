#include <iostream>

using namespace std;

int n;
void solution(int N){
    if(N==0){
        return;
    }
    for(int i=0; i<N; i++){
        cout << "*" << " ";
    }
    cout << endl;
    solution(N-1);
    for(int i=0; i<N; i++){
        cout << "*" << " ";
    }
    cout << endl;
}

int main() {
    cin >> n;

    // Please write your code here.
    solution(n);
    return 0;
}