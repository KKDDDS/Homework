#include <iostream>
#include <string>

using namespace std;

string A;
bool solution(string A){
    int temp = A.length();
    bool right = false;
    for(int i=0; i<temp-1; i++){
        if(A[i] != A[i+1]){
            right = true;
            break;
        }
    }
    return right;
}

int main() {
    cin >> A;

    // Please write your code here.
    bool n = solution(A);
    if(n){
        cout << "Yes";
    }
    else{
        cout << "No";
    }
    return 0;
}