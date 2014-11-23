#include <iostream>
#include <cassert>
#include<cstdio>
#include <map>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int T;
    scanf("%d",&T);
    while(T--) {
        int r, R;
        map<double, vector<double> > points;
        scanf("%d%d", &r, &R);
        int C;
        scanf("%d", &C);
        for (int i = 0; i < C; i++) {
            int x, y;
            scanf("%d%d", &x, &y);
            points[(y+0.0)/x].push_back(sqrt(x * x + y * y));
        }
        double max_width = R - r;
        for (map<double, vector<double> >::iterator it = points.begin(); it != points.end(); ++it) {
            vector<double> distances = it->second;
            sort(distances.begin(), distances.end());
            double last = r;
            double max_found = 0;
            for(int i = 0; i < distances.size(); ++i) {
                assert(distances[i] >= last);
                max_found = max(max_found, distances[i] - last); 
                last = distances[i];
            }
            max_found = max(max_found, R - last);
            max_width = min(max_width, max_found);
        }
        printf("%.3f\n", max_width);
    }
}
