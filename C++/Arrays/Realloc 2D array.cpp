#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

int **init(int **tab, int oldH, int oldW, int h, int w)
{
    tab = realloc(tab, h * sizeof(int *));

    for (int i = 0; i < h; ++i)
    {
        tab[i] = realloc(tab[i], w * sizeof(int));
    }

    for (int i = oldH; i < h; ++i)
    {
        for (int j = 0; j < w; ++j)
        {
            tab[i][j] = rand() % 10;
        }
    }
}

void printTab(int **tab, int h, int w)
{
    for (int i = 0; i < h; ++i)
    {
        for (int j = 0; j < w; ++j)
        {
            cout << tab[i][j] << " ";
        }
    }
    cout << endl;
}

int main()
{
    const int h = 5, w = 10;
    srand(time(NULL));

    // Tworzymy tablicę 2D i wypełniamy liczbami.
    int **tab = (int **) malloc(h * sizeof(int *));

    for (int i = 0; i < h; ++i)
    {
        tab[i] = (int *) malloc(w * sizeof(int));
    }

    for (int i = 0; i < h; ++i)
    {
        for (int j = 0; j < w; ++j)
        {
            tab[i][j] = rand() % 10; // [0, 9]
        }
    }

    printTab(tab, h, w);

    int **newTab = init(tab, h, w, h + 10, w + 10);
    printTab(newTab, h + 10, w + 10);
}
