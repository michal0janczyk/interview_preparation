#include <cassert>
#include <iostream>
#include <cstring>
#include <vector>
#include <string>

using namespace std;

char *wordsToTab(const vector<string> &words)
{
    char *tab = nullptr;

    // Policzyc laczny rozmiar.
    int size = 0;

    for (const string &e : words)
    {
        size += e.size() + 1;
    }

    size += 1;
    cout << "Size = " << size << endl;

    // Zaalokowac pamiec.
    tab = new char[size];
    assert (tab != nullptr);

    int cur = 0;

    // Iterujemy po kazdym slowie i kopiujemy do tablicy.
    for (const string &e : words)
    {
        tab[cur] = (char) e.size();

        for (int i = 0; i < (int) e.size(); ++i)
        {
            tab[cur + 1 + i] = e[i];
        }

        cur += e.size() + 1;
    }

    tab[size - 1] = (char) 0;
    return tab;
}

// Przerobic tak, zeby wykorzystywac jedynie realloc.
char *wordsToTabAlt(const vector<string> &words)
{
      // int size = words[0].size() + 1;
      // char *tab = malloc(size);

      int size = 0;
      char *tab = nullptr;

      //tab[0] = (char) words[0].size();
      //memcpy(tab + 1, words[0].c_str(), words[0].size());

      char *cur = tab;

      for (size_t i = 1; i < words.size(); ++i)
      {
          size += (words[i].size() + 1);
          cur += words[i - 1].size() + 1;

          tab = (char *)realloc(tab, size);
          assert(tab != nullptr);

          cur[0] = (char) words[i].size();
          memcpy(cur + 1, words[i].c_str(), words[i].size());
      }

      tab[size - 1] = (char) 0;
      return tab;
}

// Nie mozna stworzyc wzorca dla T<>, czyli nie mozemy zamienic wektora na typename.
template<typename T>
void print(const vector<T> &words)
{
    for (const T &e : words)
    {
        cout << e << endl;
    }
}

void print(char const *tab)
{
    assert (tab != nullptr);

    while (true)
    {
        char size = *tab; // cur[0]
        // char size = (char) tab[cur];

        if (size == 0)
            break;

        tab += 1;

        for (int i = 0; i < size; ++i)
        {
            cout << *tab;
            tab += 1;
        }

        cout << endl;
    }
}

int main()
{
    vector<string> words { "ala", "ma", "kota", "jarek", "tusk" };
    print(words);

    char *tab = wordsToTab(words);
    print(tab);
}
