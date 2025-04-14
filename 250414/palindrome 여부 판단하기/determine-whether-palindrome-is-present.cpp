#include <iostream>
#include <string>

using namespace std;

string A;
bool is_p(string &s){
    int num = s.length();
    for(int i=0; i<num/2; i++){
        if(s[i] != s[num-1-i]){
            return false;
        }
    }
    return true;
}

int main() {
    cin >> A;

    // Please write your code here.

    if(is_p(A)){
        cout << "Yes";
    }
    else{
        cout << "No";
    }
    return 0;
}