/*
  Binary search is a search algorithm that finds the position of a target value within a sorted array.
  Binary search compares the target value to the middle element of the array; if they are unequal,
  the half in which the target cannot lie is eliminated and the search continues on the remaining half until it is successful.
  If the search ends with the remaining half being empty, the target is not in the array.
  Binary search runs in at worst logarithmic time, making O(log n) comparisons, where n is the number of elements in the array.
*/

#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

#define N 10
#define M 5000

// end points past the end of the array
bool bs(const int *tab, int start, int end, int toFind)
{
    while (start < end)
    {
        // cout << endl << "S = " << start << " " << end << endl;
        // compare mid element
        int mid = start + (end - start) / 2;

        // == return true
        if (tab[mid] == toFind)
            return true;

        // jump to first half
        else if (tab[mid] > toFind)
            end = mid;

        // jump to second half
        else
            start = mid + 1;
    }

    return false;
}

int main()
{
    srand(time(NULL));
    int *tab = new int[N];

    for (int i = 0; i < N; ++i)
    {
        tab[i] = rand() % M;
    }

    for (int i = 0; i < N; ++i)
    {
        cout << tab[i] << " ";
    }

    cout << bs(tab, 0, N, tab[2]) << endl;
    cout << bs(tab, 0, N, tab[0]) << endl;
    cout << bs(tab, 0, N, tab[N - 1]) << endl;
    cout << bs(tab, 0, N, tab[N / 2]) << endl;
    cout << bs(tab, 0, N, -1) << endl;

    delete[] tab;
}
