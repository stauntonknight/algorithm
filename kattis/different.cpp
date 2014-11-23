#include <iostream>

using namespace std;

int main() {
	long long a,b;
	while(cin >> a >> b) {
		if (a < b ) {
			long long t = a;
			a = b;
			b = t;
		}
		cout << a - b << endl;
	}
}
