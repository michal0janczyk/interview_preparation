#include <cstdarg>
#include <iostream>

using namespace std;

int sum(int n, ...)
{
    va_list ap;
    va_start(ap, n);

    int s = 0;

    for (int i = 0; i < n; ++i)
    {
        int cur = va_arg(ap, int);
        s += cur;
    }

    va_end(ap);
    return s;
}

int main()
{
    //cout << sum(3, 1, 2, 3) << endl;
    cout << sum(3, 1, 2, 3) << endl;
}
