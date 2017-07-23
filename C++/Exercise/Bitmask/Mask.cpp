#include <cassert>
#include <iostream>

using namespace std;

int calcOnes(unsigned x)
{
    unsigned mask = 0x1;
    int nOnes = 0;

    while (mask != 0)
    {
        if ((x & mask) != 0)
        {
            nOnes += 1;
        }

        mask <<= 1;
    }

    return nOnes;
}

void printIP(unsigned ip)
{
    unsigned d = ip;
    d <<= 24;
    d >>= 24;

    cout << d << endl;

    unsigned c = ip;
    c <<= 16;
    c >>= 24;

    cout << c << endl;

    // TODO: przesuwanie

}

int main()
{
    // unsigned x = 0xA; // = 10
    // unsigned x1 = 0x1;
    // unsigned x2 = 0x3;

    // unsigned res = x1 | x2;
    // unsigned res = x1 & x2;

    unsigned x3 = 0x5;
    
    // x3 = x3 << 2;
    x3 <<= 3;
    x3 >>= 2;

    cout << ~x3 << endl;

    unsigned x = 16;
    cout << calcOnes(x) << endl;

    unsigned ip = 3482223596;
    printIP(ip);
}
