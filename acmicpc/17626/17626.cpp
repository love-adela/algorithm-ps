#include <cstdio>
#include <cmath>
using namespace std;

int get_min(int a, int b) { return a < b ? a : b;}

int main() {
  int n, i, j;
  scanf("%d", &n);

  int len = sqrt(n)+1;
  int arr[len];
  int dp[n+1];

  for (i = 1; i < len; i++) arr[i] = i*i;
  for (i = 1; i <= n; i++) dp[i] = __INT_MAX__;
  dp[0] = 0;

  for (i=1; i<len; i++) {
    for (j=arr[i]; j<=n; j++) dp[j] = get_min(dp[j - arr[i]] + 1, dp[j]);
  }
  printf("%d\n", dp[n]);

  return 0;
}
