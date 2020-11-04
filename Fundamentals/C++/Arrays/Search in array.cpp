#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
    int t[] = {1, 5, 2, 3, 0};
    int szukana;
    bool found = false; // bool -> true, false (Boolean)

    cout << "Wpisz szukana liczbe: " << endl;
    cin >> szukana;

    for (int i = 0; i < 5; i = i + 1)
    {
        if (t[i] == szukana)
        {
            cout << "Liczba " << szukana << " jest tabeli" << endl;
            found = true;
        }
    }

    if (found == false)
    {
        cout << "Liczby " << szukana << " nie ma w tabeli" << endl;
    }

    return 0;
}
