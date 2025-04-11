#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    int arr[N];
    for(int i=0; i<N; i++){
        cin >> arr[i]; 
    }
    for(int i=0;i<N;i++){
        cout << arr[i]*arr[i] << " ";
    }
    return 0;
}