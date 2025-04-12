#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int nums[10] = {0};
    for(int i=0;i<10;i++){
        cin >> nums[i];
    }
    int cnt_3 = 0;
    int cnt_5 = 0;

    for(int i=0; i<10; i++){
        if(nums[i]%3==0){
            cnt_3 += 1;
        }
        if(nums[i]%5==0){
            cnt_5 += 1;
        }
    }

    cout << cnt_3 <<" "<< cnt_5;
    return 0;
}