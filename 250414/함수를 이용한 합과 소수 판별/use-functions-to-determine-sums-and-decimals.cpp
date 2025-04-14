#include <iostream>

using namespace std;

int a, b;

bool is_Prime(int n){
    bool result = true;
    for(int i=2;i<n;i++){
        if(n%i==0){
            result = false;
            break;
        }
    }
    if(result==true){
        int x = n%10;
        int y = n/10;
        if((x+y)%2!=0){
            result = false;
        }
    }
    return result;
}

int main() {
    cin >> a >> b;
    int cnt = 0;
    // Please write your code here.
    for(a; a<=b;a++){
        bool result = is_Prime(a);
        if(result){
            cnt += 1;
        }
    }
    cout << cnt;
    return 0;
}