#include "stdafx.h"
#include <algorithm>
#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

#define N 10
#define M 10

void printTab(int *tab)
{
    for (int i = 0; i < N; ++i)
    {
        cout << tab[i] << " ";
    }
    cout << endl;
}

int **outputSignal(int *tabX, int *tabW)
{
    int *tabRes = new int[N];

    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            tabRes[i * N + j] = 0; 
            for (int k = 0; k < N; ++k)
            {
                tabRes[i * N + j] += tabX[i * N + k] * tabW[k * N + j];
            }
        }
    }

    return &tabRes;
}

int main()
{
    srand(time(NULL));

    int *tabX = new int[N];

    for (int i = 0; i < N; ++i)
    {
        tabX[i] = rand() % M;
    }

    int *tabW = new int[N];

    for (int j = 0; j < N; ++j)
    {
        tabW[j] = rand() % M;
    }

    cout << "Wektor sygnalow wejsciowych : " << endl;
    printTab(tabX);

    cout << endl;

    cout << "Wektor wag : " << endl;
    printTab(tabW);

    cout << endl;

    int **tabRes = outputSignal(tabX, tabW);
    
    cout << "Sygnal wyjsciowy : " << endl;
    printTab(*tabRes);

    delete[] tabX;
    delete[] tabW;

    cin.get();
    return 0;
}