#include <iostream>

using namespace std;

bool check2(int x){
    return x!=0&&x%3==0;
}

bool check1(int a)
{
    int b, c, d, e, f, g, h, z;
    b=a%10;
    c=(a/10)%10;
    d=(a/100)%10;
    e=(a/1000)%10;
    f=(a/10000)%10;
    g=(a/100000)%10;
    h=(a/1000000)%10;
    z=check2(b)||check2(c)||check2(d)||check2(e)||check2(f)||check2(g)||check2(h)||a%3==0;
    return z;
}

int main() {
    int a, b;
    int cnt=0;
    cin >>a >>b;
    for(int i=a; i<=b; i++)
    {
        if (check1(i))
        {
            cnt++;
        }
    }
    cout << cnt;
    return 0;
}