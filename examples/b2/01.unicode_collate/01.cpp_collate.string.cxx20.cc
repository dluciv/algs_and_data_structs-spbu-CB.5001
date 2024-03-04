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
    "coté"s,
    "côte"s,
    "а"s,
    "\"а\""s,
    "ё"s,
    "и"s,
    "й"s,
    "ґ"s,
    "і"s,
    "ї"s,
    "i"s,
    "ю"s,
    "\"ю\""s,
    "я"s
  };

  for(auto ln: locale_names)
  {
    std::locale l(ln);

    std::sort(strings.begin(), strings.end(), l);

    std::cout << ln << '\t';
    for(auto s: strings)
    {
      std::cout << s << ' ';
    }
    std::cout << std::endl;
  }
  return 0;
}
