#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int main() {
	int p,a,b,c,d,n;
	cin >> p >> a >> b >> c >> d >> n;
	double prices[n];
	for (int i = 1 ; i <= n ; i++ ){
		prices[i - 1] =  p * (sin (a * i + b) + cos( c * i + d ) + 2);
	}
	double mini = 0;
	double val = 0;
	for (int i = 0 ; i < n ; i ++) {
		val = max(mini - prices[i], val);
		if (mini < prices[i]) {
			mini = prices[i];
		}
	}
	printf("%.8f\n", val);

}
