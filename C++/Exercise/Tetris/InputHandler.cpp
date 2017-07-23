#include "InputHandler.hpp"

#include <conio.h>
#include <iostream>

using namespace std;

// Read input from the keyboard and set choice.
void InputHandler::read()
{
    char cur;

    if (_kbhit())
    {
        cur = _getch();
        choice = None;
    }
    else
    {
        return;
    }

	switch (cur)
	{
	case 'w':
	{
        choice = Up;
	}
	case 'a':
	{
        choice = Left;
	}
	case 'd':
	{
        choice = Right;
	}
	case 's':
	{
        choice = Down;
	}
    case ' ':
        choice = Rotate;
	}
}
