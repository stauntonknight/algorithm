#include<iostream>
#include <cstdio>
#include <string>

using namespace std;

bool isVowel(char c) {
  switch (c) {
    case 'a':
    case 'A':
    case 'e':
    case 'E':
    case 'i':
    case 'I':
    case 'o':
    case 'O':
    case 'u':
    case 'U':
    case 'y':
    case 'Y':
     return true;
  }
  return false;
}

int main() {
  string s;
  cin >> s;
  for (int i = s.size() - 1; i >= 0 ; --i) {
    if (isVowel(s[i])) {
      s.erase(i, 1);
    } else if (s[i] != '.') {
      if (s[i] >= 'A' && s[i] <= 'Z') {
        s[i] = s[i] - 'A' + 'a';
      }
      s.insert(i, ".");
    }
  }
  cout << s << endl;
  return 0;
}
