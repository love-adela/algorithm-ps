#include <iostream>
using namespace std;
int main()
{
  int testcase, m, n, sum, cnt, i ,j;
  int arr[101][101] = { 0 };
  cin >> testcase;
  while (testcase--){
    cin >> m >> n;
    sum = 0;
    for (i = 1; i <= m; i++)
      for (j = 1; j <= n; j++)
        cin >> arr[i][j];
	for (j = 1; j <= n; j++){
	    for (i = m; i >= 1; i--){
	      cnt = 0;
	      if (arr[i][j] == 1){
	        for (int k = i + 1; k <= m; k++){
		  if (arr[k][j] == 1) 
		    break; 
		  else
		    cnt++;}
		sum += cnt;
		swap(arr[i + cnt][j], arr[i][j]);}}}
		cout << sum << '\n';
	}
	
	return 0;
}
