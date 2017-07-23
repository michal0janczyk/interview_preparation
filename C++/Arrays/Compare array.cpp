#include <ctime> // time(NULL)
#include <iostream>
#include <cstdlib> // srand, rand

using namespace std;

int main()
{
    const int n = 5;

    // int t1[n];
    // int t2[n];
    int *t1 = new int[n];
    int *t2 = new int[n];

    srand(time(NULL)); // wynik z time(NULL) jako argument do srand

    for (int i = 0; i < n; i++)
    {
        int cur1 = rand();
        t1[i] = cur1 % 101;

        int cur2 = rand();
        t2[i] = cur2 % 101;
    }

    for (int i = 0; i < n; i++)
    {
        cout << t1[i] << " ";
    }
    cout << endl;

    for (int i = 0; i < n; i++)
    {
        cout << t2[i] << " ";
    }
    cout << endl;

    bool in;

    for (int i=0; i<5; i++)
    {
        in = false;

        for (int j=0; j<5; j++)
        {
            if (t1[i] == t2[j])
            {
                cout << "Tablica 2 zawiera liczbe: " << t1[i] << endl;
                in = true;
                break;
            }
        }

        if (in == false)
        {
            cout << "Tablica 2 nie zawiera liczby: " << t1[i] << endl;
        }
    }
    delete [] t1;
    delete [] t2;

    return 0;
}
