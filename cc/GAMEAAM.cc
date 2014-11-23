#include<iostream>
#include <cstdio>

using namespace std;

int get_grundy(int a, int b) {
    if (a > b) {
        int t = a;
        a = b;
        b = t;
    }
    if (b%a == 0) return b/a - 1;
    // b = a * k + r
    int t = get_grundy(a, b % a);
    if (t == 0) {
        return b/a;
    }
    // b = a + r is losing and is 0.
    // b = 2 * a + r is winning and is 1
    // b = 3 * a + r is winning and is 3
    int x = b /a ;
    if (x > t) return x;
    return x - 1;
}
int main() {
    int T;
    scanf("%d", &T);
    while(T--) {
        int N;
        int g = 0;
        scanf("%d", &N);
        while (N--) {
            int a, b;
            scanf("%d%d", &a, &b);
            g ^= get_grundy(a, b);
        }
        printf("%s\n", g ? "YES" : "NO"); 
    }
}
