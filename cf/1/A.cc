#include <iostream>
#include <cmath>

using namespace std;

int main() {
  long long H,W,N;
  cin >> W >> H >> N;
  double Nd = N + 0.0;
  int ans = ceil(W/Nd) + ceil(H/Nd);
  cout << ans << endl;
  return 0;
}
