#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int N;
        scanf("%d", &N);
        int A[N];
        int sum = 0;
        for (int i = 0; i < N ; i++) {
            scanf("%d", &A[i]);
            sum += A[i];
        }
        int min = 0;
        for (int i = 0; i < N ; i++) {
            min = min + (A[i] > 0 ? A[i] - 1 : A[i]);
        }
        if (min < 100 && sum >= 100)  {
            cout << "YES";
        } else cout << "NO";
        cout << endl;
    }
}
