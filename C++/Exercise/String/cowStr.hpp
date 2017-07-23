#ifndef COWSTR_H
#define COWSTR_H

#include <iostream>
#include <cstring>
#include <new>
#include <sstream>
#include <string>

struct StrHolder
{
  char *str;
  int  size;
  int  capacityString;
  int  instanceCounter;
};

class MyStr
{
public:
    /** Default constructor */
    MyStr() noexcept; // doesn't throw
    MyStr(int n) noexcept;
    MyStr(const std::string &str) noexcept;

    /** Destructor */
    ~MyStr();

    /** Copy constructor */
    MyStr(const MyStr &otherStr);

    /** Move constructor */
    MyStr(MyStr &&otherStr);

    /** Copy assignment operator */
    MyStr &operator = (const MyStr &otherStr);

    /** Move assignment operator */
    MyStr &operator = (MyStr &&otherStr);

    /** Copy on write */
    char &operator [](int index);
    char &operator [](int index) const;

    char *getStr(){return strHolder->str;}
    int  getSize(){return strHolder->size;}

    std::string toString() const
    {
        std::ostringstream ss;
        ss << strHolder->str << " (" << strHolder->size << ")";

        return ss.str();
    }

private:
    void copyExistingHolder();
    unsigned int stringSize() const;
    StrHolder *strHolder;
};

#endif // COWSTR_H
