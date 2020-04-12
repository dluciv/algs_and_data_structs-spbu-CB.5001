#include <string>
#include <iostream>
#include <typeinfo>

using namespace std::string_literals; // enables s-suffix for std::string literals

template<typename T> T prr(T v)
{
    std::cout << typeid(T).name() << " -<>- " << typeid(v).name() << " {{{" << v << "}}}" << std::endl;
    return v;
}

template<typename T> T vrr(T v)
{
    std::cout << typeid(T).name() << " -<>- " << typeid(v).name() << " {{{ * }}}" << std::endl;
    return v;
}


int main()
{
    // Character literals
    auto c0 = prr(  'A'); // char
    auto c1 = prr(u8'A'); // char
    auto c2 = prr( L'A'); // wchar_t
    auto c3 = prr( u'A'); // char16_t
    auto c4 = prr( U'A'); // char32_t

    // Multicharacter literals
    auto m0 = prr('abcd'); // int, value 0x61626364

    // String literals
    auto s0 = prr(  "hello"); // const char*
    auto s1 = prr(u8"Привет"); // const char*, encoded as UTF-8
    auto s2 = vrr( L"Привет"); // const wchar_t*
    auto s3 = vrr( u"Привет"); // const char16_t*, encoded as UTF-16
    auto s4 = vrr( U"Привет"); // const char32_t*, encoded as UTF-32

    // Raw string literals containing unescaped \ and "
    auto R0 = prr(  R"("Hello \ world")"); // const char*
    auto R1 = prr(u8R"("Hello \ world")"); // const char*, encoded as UTF-8
    auto R2 = vrr( LR"("Hello \ world")"); // const wchar_t*
    auto R3 = vrr( uR"("Hello \ world")"); // const char16_t*, encoded as UTF-16
    auto R4 = vrr( UR"("Hello \ world")"); // const char32_t*, encoded as UTF-32

    // Combining string literals with standard s-suffix
    auto S0 = prr(  "hello"s); // std::string
    auto S1 = prr(u8"hello"s); // std::string
    auto S2 = vrr( L"hello"s); // std::wstring
    auto S3 = vrr( u"hello"s); // std::u16string
    auto S4 = vrr( U"hello"s); // std::u32string

    // Combining raw string literals with standard s-suffix
    auto S5 = prr(  R"("Hello \ world")"s); // std::string from a raw const char*
    auto S6 = prr(u8R"("Hello \ world")"s); // std::string from a raw const char*, encoded as UTF-8
    auto S7 = vrr( LR"("Hello \ world")"s); // std::wstring from a raw const wchar_t*
    auto S8 = vrr( uR"("Hello \ world")"s); // std::u16string from a raw const char16_t*, encoded as UTF-16
    auto S9 = vrr( UR"("Hello \ world")"s); // std::u32string from a raw const char32_t*, encoded as UTF-32

    return 0;
}

// https://onlinegdb.com/Hkg5s4cNU
