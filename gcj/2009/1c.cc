#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <map>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

int main() {
	int T;
	scanf("%d", &T);
	int K = T;
	while (T--) {
		string s;
		cin >> s;
		long long ans = 0;
		map<char, int> mapp;	
		int mini = 0;
		for (int i = 0 ; i <s.size(); i++) {
			if (i ==0 ) {
				mapp[s[i]] = 1;
			} else {
				if (mapp.count(s[i]) != 0) continue;
				mapp[s[i]] = mini;
				mini ++;
				if (mini == 1) mini++;
			}
		}
		int base = mini == 0 ? 2 : mini;
		long long  mul = 1;
		for (int i = s.size() - 1; i>= 0; i--) {
			ans += mul * mapp[s[i]];
			mul = mul * base;
		}
		cout << "Case #" << K-T<<": ";
		cout << ans << endl;
	}
}
