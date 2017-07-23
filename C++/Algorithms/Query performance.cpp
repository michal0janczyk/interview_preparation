#include <iostream>
#include <vector>
#include <windows.h>

using namespace std;

void sort1(int *tab, int n)
{
    int x = 5;

    for (int i = 0; i < 100000000; ++i)
    {
        x += 1;
    }
}

void sort2(int *tab, int n)
{
    int x = 5;

    for (int i = 0; i < 10000000; ++i)
    {
        x += 1;
    }
}

void calcStdDev(const vector<double> &times)
{
    double avg = 0;

    for (size_t i = 0; i < times.size(); ++i)
    {
        avg += times[i];
    }

    avg = avg / times.size();

    // double stdDev = 0;
    double Res = 0;

    for (size_t i = 0; i < times.size(); ++i)
    {
        double x = times[i] - avg;
        x = x * x;
        Res += x;
    }

    Res /= times.size();

    cout << "stdDeV " << Res << endl;
}

void calcStats(const vector<double> &times)
{
    double sum = 0;

    for (size_t i = 0; i < times.size(); ++i)
    {
        sum += times[i];
    }

    sum /= times.size();
    cout << "Elapsed (ms) = " << sum << endl;
}

int main()
{
    vector<double> times;
    const int n = 100;

    LARGE_INTEGER frequency;        // ticks per second
    LARGE_INTEGER t1, t2;           // ticks
    double elapsedTime;
    // get ticks per second
    QueryPerformanceFrequency(&frequency);

    for (int i = 0; i < n; ++i)
    {
        cout << (i + 1) << "/" << n << endl;

        QueryPerformanceCounter(&t1);

        // sort1(NULL, 1);
        sort2(NULL, 2);

        QueryPerformanceCounter(&t2);

        // compute and print the elapsed time in millisec
        elapsedTime = (t2.QuadPart - t1.QuadPart) * 1000.0 / frequency.QuadPart;
        times.push_back(elapsedTime);
    }

    calcStats(times);
    calcStdDev(times);
}
