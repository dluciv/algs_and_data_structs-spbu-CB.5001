#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  int size;
  scanf("%d", &size);
  for(int i = 0; i < 16; ++i)
  {
    void *p = malloc(size);
    // free(p);
    printf("%p\n", p);
  }
  return 0;
}
