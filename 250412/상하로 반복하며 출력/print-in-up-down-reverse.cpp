#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    int matrix[N][N];
    for(int j=0; j<N; j++){
        int num;
        if(j%2==0){
            num = 1;
        }
        else{
            num = N;
        }
        for(int i=0; i<N; i++){
            matrix[i][j] = num;
            if(j%2==0){
                num += 1;
            }
            else{
                num -= 1;
            }
            
        }
    }
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cout << matrix[i][j];
        }
        cout << endl;
    }
    return 0;
}