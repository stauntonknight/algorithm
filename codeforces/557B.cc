#include <cmath>
#include <algorithm>
#include <cstdio>
#include <iostream>

using namespace std;

int main() {
	long long n,w;
	cin >> n >> w;
	long long a[2*n];
	for (long long i = 0 ; i < n ; i++) {
		cin >> a[i] >> a[i+n];
	}
	sort(a, a+2*n);
	double minim = a[0];
	if (a[n] < 2 * a[0]) {
		minim = a[n] / 2.0;
	}
	double total = 3 * n * minim;
	if (total > w) {
		total = w;
	}
	printf("%.6f", total);
}
