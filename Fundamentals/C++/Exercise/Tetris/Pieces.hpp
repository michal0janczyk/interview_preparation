#pragma once

class Pieces
{
public:
    Pieces();
    ~Pieces();

    int BlockType(int TotalPieces, int Rotation, int X, int Y);

    int **getRandPiece();

    static const int tabSize = 5;

private:
	static const int nPieces = 7;
	static const int nRot = 4;

    int **pieces[nPieces][nRot];
};
