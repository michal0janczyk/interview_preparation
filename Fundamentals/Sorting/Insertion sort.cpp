/*
*/

#include <iostream>
#include <time.h>

using namespace std;

void merge_sort(int *tab, int startTab, int midTab, int endTab) // range inclusive [start, end]
{
    cout << "MS: S = " << startTab << " M = " << midTab << " E = " << endTab << endl;

    // setting parameters
    int i = startTab;
    int tmpSize = endTab - startTab + 1;

    // array auxiliary
    int *temp = new int[tmpSize];
    int iTemp = 0;

    // copying data to the auxiliary array
    for (i = startTab; i <= endTab; ++i)
    {
        temp[iTemp++] = tab[i];
    }

    iTemp = 0;
    int midTemp = tmpSize / 2;
    int j = midTemp;

    int q = 0;

    // copying sorted data to the main array
    while (iTemp <= midTemp && j < tmpSize)
    {
        if (temp[iTemp] < temp[j])
        {
            tab[startTab + q] = temp[iTemp++];
        }
        else
        {
            tab[startTab + q] = temp[j++];
        }

        q += 1;
    }
    delete[] temp;
}

// division array
void merg(int *tab, int startTab, int endTab) // range inclusive [start, end]
{
    int mid;

    if (startTab < endTab)
    {
        mid = (startTab + endTab) / 2;

        // splitting left side of the array
        merg(tab, startTab, mid);

        // splitting right side of the array
        merg(tab, mid + 1, endTab);

        //adding the left and right side of array
        merge_sort(tab, startTab, mid, endTab);
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
