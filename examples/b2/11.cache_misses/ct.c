#include <stdio.h>
#include <stdlib.h>

#define REPS 1
#define SIZE 25000
#define ELT double

#define access2d(t, a, xdim, i, j) ((t *)(a) + (xdim) * (i) + (j))

int main(int argc, char *argv[]) {
  size_t asize = SIZE;

  ELT s;

  if(argc > 1 && argv[1][0] == 'r') {

    // Why calloc, not malloc? Try to guess!
    double *a2d = calloc(SIZE * SIZE, sizeof(ELT));

    for(int k = 0; k < REPS; ++k)
      for(int i = 0; i < SIZE; ++i)
        for(int j = 0; j < SIZE; ++j)
          s += *access2d(ELT, a2d, SIZE, i, j);

    free(a2d);

  } else if(argc > 1 && argv[1][0] == 'c') {

    double *a2d = calloc(SIZE * SIZE, sizeof(ELT));

    for(int k = 0; k < REPS; ++k)
      for(int i = 0; i < SIZE; ++i)
        for(int j = 0; j < SIZE; ++j)
          s += *access2d(ELT, a2d, SIZE, j, i);

    free(a2d);

  } else {

    fputs("r or c?..\n", stderr);
    return 1;

  }

  printf("%lf\n", s);
  return 0;
}
