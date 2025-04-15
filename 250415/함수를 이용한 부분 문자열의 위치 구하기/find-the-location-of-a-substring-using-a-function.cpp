#include <iostream>
#include <string>

using namespace std;

string text;
string pattern;
int solution(string t, string p){
    int t_l = t.length();
    int p_l = p.length();
    for(int i=0;i<=t_l-p_l;i++){
        if(t[i]==p[0]){
            for(int j=0;j<p_l;j++){
                if(j==p_l-1 && t[i+j]==p[j]){
                    return i;
                }
                else if(t[i+j]==p[j]){
                    continue;
                }
                else{
                    break;
                }
            }
        }
    }
    return -1;
}

int main() {
    cin >> text;
    cin >> pattern;

    // Please write your code here.
    cout << solution(text, pattern);
    return 0;
}