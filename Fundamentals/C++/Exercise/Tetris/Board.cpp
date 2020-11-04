#include "Board.hpp"
#include "Pieces.hpp"

#include <Windows.h>

Board::Board()
{
	tab = new int *[height];

	for (int i = 0; i < height; ++i)
	{
		tab[i] = new int[width];
	}

	for (int i = 0; i < height; ++i)
	{
		for (int j = 0; j < width; ++j)
		{
			tab[i][j] = 0;
		}
	}
}

Board::~Board()
{
	for (int i = 0; i < height; ++i)
	{
		for (int j = 0; j < width; ++j)
		{
			delete [] tab; 
		}
	}
}

void Board::insertPiece(const int* const *piece)
{
    for (int x = 0; x < Pieces::tabSize; ++x)
    {
        for (int y = 0; y < Pieces::tabSize; ++y)
        {
           tab[startX + x][startY + y] = piece[x][y];
        }
    }

    OutputDebugString("Inserted a piece");
}

void Board::DumpPiece(int X, int Y, int Piece, int Rotation)
{
	//Store each block
}

void Board::ClearLine(int Y)
{
	//Delete one line and move lines one row down

	for (int i = Y; i > 0; --i)
	{
		for (int j = 0; j < width; ++j)
		{
			tab[i][j] = tab[i][j - 1];
		}
	}
}

