#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N, M;
    cin >> N >> M;
    int matrix_1[N][M], matrix_2[N][M];
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin >> matrix_1[i][j];
        }
    }
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin >> matrix_2[i][j];
        }
    }
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            if(matrix_1[i][j]==matrix_2[i][j]){
                cout << 0 << " ";
            }
            else{
                cout << 1 << " ";
            }
        }
        cout << endl;
    }
    return 0;
}