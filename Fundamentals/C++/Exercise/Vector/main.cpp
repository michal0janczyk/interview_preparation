#include <iostream>

#include "vec.h"
//template  class vec<int>;

using namespace std;

int main()
{
    cout << "Started" << endl;
    vec<int> v;

    v.push_back(10);
    cout << "Pushed back" << endl;

    cout<<v[0];

    return 0;
}
