#include <iostream>

#include "OutputHandler.hpp"

using namespace std;

void OutputHandler::dump(const int * const *tab)
{
    // We dump the board to the console.
    // Board[][] == 0 -> dump ' ', else '*'.
    system("cls");

	for (int i = 0; i < height; ++i)
	{
		for (int j = 0; j < width; ++j)
		{
			cout << tab[i][j] << " " ;
		}
		cout << endl;
	}
}
