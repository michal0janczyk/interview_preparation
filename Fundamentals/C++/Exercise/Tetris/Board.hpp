#pragma once

class Board
{
public:
    Board();
    ~Board();

    static const int height = 30, width = 30;
    const int * const *getTab() { return tab; }

    void insertPiece(const int* const *piece);

	int GetXPosition(int Pos);
	int GetYPosition(int Pos);

	void DumpPiece(int X, int Y, int Piece, int Rotation);
	bool FreeSpace(int X, int Y);
	bool PossibleMove(int X, int Y, int Piece, int Rotation);
	
	void ClearLine(int Y);
	
private:
    // 0 -> empty square, 1 -> square tile, ...
    int **tab;

    static const int startX = 0, startY = 10;
};
