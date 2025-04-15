#include <iostream>

using namespace std;

int a, b;
void solution(int &n, int &m){
    if(n<m){
        n += 10;
        m *= 2;
    }
    else{
        n *= 2;
        m += 10;
    }
}

int main() {
    cin >> a >> b;

    // Please write your code here.
    solution(a, b);
    cout<< a << " " << b;
    

    return 0;
}