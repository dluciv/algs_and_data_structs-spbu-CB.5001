#include <iostream>
#include <unordered_map>
#include <functional>
#include <chrono>

using namespace std;

typedef chrono::duration<double, std::micro> usec;

void benchmark(function<void()> fn)
{
  auto s = std::chrono::high_resolution_clock::now();
  fn();
  auto f = std::chrono::high_resolution_clock::now();

  cout << "Took " <<
    chrono::duration_cast<chrono::microseconds>(usec() + f - s).count() << "[μs]" << endl;
}

template<typename R, typename A, R F(A)>
R cached(A a)
{
  static unordered_map<A, R> cache; // infinite =)
  auto f = cache.find(a);
  if(f == cache.end())
  {
    R r = F(a);
    cache[a] = r;
    return r;
  }
  else
    return f->second;
}

bool is_simple(int n)
{
  if(n % 2 == 0 || n % 3 == 0 || n % 5 == 0 || n % 7 == 0)
    return false;
  int i = 11, i_2 = 121;
  while(i_2 <= n)
  {
    if(n % i == 0)
      return false;

    i_2 += 2 * i + 1;
    i += 1;
  }
  return true;
}

int main()
{
  int ts;
  for(auto k = 0; k < 2; ++k)
  {
    benchmark([&](){
      ts = 0;
      for(int i = 3; i < 1000000; ++i)
        if(cached<bool, int, is_simple>(i))
          ts ++;
    });
  }
  return 0;
}
