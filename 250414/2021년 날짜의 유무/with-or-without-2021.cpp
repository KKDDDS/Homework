#include <iostream>

using namespace std;

int M, D;

int main() {
    cin >> M >> D;

    // Please write your code here.
    int arr[7] = {1,3,5,7,8,10,12};
    bool is_in = false;
    for (int i = 0; i < 7; i++) {
        if (arr[i] == M) {
            is_in = true;
            break;
        }
    }
    if(is_in){
        if(D<=31){
            cout << "Yes";
            return 0;
        }
    }
    else if(M==2){
        if(D<=28){
            cout << "Yes";
            return 0;
        }
    }
    else{
        if(D<=30){
            cout << "Yes";
            return 0;
        }
    }
    cout << "No";
    return 0;
}