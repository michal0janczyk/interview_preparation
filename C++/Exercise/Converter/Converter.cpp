#include <iostream>
#include <string>

struct romanType {const int value; const char *literal;};
static romanType const romanData[] = { 1000, "M", 900, "CM", 500, "D", 400, "CD", 100, "C", 90, "XC", 50, "L", 40, "XL", 10, "X", 9, "IX", 5, "V", 4, "IV", 1, "I", 0, NULL };

map<string, int> romanToDec; // "V" -> 5
map<int, string> decToRoman;// 5 -> "V"

std::string convertToRoman(const int &value)
{
    std::string result;

    for (romanType const* curr = romanData; curr->value > 0; ++curr)
    {
        while (value > curr->value)
        {
            result += curr->literal;
            value -= curr->value;
        }
    }

    return result;
}

std::string convertToDecimal(const std::sring &string)
{
    int result, lastDigit = 0;
    for(romanType const *curr = romanData; curr->literal; ++curr)
    {
        if(value > lastDigit)
        {
            result += value;
            lastDigit = value;
        } else {
            result -= value;
        }
    }
    return result;
}

int romanToDecimal(string number)
{
    int value = 0;

    for (int i = 0; i < number.size(); ++i)
    {
        if (map[number[i]] >= map[number[i + 1]])
        {
            value += map[number[i]];
        }
        else
        {
            value -= map[number[i]];
        }
    }

    return value;
}

// Assume value is set 0.
void romanToDecimal(string number, int *value)
{
    for (int i = 0; i < number.size(); ++i)
    {
        (map[number[i]] >= map[number[i + 1]] or i == number.size() - 1) ? value += map[number[i]] : value -= map[number[i]];
    }
}

int main()
{
    // int value = 0;
    int value = new int(); // set to 0
    romanToDecimal("M", &value);

    // std::string cTR = convertToRoman(100);
    // std::cout << cTR << std::endl;

    std::string cTD = convertToDecimal("MD");
    std::cout << cTD << std::endl;
}

void debug(const string &msg)
{
#if DEBUG
    cout << msg << endl;
#endif
}
