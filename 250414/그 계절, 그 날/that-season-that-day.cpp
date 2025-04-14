#include <iostream>
#include <array>

using namespace std;

int Y, M, D;

bool is_yoon(int Y){
    bool temp = false;
    if(Y%4==0){
        if(Y%100==0){
            if(Y%400==0){
                temp = true;
            }
        }
        else{
            temp = true;
        }
    }
    return temp;
}

int weather(bool yoon, int M, int D){
    array<int, 7> arr = {1,3,5,7,8,10,12};
    bool is_in = false;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == M) {
            is_in = true;
            break;
        }
    }
    int num = -1;
    if(is_in){
        if(D<=31){
            num = M;
        }
    }
    else if(yoon && M==2){
        if(D<=29){
            num = M;
        }
    }
    else if(M ==2){
        if(D<=28){
            num = M;
        }
    }
    else{
        if(D<=30){
            num = M;
        }
    }
    return num;
}



int main() {
    cin >> Y >> M >> D;

    // Please write your code here.
    int month = weather(is_yoon(Y), M, D);
    if(month==-1){
        cout << -1;
    }
    else if(month==3 || month==4 || month==5){
        cout << "Spring";
    }
    else if(month==6 || month==7 || month==8){
        cout << "Summer";
    }
    else if(month==9 || month==10 || month==11){
        cout << "Fall";
    }
    else{
        cout << "Winter";
    }
    
    return 0;
}