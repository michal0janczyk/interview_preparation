#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

void printTab(int tab[5][3])
{
    for (int iH = 0; iH < 5; ++iH)
    {
        for (int iW = 0; iW < 3; ++iW)
        {
            cout << tab[iH][iW] << " ";
        }

        cout << endl;
    }
}

int main()
{
    const int h = 5, w = 3;
    int tab1[h][w], tab2[h][w];

    srand(time(NULL));

    for (int iH = 0; iH < h; ++iH)
    {
        for (int iW = 0; iW < w; ++iW)
        {
            tab1[iH][iW] = rand() % 101;
            tab2[iH][iW] = rand() % 101;
        }
    }

    printTab(tab1);
    cout << endl;
    printTab(tab2);
    cout << endl;

    int res[h][w];
    for (int iH = 0; iH < h; ++iH)
    {
        for (int iW = 0; iW < w; ++iW)
        {
            res[iH][iW] = tab1[iH][iW] + tab2[iH][iW];
        }
    }

    printTab(res);

    cin.get();
    return 0;
}

