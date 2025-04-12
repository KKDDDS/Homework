#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    for(int i=0; i<N;i++){
        int num;
        if(i%2==0){
            num = 1;
        }
        else{
            num = N;
        }
        for(int j=0; j<N;j++){
            cout<<num;
            if(i%2==0){
                num += 1;
            }
            else{
                num -= 1;
            }
        }
        cout << endl;
    }
    return 0;
}