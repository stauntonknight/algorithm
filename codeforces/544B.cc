#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	int N, K;
	scanf("%d%d", &N,&K);
	int bottom = (N + 1) / 2;
	int above = N / 2;
	int maxim = bottom * ((N  + 1) / 2) + above * (N / 2);
	if (maxim >= K) {
		cout << "YES\n";
		for (int i = 0,t=K; i < N ; i++) {
			for (int j = 0 ; j < N ; j++) {
				if (t == 0) cout << "S";
				else if (i % 2 == j % 2) {
					cout << "L";
					t--;
				} else cout << "S" ;
			}
			cout << endl;
		}
	} else {
		cout << "NO\n";
	}
}
