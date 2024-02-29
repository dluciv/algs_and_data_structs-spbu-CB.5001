#include <string>
#include <iostream>
#include <typeinfo>
#include <locale>

using namespace std::string_literals; // enables s-suffix for std::string literals

template<typename CT> std::u8string str2utf8(const std::basic_string<CT> &in_s)
{
    if(!std::has_facet<std::codecvt<CT, char8_t, std::mbstate_t>>(std::locale()))
    {
        std::cerr << "No facet for " << typeid(CT).name() << " -> char8_t and locale " << std::locale().name() << std::endl;
        return u8"?"s;
    }

    auto& f = std::use_facet<std::codecvt<CT, char8_t, std::mbstate_t>>(std::locale());
    std::mbstate_t mb = std::mbstate_t();
    std::u8string out_s(in_s.size() * f.max_length(), '\0');

    const CT *from_next;
    char8_t  *to_next;

    f.out(mb,
        &in_s[0], &in_s[in_s.size()], from_next,
        &out_s[0], &out_s[out_s.size()], to_next
    );

    out_s.resize(to_next - &out_s[0]);
    return out_s;
}

template<typename CT> std::string st2cst(const std::basic_string<CT> &ssref)
{
    return st2cst(str2utf8(ssref));
}

template<typename C> std::string st2cst(const C *cstr)
{
    return st2cst(std::basic_string<C>(cstr));
}

template<typename T> std::string st2cst(T ssref)
{
    return "@"s;
}

template<> std::string st2cst(const std::string &ssref)
{
    return ssref;
}

// Assume std::cout eats UTF-8
template<> std::string st2cst(const std::u8string &ssref)
{
    return std::string(*reinterpret_cast<const std::string *>(&ssref));
}

template<typename T> T prr(int stage, T v)
{
    std::string sv(st2cst(v));

    std::cout << stage << '\t' << typeid(T).name() << " -<>- " << typeid(v).name() << " -<>- " << typeid(sv).name() << " {{{";
    std::cout << sv;
    std::cout << "}}}" << std::endl;
    return v;
}

int main()
{
    // Multicharacter literals
    auto m0 = prr(0, 'abcd'); // int, value 0x61626364

    /*
    // Character literals
    auto c0 = prr(1,   'A'); // char
    auto c1 = prr(1, u8'A'); // char
    auto c2 = prr(1,  L'A'); // wchar_t
    auto c3 = prr(1,  u'A'); // char16_t
    auto c4 = prr(1,  U'A'); // char32_t
    */

    // String literals
    auto s0 = prr(2,   "hello"); // const char*
    auto s1 = prr(2, u8"Привет"); // const char*, encoded as UTF-8
    auto s2 = prr(2,  L"Привет"); // const wchar_t*
    auto s3 = prr(2,  u"Привет"); // const char16_t*, encoded as UTF-16
    auto s4 = prr(2,  U"Привет"); // const char32_t*, encoded as UTF-32

    // Raw string literals containing unescaped \ and "
    auto R0 = prr(3,   R"("Hello \ world")"); // const char*
    auto R1 = prr(3, u8R"("Hello \ world")"); // const char*, encoded as UTF-8
    auto R2 = prr(3,  LR"("Hello \ world")"); // const wchar_t*
    auto R3 = prr(3,  uR"("Hello \ world")"); // const char16_t*, encoded as UTF-16
    auto R4 = prr(3,  UR"("Hello \ world")"); // const char32_t*, encoded as UTF-32

    // Combining string literals with standard s-suffix
    auto S0 = prr(4,   "hello"s); // std::string
    auto S1 = prr(4, u8"hello"s); // std::string
    auto S2 = prr(4,  L"hello"s); // std::wstring
    auto S3 = prr(4,  u"hello"s); // std::u16string
    auto S4 = prr(4,  U"hello"s); // std::u32string

    // Combining raw string literals with standard s-suffix
    auto S5 = prr(5,   R"("Hello \ world")"s); // std::string from a raw const char*
    auto S6 = prr(5, u8R"("Hello \ world")"s); // std::string from a raw const char*, encoded as UTF-8
    auto S7 = prr(5,  LR"("Hello \ world")"s); // std::wstring from a raw const wchar_t*
    auto S8 = prr(5,  uR"("Hello \ world")"s); // std::u16string from a raw const char16_t*, encoded as UTF-16
    auto S9 = prr(5,  UR"("Hello \ world")"s); // std::u32string from a raw const char32_t*, encoded as UTF-32

    return 0;
}
