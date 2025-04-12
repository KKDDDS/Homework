#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    int a, b;
    int tot;
    for(int i=0; i<N; i++){
        cin >> a >> b;
        tot = 0;
        for(a;a<=b;a++){
            if(a%2==0){
                tot += a;
            }
        }
        cout << tot << endl;
    }
    return 0;
}