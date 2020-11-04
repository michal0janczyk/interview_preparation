using namespace std;

template<class T> vec<T>::vec()
{
    buffer_ = nullptr;

    capacity_ = 5;
    reserve(capacity_);

    size_ = 0;
}

template<class T> vec<T>::~vec()
{
    ::operator delete (buffer_);
}

template<class T> vec<T>::vec(const vec &v)
{
    size_ = v.size_;
    capacity_ = v.capacity_;
    buffer_ = (static_cast<T*>(::operator new(sizeof(T) * capacity_)));

    for(unsigned int i = 0; i < size_; ++i)
    {
        buffer_[i] = v.buffer_[i];
    }
}

template<class T> vec<T>::vec(vec &&v)
{
    this->capacity_ = v.capacity_;
    this->size_ = v.size_;

    this->buffer_ = v.buffer_;
    v.buffer_ = nullptr;
    v.swap(*this);

}

template<class T> vec<T>::vec(unsigned int capacity)
{
    size_ = 0;
    capacity_ = capacity;

    buffer_ = new T[capacity];
}

template<class T> vec<T>::vec(unsigned int size, const T &init)
{
    size_ = size;
    buffer_ = new T[capacity_];

    for(unsigned int i = 0; i < size; ++i)
    {
        buffer_[i] = init;
    }
}

template<class T> T& vec<T>::operator[](unsigned int index)
{
    return buffer_[index];
}

template<class T> const vec<T> &vec<T>::operator[](const vec<T> &)
{

}

template<class T> vec<T> &vec<T>::operator=(vec &v)
{
    delete[] buffer_;
    size_ = v.size_;
    capacity_ = v.capacity_;
    buffer_ = new T[capacity_];

    for(unsigned int i = 0; i < size_; ++i)
    {
        buffer_[i] = v.buffer_[i];
    }
    return *this;
}

 template<class T> const vec<T> &vec<T>::operator=(const vec &v)
 {
     vec<T> tmp(v);
     tmp.swap(*this);
     return *this;
 }

 template <class T> vec<T> &vec<T>::operator=(vec &&vv) noexcept
 {
     vv.swap(*this);
     return *this;
 }

template<class T> void vec<T>::reserve(unsigned int newCapacity)
{
    cout << "Reserving: " << newCapacity << endl;

    // if (buffer_ == nullptr) // sanity check
    // {
    //     size_ = 0;
    //     capacity_ = 0;
    // }

    T* tempBuffer = static_cast<T *>(realloc(buffer_, newCapacity * sizeof(T)));

    if (tempBuffer == nullptr)
    {
        // Warto dodac wiecej informacji
        throw new std::runtime_error("realloc failed");
    }

    capacity_ = newCapacity;

    if (capacity_ < size_)
    {
        size_ = capacity_;
    }

    buffer_ = tempBuffer;
    cout << "Reserved: " << newCapacity << endl;
}

template<class T> void vec<T>::push_back(const T &value)
{
    assert(size_ <= capacity_);

    if (size_ == capacity_)
    {
        unsigned newCapacity = capacity_ * 2;
        reserve(newCapacity);
    }

    buffer_[size_] = value;
    size_ += 1;
}

template<class T> void vec<T>::pop_back()
{
    --size_;
    // reduce capacity?
}

template<class T> bool vec<T>::empty() const
{
    return size_ == 0;
}

template<class T> unsigned int vec<T>::size() const
{
    return (unsigned int) size_;
}

template <class T> unsigned int vec<T>::capacity() const
{
    return (unsigned int) capacity_;
}

template<class T> void vec<T>::clear()
{
    buffer_ = nullptr;
    capacity_ = 0;
    size_ = 0;

    delete[] buffer_;
}

template<class T> typename vec<T>::iterator vec<T>::begin()
{
    return buffer_;
}

template<class T> typename vec<T>::iterator vec<T>::end()
{
    return buffer_ + size();
}

 template <class T> void vec<T>::swap(vec &v) noexcept
 {
     using std::swap;
     swap(size_, v.size_);
     swap(capacity_, v.capacity_);
     swap((T *&)buffer_, v.buffer_);
 }

//template class vec<int>;
