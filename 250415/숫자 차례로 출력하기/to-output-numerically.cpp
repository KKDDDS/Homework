#include <iostream>

using namespace std;

int N;

void solution1(int n){
    if(n==0){
        return;
    }
    solution1(n-1);
    cout << n << " ";

}
void solution2(int n){
    if(n==0){
        return;
    }
    solution2(n-1);
    cout << N+1-n<<" ";
}

int main() {
    cin >> N;

    // Please write your code here.
    solution1(N);
    cout << endl;
    solution2(N);
    return 0;
}