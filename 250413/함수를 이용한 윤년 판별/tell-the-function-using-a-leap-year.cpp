#include <iostream>

using namespace std;

int y;
bool is_Yoon(int y){
    if(y%4==0){
        if(y%100==0 && y%400 != 0){
            return false;
        }
        else{
            return true;
        }
    }
    return false;
}


int main() {
    cin >> y;

    // Please write your code here.
    if(is_Yoon(y)){
        cout << "true";
    }
    else{
        cout << "false";
    }
    return 0;
}