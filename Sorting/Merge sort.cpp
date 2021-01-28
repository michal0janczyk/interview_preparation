/*
  Conceptually, a merge sort works as follows:
  Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted).
  Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.
  In sorting n objects, merge sort has an average and worst-case performance of O(n log n).
  If the running time of merge sort for a list of length n is T(n), then the recurrence T(n) = 2T(n/2) + n follows from the definition of the
  algorithm (apply the algorithm to two lists of half the size of the original list, and add the n steps taken to merge the resulting two lists).
  The closed form follows from the master theorem.
*/

#include <iostream>
#include <time.h>

using namespace std;

void insertionSort(int *tab, int startTab, int midTab, int endTab) // range inclusive [start, end]
{
    cout << "MS: S = " << startTab << " M = " << midTab << " E = " << endTab << endl;
    for (int i = 1; i < endTab; i++)
    {
        int j = i;
        int temp = tab[j];
        while ((j > 0) && (tab[j - 1] > temp))
        {
            tab[j] = tab[j - 1];
            j--;
        }
        tab[j] = temp;
    }
}

int main()
{
    int n;

    cout << "How many random numbers in an array: ";
    cin >> n;

    // dynamic allocation
    int *tab = new int[n];

    // initiating the random number generator
    srand(time(NULL));

    // loading random numbers to an array
    for (int i = 0; i < n; i++)
    {
        tab[i] = rand() % 10 + 1;
    }

    // before sorting
    cout << "Before sorting: " << endl;

    for (int i = 0; i < n; ++i)
    {
        cout << tab[i] << " ";
    }
    cout << endl;

    merg(tab, 0, n - 1);

    // after sorting
    cout << "After sorting: " << endl;

    for (int i = 0; i < n; ++i)
    {
        cout << tab[i] << " ";
    }

    delete[] tab;
    return 0;
}
