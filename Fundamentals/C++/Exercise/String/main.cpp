#include <iostream>

#include "cowStr.hpp"

using namespace std;

int main()
{
    cout << "Started" << endl;

    MyStr s1("ala");
    MyStr s2 = s1;

    MyStr *ps1 = new MyStr("ada");
    MyStr *ps2 = new MyStr(*ps1);

    cout << s1.getStr() << " " << s1.getSize() << endl;
    cout << s2.toString() << endl;

    cout << ps1->toString() << endl;
    cout << ps2->toString() << endl;

    cout << (*ps1)[0] << endl;
    cout << (*ps1)[1] << endl;
    cout << (*ps1)[2] << endl;

    cout << ps1->toString() << endl;
    cout << ps2->toString() << endl;

    (*ps1)[0] = 'A';

    cout << (*ps1)[0] << endl;
    cout << (*ps1)[1] << endl;
    cout << (*ps1)[2] << endl;

    cout << "1) " << ps1->toString() << endl;
    cout << "2) " << ps2->toString() << endl;

    (*ps2)[1] = 'D';

    cout << "1) " << ps1->toString() << endl;
    cout << "2) " << ps2->toString() << endl;

    const MyStr *ps3 = new MyStr("ada");

    cout << ps3->toString() << endl;
    cout << (*ps3)[0] << endl;

    cout << noexcept(MyStr()) << endl;

    delete ps1;
    delete ps2;
}
