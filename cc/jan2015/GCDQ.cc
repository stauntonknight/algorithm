#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int N, Q;
        scanf ("%d%d", &N, &Q);
        int A[N];
        for (int i = 0; i < N ; i++) scanf("%d", &A[i]);
        int gcdL[N];
        int gcdR[N];
        gcdL[0] = A[0];
        for (int i = 1; i < N ; i++) {
            gcdL[i] = __gcd(gcdL[i-1], A[i]);
        }
        gcdR[N-1] = A[N-1];
        for (int i = N-2; i >=0 ; i--) {
            gcdR[i] = __gcd(gcdR[i+1], A[i]);
        }
        for (int i = 0; i < Q ; i++) {
            int L,R;
            scanf("%d%d", &L, &R);
            if ( L == 1) printf("%d", gcdR[R]);
            else if (R == N) printf("%d", gcdL[L - 2]);
            else printf("%d", __gcd(gcdL[L - 2], gcdR[R]));
            printf("\n");
        }
    }
}
