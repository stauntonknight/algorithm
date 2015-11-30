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
 int kases;
 cin >> kases;
 for (int i = 0 ; i < kases; i++) {
   cout << "Case #" << i + 1 << ": ";
   cout << endl;
   int N, M;
   cin >> N >> M;
   long long A[N];
   for (int i = 0 ; i < N ; i++) cin >> A[i];
   for (int i = 0 ; i < M ; i++) {
     int L, R;
     cin >> L >> R;
     int K = R - L + 1;
     double ans = 1.0;
     for (int j = L; j<= R; j++) {
       ans = ans * pow(A[j], 1.0/K);
     }
     printf("%0.7f\n", ans);
   }
 }
}

