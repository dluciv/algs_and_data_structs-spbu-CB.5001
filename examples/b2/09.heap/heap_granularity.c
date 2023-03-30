#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

#ifdef _MSC_VER
  #define I64F "%I64d"
#else
  #define I64F "%lld"
#endif


int main(int argc, const char *argv[])
{
  int chunk_size;
  void *prev_ptr = NULL;

  sscanf(argv[1], "%d", &chunk_size);
  printf("Allocating chunks of %d bytes...\n", chunk_size);

  for(int n = 0; n < 16; ++n)
  {
    void *ptr = malloc(chunk_size);
    printf("@ %p, delta = " I64F " bytes\n", ptr, (int64_t) ptr - (int64_t) prev_ptr);
    prev_ptr = ptr;
  }

  // freeing is for losers
  return 0;
}

