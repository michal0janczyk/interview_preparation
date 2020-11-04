#include <iostream>
#include <stdexcept>

#include "cowStr.hpp"

using namespace std;

/** Default constructor */
MyStr::MyStr() noexcept
{
  try
  {
    strHolder = new StrHolder;
  }
  catch (const std::bad_alloc &ba)
  {
    std::cerr << ba.what() << std::endl;
  }

  strHolder->str = nullptr;
  strHolder->size = 0;

  strHolder->instanceCounter = 1;
}

MyStr::MyStr(int n) noexcept
{
  try
  {
    strHolder = new StrHolder;
    strHolder->str = new char[n];
  }
  catch (const std::bad_alloc &ba)
  {
    std::cerr << ba.what() << std::endl;
  }

  strHolder->size = n;
  strHolder->instanceCounter = 1;
}

MyStr::MyStr(const std::string &str) noexcept
{
  try
  {
    strHolder = new StrHolder;
    strHolder->str = new char[str.size()];
    strcpy(strHolder->str, str.c_str());
  }
  catch (const std::bad_alloc &ba)
  {
    std::cerr << ba.what() << std::endl;
  }

  strHolder->size = str.size();
  strHolder->instanceCounter = 1;
}

/** Destructor */
MyStr::~MyStr()
{
  strHolder->instanceCounter -= 1;

  if (strHolder->instanceCounter == 0)
  {
    delete[] strHolder->str;
    delete strHolder;
  }
}

/** Copy constructor */
MyStr::MyStr(const MyStr &otherStr)
{
  this->strHolder = otherStr.strHolder;
  strHolder->instanceCounter += 1;
}

/** Move constructor */
MyStr::MyStr(MyStr &&otherStr)
{
  otherStr.strHolder->str = nullptr;
}

/** Copy assignment operator */
MyStr &MyStr::operator = (const MyStr &otherStr)
{
  char *tempStr = new char[std::strlen(otherStr.strHolder->str) + 1];
  std::strcpy(tempStr, otherStr.strHolder->str);
  delete[] strHolder->str;
  strHolder->str = tempStr;
  return *this;
}

/** Move assignment operator */
MyStr &MyStr::operator = (MyStr &&otherStr)
{
  if(this != &otherStr)
  {
    delete[] otherStr.strHolder->str;
    strHolder->str = otherStr.strHolder->str;
    otherStr.strHolder->str = nullptr;
  }
  return *this;
}

/** Copy on write */
char &MyStr::operator[](int index)
{
    //cout << "NON-CONST []" << endl;
  copyExistingHolder();
  return strHolder->str[index];
}

char &MyStr::operator[](int index) const
{
    //cout << "CONST []" << endl;
  return strHolder->str[index];
}

/** Private */
void MyStr::copyExistingHolder()
{
    if (strHolder->instanceCounter == 1)
        return;

  strHolder->instanceCounter -= 1;

  StrHolder *newHolder = new StrHolder;

  // try catch -- odnosi do kazdego new

  newHolder->str = new char[strHolder->size];
  std::strcpy(newHolder->str, strHolder->str);

  newHolder->size = strHolder->size;
  newHolder->instanceCounter = 1;

  this->strHolder = newHolder;
  cout << "Copy holder" << endl;
}

unsigned int MyStr::stringSize() const
{
  if(strHolder->size)
  {
      return std::strlen(strHolder->str);
  }
  else
  {
      return 0; // maybe -1?
  }
}
