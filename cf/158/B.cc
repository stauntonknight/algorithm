#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int main() {
  int N;
  scanf("%d", &N);
  int A[N];
  int count[5];
  memset(count , 0, sizeof(count));
  for (int i = 0; i < N ; i++) {
    scanf("%d", &A[i]);
    count[A[i]] ++;
  }
  int ans = count[4];
  count[4] = 0;
  int oneAndThree = min(count[1], count[3]);
  count[1] -= oneAndThree;
  count[3] -= oneAndThree;
  ans = ans + oneAndThree;
  // Take care of 2 people.
  ans = ans + count[2] / 2;
  count[2] = count[2] % 2;

  ans = ans + count[1] / 4;
  count[1] = count[1] % 4;
  ans = ans + count[3];
  if (count[2]) {
    ans ++;
    count[1] -= 2;
  }
  if (count[1] > 0) {
    ans++;
  }
  cout << ans << endl;
  return 0;
}
