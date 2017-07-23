/*
  Monte Carlo methods are a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results.
  Their essential idea is using randomness to solve problems that might be deterministic in principle.
  They are often used in physical and mathematical problems and are most useful when it is difficult or impossible to use other approaches.
  Monte Carlo methods are mainly used in three distinct problem classes:[1] optimization, numerical integration, and generating draws from a probability distribution.
*/

#include <cassert>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <time.h>

using namespace std;

int main()
{
    double pi;
    double x;
    double y;
    double distance;
    double point = 0;
    int n;

    cout << "Enter the number of iterations used to estimate pi: ";
    cin >> n;

    if (n <= 0)
    {
        cerr << "Invalid n: " << n << endl;
        return EXIT_FAILURE;
    }

    srand(time(NULL));

    for (int i = 0; i < n; ++i)
    {
        x = (double) rand() / RAND_MAX;
        y = (double) rand() / RAND_MAX;

        assert(x >= 0 and x <= 1);
        assert(y >= 0 and y <= 1);

        // Euclidean
        distance = (x * x) + (y * y);
        distance = sqrt(distance);

        if (distance <= 1)
        {
            point++;
        }
    }

    pi =  4 * point/n;
    cout << "The vaule of pi is " << pi << endl;

    // not zero -- error
    return EXIT_SUCCESS;
} ``
