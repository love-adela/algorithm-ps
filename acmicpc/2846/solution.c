#include <stdio.h>

int main() {
  int N;
  int heights[1001] = {};

  scanf("%d", &N);
  for (int i = 0; i < N; ++i) {
    scanf("%d", &heights[i]);
  }

  int local_min = heights[0];
  int maximum = 0;
  for (int i= 0; i < N; ++i) {
    if (heights[i+1]<=heights[i]) {
      int current = heights[i] - local_min;
      if (current > maximum) {
        maximum = current;
      }
      local_min = heights[i+1];
    }
  }
  printf("%d\n", maximum);
}
