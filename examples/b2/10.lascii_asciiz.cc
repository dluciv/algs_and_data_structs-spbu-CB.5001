#include <string>
#include <cstring>
#include <iostream>

using namespace std::string_literals; // enables s-suffix for std::string literals

int main()
{
    const char *cs = "hel\0lo";
    std::string cpps = "hel\0lo"s;

    std::cout << '[' << cs   << ']' << strlen(cs) << std::endl;
    std::cout << '[' << cpps << ']' << cpps.size() << std::endl;
    return 0;
}
