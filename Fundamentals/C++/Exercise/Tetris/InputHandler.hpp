#pragma once

enum Choice { Up, Down, Left, Right, Rotate, None };

class InputHandler
{
public:
    void read();
    Choice getChoice() { return choice; }

private:
    Choice choice;
};
