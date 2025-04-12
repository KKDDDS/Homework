#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    string fruit[5] = {"apple", "banana", "grape", "blueberry", "orange"};
    char a;
    cin >> a;
    int cnt = 0;
    int len = sizeof(fruit) / sizeof(fruit[0]);
    for(int i=0; i<len; i++){
        if(fruit[i][2]==a || fruit[i][3]==a){
            cout<< fruit[i] <<"\n";
            cnt += 1;
        }
    }
    cout << cnt;
    return 0;
}