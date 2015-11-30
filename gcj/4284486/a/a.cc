#include <iostream>

using namespace std;

int getNum(long long i, int target) {
    if (i <= 1) return 0;
    long long numDig = (1ll << target) - 1;
    if (i == numDig / 2 + 1) {
        return 0;
    } else if (i  <= numDig / 2) {
        return getNum(i, target - 1);
    } else {
        return 1 - (getNum(numDig - i + 1, target - 1));
    }
    return -1;  
}

int main() {
    int N;
    cin >> N;
    for (int i = 0 ; i < N ;i++) {
        long long K;
        cin >> K;
        int target = 0;
        while ((1ll<<target) <= K) {
            target++;
        }
        cout << "Case #" << i + 1 << ": " << getNum(K, target) << endl;
    }
    return 0;
}
