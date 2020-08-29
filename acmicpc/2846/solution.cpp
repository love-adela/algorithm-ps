#include <iostream>
using namespace std;

int main(void) {
  int n;
  cin >> n;

  int heights[1001] = {};
  for (int i = 0; i < n; ++i) {
    cin >> heights[i];
  }

  int local_min = heights[0];
  int maximum = 0;
  for (int i = 0; i < n; ++i) {
    if (heights[i+1]<=heights[i]) {
      int current = heights[i] - local_min;
      if (current > maximum) {
        maximum = current;
        }
      local_min = heights[i+1];
      }
    }
    cout << maximum;
    return 0;
  }


