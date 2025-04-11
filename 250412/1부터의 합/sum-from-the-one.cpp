#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    int tot=0;
    int i=1;
    while(1){
        tot += i;
        if(tot>=N){
            cout<< i;
            break;
        }
        i += 1;
    }
    return 0;
}