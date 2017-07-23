#pragma once

#include "Board.hpp"
#include "Pieces.hpp"
#include "InputHandler.hpp"

class GameState
{
public:
    GameState();
    ~GameState();

    void init();

    void update(Choice choice);
    const int * const *getTab() { return board->getTab(); }

private:
    int score;
    
    Board *board;
    Pieces *pieces;

    bool newPiece = true;
};
