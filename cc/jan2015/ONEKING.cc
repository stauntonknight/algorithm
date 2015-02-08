#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int N;
        scanf ("%d", &N);
        vector<pair<int, int> > end(N);
        int start_map[N];
        for (int i = 0; i < N ; i++) {
            int start;
            scanf("%d%d", &start, &end[i].first);
            end[i].second = i;
            start_map[i] = start;
        }
        sort (end.begin(), end.end());
        int max = -1;
        int count = 0;
        for (int i = 0; i < end.size(); i++) {
           if (max < start_map[end[i].second]) {
               max = end[i].first;
               count++;
           }
        }
        cout << count << endl;
    }
}
