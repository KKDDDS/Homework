#include <iostream>

using namespace std;

int n, m;
int arr[100];

int solution(int n, int m){
    int tot = 0;
    for(int i=n-1;i<m;i++){
        tot += arr[i];
    }
    return tot;
}

int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    for (int i = 0; i < m; i++) {
        int a1, a2;
        cin >> a1 >> a2;
        int sum = solution(a1, a2);
        cout << sum << endl;

    }

    // Please write your code here.

    return 0;
}