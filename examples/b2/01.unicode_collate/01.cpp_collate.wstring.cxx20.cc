#include <algorithm>
#include <iostream>
#include <locale>
#include <string>
#include <vector>
#include <codecvt>

using namespace std::string_literals; // enables s-suffix for std::string literals

int main()
{
  auto locale_names = { "ru_RU.UTF8", "en_US.UTF8", "fr_FR.UTF8", "fr_CA.UTF8" };
  auto strings = std::vector{
    L"coté"s,
    L"côte"s,
    L"а"s,
    L"\"а\""s,
    L"ё"s,
    L"и"s,
    L"й"s,
    L"ґ"s,
    L"і"s,
    L"ї"s,
    L"i"s,
    L"ю"s,
    L"\"ю\""s,
    L"я"s
  };

  std::locale::global(std::locale(""));
  std::wcout.imbue(std::locale(""));

  for(auto ln: locale_names)
  {
    std::locale l(ln);
    std::sort(strings.begin(), strings.end(), l);

    std::wcout << std::wstring_convert<std::codecvt_utf8_utf16<wchar_t>>().from_bytes(ln) << L'\t';

    for(auto s: strings)
    {
      std::wcout << s << L" ";
    }
    std::wcout << L"\n";
  }
  return 0;
}
