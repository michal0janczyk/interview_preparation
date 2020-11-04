#include <iostream>

class S
{
    public:
        static S &getInstance()
        {
            static S instance; // Guaranteed to be destroyed.
                               // Instantiated on first use. "lazy initialization"
            return instance;
        }

        void print() { std::cout << "PRINT" << std::endl; };

    private:
        S() {};                   // Constructor? (the {} brackets) are needed here.

        // C++ 03
        // ========
        // Dont forget to declare these two. You want to make sure they
        // are unacceptable otherwise you may accidentally get copies of
        // your singleton appearing.
        S(S const&);              // Don't Implement
        void operator=(S const&); // Don't implement
};
