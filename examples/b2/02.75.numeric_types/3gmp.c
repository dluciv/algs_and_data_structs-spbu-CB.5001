#include <stdio.h>
#include <gmp.h>
#include <time.h>

// https://gmplib.org/manual/
// https://jasonstitt.com/c-extension-n-choose-k

void sum_n(mpz_t about) {
    mpz_t res;
    mpz_init_set(res, about);
    for(int z = 0; z < 1000000; z++)
    {
        mpz_add(res, res, about);  // res += about
        mpz_sub_ui(res, res, 1);   // res --;
        mpz_sub(res, res, about);  // res -= about;
        mpz_mul_ui(res, res, 2);   // res *= 2;
        mpz_add_ui(res, res, 2);   // res += 2n;
        mpz_div_ui(res, res, 2);   // res /= 2n;
    }
    // return res;
}

void measure_v(mpz_t v)
{
    clock_t c1, c2;
    c1 = clock();
    for(int n = 0; n < 10; n++)
        sum_n(v);
    c2 = clock();
    printf("%f\n", (double)(c2 - c1) / CLOCKS_PER_SEC);
}

int main(void)
{
  mpz_t v;
  mpz_init_set_ui(v, 1);

  for(int i = 0; i < 40; i++)
  {
      mpz_mul_ui(v, v, 65536);
      gmp_printf ("%ZX\t", v);
      measure_v(v);
  }

  return 0;
}
