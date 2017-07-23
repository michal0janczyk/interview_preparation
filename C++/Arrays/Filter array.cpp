#include <iostream>
#include <cstdio>

using namespace std;

void filter(int tab[], int n)
{
    // count - liczba niewypisanych elementów
    int count = 0, lastElement = -1;
    int j = 0;

    for (int i = 0; i < n; i++)
    {
        if (tab[i] == lastElement)
        {
            count += 1;
        }
        else // szczególny przypadek lE == -1 jest tutaj zawarty
        {
            tab[j] = tab[i];

            lastElement = tab[i];
            j += 1; // j = j + 1, j++, ++j -- to samo
        }
    }

    for (int i = 0; i < count; ++i)
    {
        tab[j + i] = 0;
    }
}

int main()
{
    const int n = 10;
    int tab[n] = { 1, 1, 1, 2, 4, 5, 5, 6, 6, 7 };
    int dup[n];

    cout << "Tablica przed usuwaniem elementow: " << endl;

    for (int i = 0; i < n; i++)
    {
        cout << tab[i] << " ";
    }

    filter(tab, n);

    cout << endl << "Tablica po usunieciu elemntow: " << endl;

    for (int i = 0; i < n; i++)
    {
        cout << tab[i] << " ";
    }

    cin.get();
    return 0;
}
