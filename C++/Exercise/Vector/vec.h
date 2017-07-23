#ifndef VEC_H
#define VEC_H

#include <cassert>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <stdexcept>

template <typename T>
class vec {
public:
    vec();
    ~vec();

    vec(const vec<T> &v);
    vec(vec<T> &&v);

    vec(unsigned int capacity);
    vec(unsigned int size, const T& init);

    T & operator[](unsigned int index) ;
    const vec<T> & operator[](const vec<T> &);

    vec<T> & operator=(vec<T> &v);
    const vec<T> & operator=(const vec<T> &v);
    vec<T> & operator=(vec<T> &&vv) noexcept;

    unsigned int capacity() const;
    unsigned int size() const;
    bool empty() const;

    // newCapacity is the new #elements
    void reserve(unsigned int newCapacity);

    void push_back(const T& value);
    void pop_back();
    void clear();

    T* getBuf() { return buffer_; }
    const T* getBuf() const { return buffer_; }

    typedef T* iterator;
    typedef const T* const_iterator;

    iterator begin(); // points to the 1st element
    iterator end(); // points behind the last element

    void swap(vec &v) noexcept;

private:
    T *buffer_;
    unsigned int capacity_;
    unsigned int size_;

    bool foreignBuf = false; // foreign buf oznacza, że będziemy musieli skopiować ten bufor w przypadku modyfikacji elementów
};
//template  class vec<int>;

#include "vec.cpp"

#endif // VEC_H
