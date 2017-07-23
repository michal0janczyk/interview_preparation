#include "GameState.hpp"
#include "Pieces.hpp"

#include <cstdlib>

GameState::GameState()
{
    board = new Board;
    pieces = new Pieces;
}

GameState::~GameState()
{
    delete board;
}

void GameState::init()
{
    
}

void GameState::update(Choice choice)
{
    // Depending on choice, we modify the game state, e.g., move the piece.

    // Automatic update (pieces fall, new pieces spawn).

    // 1. Nowy klocek?

    if (newPiece)
    {
        int **curPiece = pieces->getRandPiece();
        board->insertPiece(curPiece);

        newPiece = false;
    }

    // 2. Czy opuszczamy klocek?

    // 3. Czy mamy przemiescic lub obrocic klocek (w zaleznosci od choice)?
    // Jeœli aktualny klocek upad³ na dó³, to newPiece = true.

    // 4. Czy przegralismy?
}
