#include <iostream>
using namespace std;

// 사칙연산 함수 정의
int calculate(int a, char o, int c) {
    switch (o) {
        case '+':
            return a + c;
        case '-':
            return a - c;
        case '*':
            return a * c;
        case '/':
            return a / c;
    }
}

int main() {
    int a, c;
    char o;
    cin >> a >> o >> c;

    char array[] = {'+', '-', '/', '*'};
    bool isInArray = false;

    for (int i = 0; i < 4; ++i) {
        if (o == array[i]) {
            isInArray = true;
            break;
        }
    }

    if (isInArray) {
        int result = calculate(a, o, c);
        cout << a << " "<< o << " " << c << " = " << result;
    }
    else {
        cout << "False";
    }

    return 0;
}
