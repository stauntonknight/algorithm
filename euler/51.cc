#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

inline bool is_match(string &s, string &patt) {
  bool match = true;
  set<int> dont_care;
  int index = 0;
  for (char ch : patt) {
    if (ch == '*') {
      dont_care.insert(s[index]);
    } else if (s[index] != ch) {
      match = false;
      break;
    }
    index++;
  }
  return match && dont_care.size() == 1;
}

int main() {
  long K = 999999l;

  bool *a = new bool[K];
  for (long  i = 0 ; i < K; i++) {
    a [i] = true;
  } 
  for (long  i = 2; i * i <= K; i++) {
    if (!a[i]) continue;
    for (long  j = i*i ; j < K; j+=i)  {
      a[j] = false;
    }
  }
  vector<long > n;
  for (long  i = 1; i < K; i++) {
    if (a[i] && i > 100000) {
      n.push_back(i);
    }
  }
  delete a;
  cout << n.size() << endl;
  set<string> patts;
  set<long > all;
  long  done = 0;
  for (long i : n) {
    map<long , long > s;
    long t = i;
    while (t) {
      s[t%10]++;
      t /= 10;
    }
    for (long  j = 0 ; j <= 9; j++) {
      if (s[j] >= 3) {
        all.insert(i);
        char ch[10];
        sprintf(ch, "%d", i);
        string str(ch);
        for (long  k = 0 ; k < str.size(); k++) {
          if (str[k] == j + '0') {
            str[k] = '*';
          }
        }
        patts.insert(str);
      }
    }
  }
  cout << patts.size() << endl;
  cout << all.size() << endl;
  map<string, vector<long> > ans;
  for (const long t : all) {
    char ch[10];
    sprintf(ch, "%d", t);
    string num(ch);
    for (string patt : patts) {
      if (is_match(num, patt)) {
        ans[patt].push_back(t);
      }
    }
  }
  for (auto &t : ans) {
    if (t.second.size() >= 8) {
      cout << t.first << endl;
      for (long val : t.second) {
        cout << val << " ";
      }
      cout << endl;
    }
  }
}

