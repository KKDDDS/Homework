#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    int cnt = 0;

    for(int i=0; i<=N; i++){
        if(i%2!=0 && i%3!=0 && i%5!=0){
            cnt += 1;
        }
    }
    cout << cnt;
    return 0;
}