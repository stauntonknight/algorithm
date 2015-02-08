#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        long long N, K;
        scanf("%lld%lld", &N, &K);
        long long mprofit = 0;
        long long A[N];
        for (int i = 0 ; i < N ; i++) {
            scanf("%lld", &A[i]);
        }
        for (int i = 0; i < N ; i++) {
            long long P;
            scanf ("%lld", &P);
            long long profit = (K / A[i]) * P;
            if (profit > mprofit) mprofit = profit;
        }
        printf("%lld\n", mprofit);
    }
}
