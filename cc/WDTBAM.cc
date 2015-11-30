#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <map>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

int main() {
  int T;
  scanf("%d", &T);;
  while (T--) {
    int N;
    scanf("%d", &N);
    string correct, actual;
    cin >> correct;
    cin >> actual;
    int total_c = 0;
    for (int i = 0 ; i < correct.size(); i++) if (correct[i] == actual[i]) total_c++;
    long long w[N+1];
    for (int i = 0 ; i < N + 1 ; i++) cin >> w[i];
    long long ans = -1;
    for (int i = total_c ; i >= 0 ; i--) {
      if (w[i] > ans) ans = w[i];
    }
    if (total_c == N) ans = w[N];
    cout << ans << endl;
  }
}

