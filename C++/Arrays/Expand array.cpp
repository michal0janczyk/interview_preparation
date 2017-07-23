#include <cstdlib>
#include <iostream>

using namespace std;

const char sep = '*';

void print(char **tab, int n)
{
    for (int i = 0; i < n; ++i)
    {
        cout << tab[i] << endl;
    }
}

int main()
{
    const char *s = "Ala*Jolanta*Marek*Adam*Jowita";

    char **tab = NULL;
    int nStrings = 0;
    
    int i = 0;
    int prev = 0;

    while (s[i] != '\0')
    {
        // Znaleźliśmy nowy string.
        if (s[i] == sep)
        {
            // Alokujemy pamięć na nowy string.
            int size = i - prev + 1;
            char *newStr = (char *)malloc(size * sizeof(char)); // zmienna pomocnicza (tmp)

            // Kopiujemy znaki.
            for ( int j = 0; j < size; ++j)
            {
                newStr[j] = s[prev + j];
            }

            newStr[size -1] = '\0';
            prev = i + 1;

            // Wpisujemy wskaźnik do tablicy wskaźników.
            nStrings += 1;

            // Rozszerzamy tablicę (pomijamy sprawdzanie błędów -- realloc zwraca NULL).
            tab = (char **)realloc(tab, nStrings * sizeof(char *));
            tab[nStrings -1] = newStr;
        }

        i += 1;
    }

    print(tab, nStrings);
}
