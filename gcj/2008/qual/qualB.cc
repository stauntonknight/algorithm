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
	for (int kase = 1; kase <= T; kase++) {
		int turn;
		cin >> turn;
		getchar();
		int na, nb;
		cin >> na >> nb;
		getchar();
		int reqA[1441], reqB[1441], haveA[1441], haveB[1441];
		memset(reqA, 0, sizeof(reqA));
		memset(haveA, 0, sizeof(haveA));
		memset(reqB, 0, sizeof(reqB));
		memset(haveB, 0, sizeof(haveB));
		for (int i = 0 ; i < na ;i ++ ) {
			string time;
			int h,m;

			cin >> time;
			sscanf(time.c_str(), "%d:%d", &h, &m);
			reqA[h*60 + m]++;

			cin >> time;
			sscanf(time.c_str(), "%d:%d", &h, &m);
			int tim = h * 60 + m + turn;
			if (tim <= 1440) {
				haveB[tim]++;
			}
		}
		for (int i = 0 ; i < nb ;i ++ ) {
			string time;
			int h,m;
			cin >> time;
			sscanf(time.c_str(), "%d:%d", &h, &m);
			reqB[h*60 + m]++;


			cin >> time;
			sscanf(time.c_str(), "%d:%d", &h, &m);
			int tim = h * 60 + m + turn;
			if (tim <= 1440) {
				haveA[tim]++;
			}
		}
		int have = 0, numReq = 0;
		for (int i = 0 ; i < 1441; i++) {
			have += haveA[i];
			have -= reqA[i];
			if (have < 0) {
				numReq = numReq - have;
				have = 0;
			}
		}
		cout << "Case #" << kase << ": " << numReq;
		have = 0; numReq = 0;
		for (int i = 0 ; i < 1441; i++) {
			if (haveB[i] > 0) {
			}
			if (reqB[i] > 0) {
			}
			have += haveB[i];
			have -= reqB[i];
			if (have < 0) {
				numReq = numReq - have;
				have = 0;
			}
		}
		cout << " " << numReq << endl;
	}
}
