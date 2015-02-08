#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

int P = 1000;

int main() {
  map<int, int> count;
  int total = 0;
  int p = 0;
  for (int i = 1; i < P/2 ; i++) {
    for (int j = 1; j < i ; ++j ){
      int zs = i * i - j * j;
      int z = sqrt (zs);
      if (z >= j &&  z * z == zs)  {
        int peri = j + z + i;
        count[peri]++;
        int total_curr = count[peri];
        if ( total_curr > total ) {
          total = total_curr;
          p = peri;
        }
      }
    }
  }
  cout << p << endl;
}
