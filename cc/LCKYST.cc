#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;

bool isPoss(long long a) {
	while (a != 0 && a % 10 == 0) a = a/10;
	return a%10 == 5;
}

long long getAns(long long t) {
	while (isPoss(t)) {
		t = t * 4;
	} 
	return t;
}

int main() {
	int N;
	scanf("%d", &N);
	long long A[N];
	for (int i = 0 ; i < N ; i++) {
		cin >> A[i];
		cout << getAns(A[i]) << endl;
	}
}
