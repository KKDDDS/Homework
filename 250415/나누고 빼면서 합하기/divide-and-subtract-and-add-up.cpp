#include <iostream>

using namespace std;

int n, m;
int A[100];

int solution(){
    int tot = A[m-1];
    while(m!=1){
        if(m%2==0){
            m /=2;
        }
        else{
            m -=1;
        }
        tot += A[m-1];
    }
    return tot;
}

int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    // Please write your code here.
    int tot = solution();
    cout << tot;
    return 0;
}