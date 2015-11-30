#include <iostream>
#include <cstdio>
#include <cmath>
#include <set>
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
	while(T--) {
		int N;
		cin >> N;
		getchar();
		set<string> engines;
		for (int i= 0 ;i < N ; i++) {
			string engine;
			getline(cin, engine);
			engines.insert(engine);
		}
		int Q;
		cin >> Q;
		getchar();
		map<string, bool> blocked;
		int bcount = 0;
		int nswitch = 0;
		for (int i = 0 ; i < Q; i++) {
			string query;
			getline(cin, query);
			if (engines.find(query) != engines.end() && blocked.count(query) == 0) {
				if (bcount == N - 1) {
					nswitch++;
					bcount = 0;
					blocked.clear();
				}
				bcount ++;
				blocked[query] = true;
			}
		}
		cout << "Case #" << K - T << ": " << nswitch << endl;
	}
}
