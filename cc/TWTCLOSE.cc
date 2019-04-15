#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main() {
  int N, K;
  cin >> N >> K;
  cin.ignore();
  bool A[N + 1];
  string s;
  int kount = 0;
  int index;
  while (K--) {
    cin >> s;
    if (s == "CLOSEALL") {
      memset(A, 0, sizeof(A));
      kount = 0;
    } else {
      cin >> index;
      A[index] = !A[index];
      kount = kount + (A[index] ? 1 : -1);
    }
    cout << kount << endl;
  }
}
