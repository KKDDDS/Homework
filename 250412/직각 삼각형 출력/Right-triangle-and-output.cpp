#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    for(int i=1; i<2*N; i+=2){
        for(int j=0;j<i;j++){
            cout<<"*";
        }
        cout << endl;
    }
    return 0;
}