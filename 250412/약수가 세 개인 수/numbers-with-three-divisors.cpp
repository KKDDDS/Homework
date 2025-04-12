#include <iostream>

using namespace std;

int main() {
    int start, end;
    cin >> start >> end;
    int cnt = 0;
    for(start; start<=end; start++){
        for(int i=2; i<start; i++){
            if(start%i==0){
                if(i*i==start){
                    cnt +=1;
                    break;
                }
                else{
                    break;
                }
            }
        }
    }
    cout << cnt;

    return 0;
}
