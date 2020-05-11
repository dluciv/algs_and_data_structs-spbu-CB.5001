#include <iostream>
#include <functional>
#include <chrono>
#include <random>
#include <unordered_map>

using namespace std;

const size_t pieces = 100000;
const size_t max_piece_size = 8192;
const size_t std_piece_size = max_piece_size / 2;

std::default_random_engine generator;
std::uniform_int_distribution<size_t> piece_idx_distribution(0, pieces - 1);
std::uniform_int_distribution<size_t> piece_size_distribution(1, max_piece_size);
auto piece_dice = std::bind(piece_idx_distribution, generator);
auto size_dice = std::bind(piece_size_distribution, generator);

typedef chrono::duration<double, std::micro> usec;

void benchmark(function<usec()> fn, string note)
{
    auto d = fn();
    cout << "Running: " << note << " took " <<
        chrono::duration_cast<chrono::microseconds>(d).count() <<
        "[μs]" << endl;
}

char *hptr[pieces];

void setup(bool random_size)
{
    for(int i = 0; i < pieces; ++i)
        hptr[i] = new char[random_size ? size_dice() : std_piece_size];

}

usec perform(bool random_size)
{
    const size_t mod_size = 1000, iterations = 10000;
    auto total = usec();
    auto mod = unordered_map<size_t, size_t>();
    for(int r = 0; r < iterations; ++r)
    {
        mod.clear();

        for(int j = 0; j < mod_size; ++j)
            mod[piece_dice()] = random_size? size_dice() : std_piece_size;

        auto t1 = std::chrono::high_resolution_clock::now();

        // free some allocations
        for(const auto& [i,s]: mod)
            delete hptr[i];
        // feel those allocations
        for(const auto& [i,s]: mod)
            hptr[i] = new char[s];

        auto t3 = std::chrono::high_resolution_clock::now();

        total += t3 - t1;
    }
    // cout << chrono::duration_cast<chrono::microseconds>(total).count() << endl;
    return total;
}

void teardown()
{
    for(auto p: hptr)
        delete p;
}

int main()
{
    setup(false);
    benchmark([](){return perform(false);}, "Similar size");
    teardown();

    setup(true);
    benchmark([](){return perform(true); }, "Random size");
    teardown();

    return 0;
}
