#include <iostream>

using namespace std;

int n;
int arr[100];
int findMax(int arr[], int n) {
    if (n == 1)
        return arr[0];
    return max(arr[n - 1], findMax(arr, n - 1));
}

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Please write your code here.
    cout << findMax(arr, n);
    return 0;
}