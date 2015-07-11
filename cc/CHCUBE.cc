#include <cstdio>
#include <iostream>
#include <string>
#include <map>

using namespace std;


int main() {
	int T;
	scanf("%d", &T);
	string s[6];
	while(T--) {
		bool poss = false;
		for (int i = 0; i < 6; i++) {
			cin >> s[i];
		}
		for (int i = 0 ; i < 2 ; i++)
			for (int j= 2; j < 4; j++) 
				for (int k = 4;k < 6; k++)
					if (s[i] == s[j] && s[j] == s[k]) poss = true;
		if (poss) {
			cout << "YES" ;
		} else cout << "NO";
		cout << endl;
	}

}
