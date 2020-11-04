#include "Pieces.hpp"

#include <ctime>

#include <cstring>

#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

// kind
// rotation
// horizontal blocks
// vertical blocks

#include <Windows.h>

Pieces::Pieces()
{
	srand((unsigned int)time(NULL));

	// Zaalokowanie pamiêci
	for (int iP = 0; iP < nPieces; ++iP)
	{
		for (int iR = 0; iR < nRot; ++iR)
		{
			pieces[iP][iR] = new int *[tabSize];

			for (int iC = 0; iC < tabSize; ++iC)
			{
				pieces[iP][iR][iC] = new int[tabSize];
			}
		}
	}

    OutputDebugString("Allocated memory");

	// Sczytaæ plik
    vector<string> lines;
    
    ifstream inpieces("pieces.dat");
	string line;

	if (inpieces.is_open())
	{
		while (getline(inpieces, line))
		{
            lines.push_back(line);
		}
		inpieces.close();
	}
	else
		cout << "Error ! ";

    cout << "Read #lines: " << lines.size() << endl;
    cin.get();

    OutputDebugString("Read from file");

    // TODO

    for (size_t iLine = 0; iLine < lines.size(); ++iLine)
    {
        if (lines[iLine] == "")
        {
            continue;
        }
    }

    OutputDebugString("Saved the pieces");
};

Pieces::~Pieces()
{

}

//SprawdŸ czy dany element mo¿na wyœwietliæ w dany miejscu 

int Pieces::BlockType(int TotalPieces, int Rotation, int X, int Y)
{
	return pieces[TotalPieces][Rotation][X][Y];
}

int **Pieces::getRandPiece()
{
    int iPiece = rand() % nPieces;
    return pieces[iPiece][0];
}
