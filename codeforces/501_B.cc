#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <string>

using namespace std;

int main() {
    int N;
    scanf("%d", &N);
    set<string> used;
    map<string, string> orig;
    map<string, string> curr;
    for (int i = 0 ; i < N ; i++) {
        string a,b;
        cin >> a>> b;
        if (!used.insert(b).second) {
            continue;
        }
        if (curr.count(a) == 0) {
            orig[a] = b;
            curr[b] = a;
        } else {
            orig[curr[a]] = b;
            curr[b] = curr[a];
        }
    }
    int count= 0;
    for (std::map<string, string>::iterator it = orig.begin(); it!= orig.end(); it++) {
        if (it->first != it->second) count++;
    }
    cout << count << endl;
    for (std::map<string, string>::iterator it = orig.begin(); it!= orig.end(); it++) {
        cout << it->first << " " << it->second << endl;
    }
}
