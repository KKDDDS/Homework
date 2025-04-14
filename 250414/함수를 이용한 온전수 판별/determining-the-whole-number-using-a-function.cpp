#include <iostream>

using namespace std;

int A, B;

int main() {
    cin >> A >> B;

    // Please write your code here.
    int cnt = 0;
    for(A; A<=B; A++){
        if((A%2 !=0)&&(A%10 !=5)&&(A%9 ==0||A%3 !=0)){
            cnt +=1;
        }
    }
    cout << cnt;
    return 0;
}