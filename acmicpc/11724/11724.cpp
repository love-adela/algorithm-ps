#include <cstdio>
#include <vector>
using namespace std;
vector<int> neighbor[1001];
bool visited[1001];
void dfs(int node) {
  visited[node] = true;
  for (int i=0; i<neighbor[node].size(); i++){
    int next = neighbor[node][i];
    if (visited[next] == false) {
      dfs(next);
    }
  }
}

int main() {
  int n, m;
  scanf("%d %d", &n, &m);
  for (int i=0; i<m; i++) {
    int u, v;
    scanf("%d %d", &u, &v);
    neighbor[u].push_back(v);
    neighbor[v].push_back(u);
  }
  int components = 0;
  for (int i=1; i<=n; i++) {
    if (visited[i] == false) {
      dfs(i);
      components += 1;
    }
  }
  printf("%d\n", components);
  return 0;
}


