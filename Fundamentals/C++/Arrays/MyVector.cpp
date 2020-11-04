#include <iostream>

using namespace std;

class MyVector
{
public:
    MyVector();
    ~MyVector();

    void push_back(int x);
    int pop_back();

    int getElem(int i) const;

    int size() const { return n; }

private:
    int n;
    int *tab;
};

MyVector::MyVector()
{
    n = 0;
    tab = NULL;
}

MyVector::~MyVector()
{
    delete[] tab;
}

void MyVector::push_back(int x)
{
    n += 1;
    int *newTab = new int[n];

    // Przepisujemy stare elementy do nowej tablicy.
    for (int i = 0; i < n - 1; ++i)
    {
        newTab[i] = tab[i];
    }

    newTab[n - 1] = x; // Dodajemy element na koniec (indeks n - 1).

    delete[] tab;
    tab = newTab;
}

int MyVector::pop_back()
{
    n -= 1;
    int *newTab = new int[n];

    // Przepisujemy stare elementy do nowej tablicy.
    for (int i = 0; i < n; ++i)
    {
        newTab[i] = tab[i];
    }

    int last = tab[n]; // ostatni element starej tablicy

    delete[] tab;
    tab = newTab;

    return last;
}

int MyVector::getElem(int i) const
{
    if (i < 0 or i >= n)
    {
        // "błąd"
        return 0;
    }

    return tab[i];
}

int main()
{
    MyVector *v = new MyVector;

    v->push_back(1);
    v->push_back(2);
    v->push_back(3);
    v->push_back(4);

    cout << "v[0] = " << v->getElem(0) << " size = " << v->size() << endl;
    cout << v->pop_back() << " " << v->size() << endl;

    delete v;
}
