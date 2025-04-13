#include <iostream>

using namespace std;

bool PrimeNumber(int x, int b){
    for(int i=2; i<=b; i++){
        if(x!=i && x%i == 0){
            return false;
        }
    }
    return true;
}

int main() {
    int a, b;
    int sum=0;
    cin>>a>>b;
    for(int i=a; i<=b; i++){
        if(a==1){
            continue;
        }   
        if(PrimeNumber(i, b))
            sum+=i;
    }
    cout<<sum;
    return 0;
}

