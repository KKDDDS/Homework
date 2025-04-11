#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int gender, age;
    cin >> gender >> age;

    if(gender){
        if(age >= 19){
            cout << "WOMAN";
        }
        else{
            cout << "GIRL";
        }
    }
    else{
        if(age >=19){
            cout << "MAN";
        }
        else{
            cout << "BOY";
        }
    }
    return 0;
}