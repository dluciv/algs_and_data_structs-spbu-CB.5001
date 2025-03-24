#include <stdio.h>

#define REPS 1
#define SIZE 10000

volatile double a[SIZE][SIZE];

int main(int argc, char *argv[]) {
  double s;
  if(argc > 1 && argv[1][0] == 'r') {
    for(int k = 0; k < REPS; ++k)
      for(int i = 0; i < SIZE; ++i)
        for(int j = 0; j < SIZE; ++j)
          s += a[i][j];
  } else if(argc > 1 && argv[1][0] == 'c') {
    for(int k = 0; k < REPS; ++k)
      for(int i = 0; i < SIZE; ++i)
        for(int j = 0; j < SIZE; ++j)
          s += a[j][i];
  } else {
    puts("r or c?");
  }
  printf("%lf\n", s);
  return 0;
}