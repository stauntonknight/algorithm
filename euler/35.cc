#include <iostream>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main() {
  int N = 1000000;
  int A[N];
  int num[N];
  int K = 0;
  for (int i = 0 ;i < N ; i++) A[i] = 1;
  A[1] = 0;
  for (int i = 2 ; i*i <= N ; i++) {
    if (!A[i]) continue;
    for (int j = i*i; j < N ;  j += i) {
      A[j] = 0;
    }
  }
  for (int  i = 2 ; i< N ;i ++) if (A[i]) num[K++] = i;
  int count = 0;
  for (int i = 0; i <K ; i++) {
    char buffer[20];
    sprintf(buffer, "%d", num[i]);
    int len = strlen(buffer);
    for (int i = 0; i < len - 1; i++) buffer[i+len] = buffer[i];
    buffer[len + len] = '\0';
    bool is = true;
    for ( int j = 0; j < len ; j++) {
      char ch = buffer[j+len];
      buffer[j+len] = '\0';
      int x = atoi(buffer + j);
      if (!A[x]) {
        is = false;
        break;
      }
      buffer[j+len] = ch;
    }
    if (is) {
      count++;
      cout << num[i] << endl;
    }
  }
  cout << count << endl;
}
