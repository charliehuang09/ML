#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <map>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <list>
#include <stack>
#define ll long long
using namespace std;

int main(){
    int length;
    cin >> length;
    int input[length];
    int l[length];
    int r[length];
    for (int i = 0; i < length; i++) cin >> input[i];
    stack<int> s;

    for (int i = 0; i < length; i++){
        if (s.empty()){
            s.push(i);
            l[i] = i;
            continue;
        }
        if (input[s.top()] < input[i]){
            s.push(i);
            l[i] = i;
            continue;
        }
        while(!s.empty() && input[s.top()] >= input[i]){
            s.pop();
        }
        if (!s.empty()) l[i] = s.top() + 1;
        else l[i] = 0;
        if (s.empty() || input[s.top()] < input[i]) s.push(i);
    }
    while(!s.empty()) s.pop();

    for (int i = length - 1; i >= 0; i--){
        if (s.empty()){
            s.push(i);
            r[i] = i;
            continue;
        }
        if (input[s.top()] < input[i]){
            s.push(i);
            r[i] = i;
            continue;
        }
        while(!s.empty() && input[s.top()] >= input[i]){
            s.pop();
        }
        if (!s.empty()) r[i] = s.top() - 1;
        else r[i] = length - 1;
        if (s.empty() || input[s.top()] < input[i]) s.push(i);
    }
//    for (int i = 0; i < length; i++) cout << l[i] << " ";
//    cout << "\n";
//    for (int i = 0; i < length; i++) cout << r[i] << " ";
//    cout << "\n";
    int output = 0;
    for (int i = 0; i < length; i++) output = max(output, input[i] * (r[i] - l[i] + 1));
    cout << output;
}
/*

*/