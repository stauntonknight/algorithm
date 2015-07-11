#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>

using namespace std;

int main() {
	int N;
	scanf("%d",&N);
	string s;
	for (int i = 0 ; i < N ;i ++) {
		cin >> s;
		int sum = 0;
		for (int i = 0 ; i < s.size(); i++) {
			sum += ('9' - s[i]);
		}
		sum = sum % 9;
		cout << min(sum, 9-sum) << endl;
	}
}
