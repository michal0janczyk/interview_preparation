#include <iostream>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;

void printTab(int **tab, int h, int w)
{
    for (int i = 0; i < h; ++i)
    {
        for (int j = 0; j < w; ++j)
        {
            cout << tab[i][j] << " ";
        }
        cout << endl;
    }
}

int **expand(int **tab, int h, int w, int H, int W)
{
    tab = (int **)realloc(tab, H * sizeof(int *));

    for (int i = 0; i < h; ++i)
    {
        tab[i] = (int *)realloc(tab[i], W * sizeof(int));
    }

    for (int i = h; i < H; ++i)
    {
        tab[i] = (int *)malloc(W * sizeof(int));
    }

    for (int i = 0; i < h; ++i)
    {
        for (int j = w; j < W; ++j)
        {
            tab[i][j] = rand() % 10;
        }
    }

    for (int i = h; i < H; ++i)
    {
        for (int j = 0; j < W; ++j)
        {
            tab[i][j] = rand() % 10;
        }
    }

    return tab;
}

int main()
{
    srand(time(NULL));
    const int h = 5, w = 10;

    int **tab = (int **)malloc(h * sizeof(int *));
    assert(tab != NULL);

    for (int i = 0; i < h; ++i)
    {
        tab[i] = (int *)malloc(w * sizeof(int));
        assert(tab[i] != NULL);
    }

    for (int i = 0; i < h; ++i)
    {
        for (int j = 0; j < w; ++j)
        {
            tab[i][j] = rand() % 10;
        }
    }

    printTab(tab, h, w);
}
