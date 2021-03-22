#include <iostream>
#include <gmpxx.h>
#include <time.h>

using namespace std;

// https://gmplib.org/manual/
// https://jasonstitt.com/c-extension-n-choose-k

void sum_n(const mpz_class about) {
    mpz_class res = about;
    for(int z = 0; z < 1000000; z++)
    {
        res += about;
        res --;
        res -= about;
        res *= 2;
        res += 2;
        res /= 2;
    }
}

void measure_v(const mpz_class v)
{
    clock_t c1, c2;
    c1 = clock();
    for(int n = 0; n < 10; n++)
        sum_n(v);
    c2 = clock();
    cout << (double)(c2 - c1) / CLOCKS_PER_SEC << endl;
}

int main(void)
{
  mpz_class v = 1;

  for(int i = 0; i < 40; i++)
  {
      v *= 65536;
      gmp_printf ("%ZX\t", v.get_mpz_t());
      measure_v(v);
  }

  return 0;
}
