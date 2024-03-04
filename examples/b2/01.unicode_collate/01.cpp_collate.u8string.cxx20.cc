#include <algorithm>
#include <iostream>
#include <locale>
#include <string>
#include <vector>

using namespace std::string_literals; // суффикс s для литералов std::string

int main()
{
  auto locale_names = { "ru_RU.UTF8", "en_US.UTF8", "fr_FR.UTF8", "fr_CA.UTF8" };
  auto strings = std::vector{
    u8"coté"s,
    u8"côte"s,
    u8"а"s,
    u8"\"а\""s,
    u8"ё"s,
    u8"и"s,
    u8"й"s,
    u8"ґ"s,
    u8"і"s,
    u8"ї"s,
    u8"i"s,
    u8"ю"s,
    u8"\"ю\""s,
    u8"я"s
  };

  for(auto ln: locale_names)
  {
    std::locale l(ln);

    // Так делать точно нехорошо, но поскольку во всех более-менее вменяемых
    // Юниксах std::string структурно эквивалентен std::u8string, работать это будет
    auto plain_strings = reinterpret_cast<std::vector<std::string> &>(strings);

    std::sort(plain_strings.begin(), plain_strings.end(), l);

    std::cout << ln << '\t';
    for(auto s: plain_strings)
    {
      std::cout << s << ' ';
    }
    std::cout << std::endl;
  }
  return 0;
}
