#include <iostream>
#include <ctime>
#include <cstdlib>
#include <stdlib.h>

using namespace std;

void createTab(int **tab, int h, int w)
{
	for (int iH = 0; iH < h; ++iH)
	{
		tab[iH] = new int[w];
	}

	for (int iH = 0; iH < h; ++iH)
	{
		for (int iW = 0; iW < w; ++iW)
		{
			tab[iH][iW] = 0;
		}
	}
}

void randomGenerator(int **tab, int h, int w)
{
	int randomIndexCol = rand()%11;
	int randomIndexLine = rand()%11;
	int randValue = rand()%11;

	for (int iH = 0; iH < randomIndexCol; ++iH)
	{
		for (int iW = 0; iW < randomIndexLine; ++iW)
		{
			tab[iH][iW] = randValue;
		}
	}
}

void printTab(int **tab, int h, int w)
{
    for (int iH = 0; iH < h; ++iH)
    {
        for (int iW = 0; iW < w; ++iW)
        {
            cout << tab[iH][iW] << " ";
        }

        cout << endl;
    }
}

unsigned short int enterElem(int **tab, int h, int w, int *value)
{
	short int col = NULL;
	short int line = NULL;
	short int elem = NULL;

	cout << "\n" <<"Enter the number of columns : ";
	cin >> col;
	cout << "Enter the number of line : " ;
	cin >> line;
	cout << "Enter a value of element : ";
	cin >> elem;

/*
    for (int iH = h-1; iH >= col-1; --iH)
    {
        for (int iW = w-1; iW >= line-1; --iW)
        {
            tab[col-1][line-1] = elem;
        }
    }*/

    int *row = tab[line - 1];
    row[col - 1] = elem;


    //vector<vector<int>> v;
    tab[line - 1][col - 1] = elem;

    return elem;
}

bool checkHorizontal(int **tab, int w, int value)
{
    for (int iW = 0; iW < w; ++iW)
    {
        if( tab[w][iW] == value)
        	{return false;}
        return true;
    }
}

bool checkVertical(int **tab, int h, int value)
{
    for (int iH = 0; iH < h; ++iH)
    {
        if( tab[iH][h] == value)
        	{return false;}
        return true;
    }
}

void removeTab(int **tab, int h)
{
	for (int iH = 0; iH < h; ++iH)
	{
		delete[] tab[iH];
	}

	delete[] tab;
}


int main()
{
	srand(time(NULL));
	const short int h = 9, w = 9;
	int **tab = new int *[h];
    short int *value;


	createTab(tab, h, w);
	printTab(tab, h, w);

	while(true)
	{
		createTab(tab, h, w);
		//randomGenerator(tab, h, w);
		if(checkHorizontal(tab, w, value) == true && checkVertical(tab, h, value) == true)
		enterElem(tab, h, w, value);
		system("cls");
		printTab(tab, h, w);
	}

	removeTab(tab, h);
	cin.get();
	return 0;
}
