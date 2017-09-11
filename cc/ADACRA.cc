#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {
  int T;
  cin >> T;
  while (T--) {
    string s;
    cin >> s;
    int cost[2] = {0,0};
    char last;
    for (int i = 0 ; i < s.size() ; i++) {
      char ch = s[i] == 'U' ? '0' : '1';
      if (ch == last) continue;
      else { 
        last = ch;
        cost[ch - '0']++;
      }
    }
    cout << min(cost[0], cost[1]) << endl;
  }
}
