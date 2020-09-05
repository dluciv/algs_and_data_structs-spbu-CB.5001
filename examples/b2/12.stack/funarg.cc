#include <iostream>
#include <functional>
#include <chrono>
#include <memory>

using namespace std;

typedef chrono::duration<double, std::micro> usec;

long bench(string note, function<long(long)> testee)
{
    auto iterations = 10000000;
    long acc = 0L;

    auto s = std::chrono::high_resolution_clock::now();
    for(auto i = 0; i < iterations; i++)
        acc = testee(acc);
    auto f = std::chrono::high_resolution_clock::now();

    cout << "Running: " << note << " took " <<
        chrono::duration_cast<chrono::microseconds>(f - s).count() / (double)iterations <<
        "[μs]" << endl;

    return acc;
}


function<long(long)> uparg = [](long n){ return n; };

long slowest(long v)
{
        auto pz = make_shared<long>(v + 1);
        auto f = [=](long x) // [=] -- copy all used vars, including pz
        {
                (*pz) += x; // z is used when f is called and modified
                return *pz;
        };
        uparg = f; // requires writable instance of z
        return f(v);
}

long slower(long v)
{
        auto z = v + 1;
        auto f = [=](long x) // [=] -- copy all used vars, including pz
        {
                return x + z; // z is used when f is created
        };
        uparg = f; // requires copy of z
        return f(v);
}

long fast(long v)
{
        auto z = v + 1;
        auto f = [&](long x) { // [&] -- reference all used vars
                return x + z;
        };
        uparg = fast; // just to take time
        return f(v);
}

int main() {
        bench("fast", fast);
        cout << "not benchamrking fast / inner" << endl;

        bench("slower", slower);
        bench("slower / inner", uparg);

        bench("slowest", slowest);
        bench("slowest / inner", uparg);
        return 0;
}
