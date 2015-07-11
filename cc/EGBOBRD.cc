#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	while (T--) {
		int N;
	        long long K;
		scanf("%d%lld", &N, &K);
		int A[N];
		long long numBU = 0;
	       	long long left = 0;
		for (int i = 0 ; i < N; i ++) {
			scanf("%d", &A[i]);
			if (left < A[i]) {
				int numBReq = ceil((A[i] - left + 0.0) / K);
				left = left + numBReq * K;
				numBU += numBReq;
			}
			left = left - A[i];
			if (left > 0 ) left --;
		}
		cout << numBU << endl;
	}
}
