#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <set>
#include <cstring>
#include <vector>
#include <map>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

struct edge {
  int b, c, id;
  edge(int _b, int _c, int _id) {
    b = _b; c = _c; id = _id;
  }
};
vector<edge> edges[100];
bool used[10001];
int N;


void djisktra(int s) {
  long long dist[100];
  bool vis[100];
  memset(vis, 0, sizeof(vis));
  for (int i = 0 ; i < 100; i++) dist[i] = 100000000000ll;
  dist[s] = 0;
  for (int i = 0 ; i < N ; i++) {
    int vi = -1;
    for (int k = 0 ; k < N ; k++) {
      if (!vis[k] && (vi == -1 || dist[vi] > dist[k])) {
        vi = k;
      }
    } 
    // cout << s << " " << vi << endl;
    // for (int i = 0 ; i < N ; i++) cout << dist[i] << " ";
    // cout << endl;
    vis[vi] = true;
    for (int j = 0 ; j < edges[vi].size(); j++) {
      edge edg = edges[vi][j];
      if (dist[edg.b] > dist[vi] + edg.c) {
        dist[edg.b] = dist[vi] + edg.c;
      }
    }
  }
  for (int i = 0 ; i < N ; i++) {
    for (int j = 0 ; j < edges[i].size(); j++) {
      edge ed = edges[i][j];
      if (dist[ed.b] == dist[i] + ed.c) {
        used[ed.id] = true;
      }
    }
  }
}

int main() {
 int kases;
 cin >> kases;
 for (int i = 0 ; i < kases; i++) {
   for (int i = 0 ; i < 100; i ++) edges[i].clear();
   for (int i = 0 ; i < 10001; i ++) used[i] = false;
   cout << "Case #" << i + 1 << ": ";
   cout << endl;
   int M;
   cin >> N >> M;
   for (int i = 0 ; i < M ; i++) {
     int u, v, K;
     cin >> u >> v >> K;
     edges[u].push_back(edge(v, K, i));
     edges[v].push_back(edge(u, K, i));
   }
   for (int i = 0 ; i < N ; i++) djisktra(i);
   for (int i = 0 ; i < M ; i ++) {
     if (!used[i])  cout << i << endl;
   }
 }
 return 0;
}

