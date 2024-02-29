#include <algorithm>
#include <iostream>
#include <locale>
#include <string>
#include <vector>

int main()
{
  auto locale_names = { "ru_RU.UTF8", "en_US.UTF8", "fr_FR.UTF8", "fr_CA.UTF8" };
  // auto strings = std::vector{ u8"coté"s, u8"côte"s, u8"ё"s, u8"и"s, u8"й"s, u8"ґ"s, u8"і"s, u8"ї"s, u8"i"s, u8"я"s };
  auto strings = std::vector{
    std::wstring(L"coté"),
    std::wstring(L"côte"),
    std::wstring(L"ё"),
    std::wstring(L"и"),
    std::wstring(L"й"),
    std::wstring(L"ґ"),
    std::wstring(L"і"),
    std::wstring(L"ї"),
    std::wstring(L"i"),
    std::wstring(L"я")
  };

  std::locale::global(std::locale("en_US.UTF8"));
  std::wcout.imbue(std::locale(""));

  for(auto ln: locale_names)
  {
    std::locale l(ln);
    std::sort(strings.begin(), strings.end(), l);
    for(auto s: strings)
    {
      std::wcout << s << L" ";
    }
    std::wcout << "\n";
  }
  return 0;
}
