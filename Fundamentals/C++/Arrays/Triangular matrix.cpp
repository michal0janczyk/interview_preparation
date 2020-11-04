#include <cstdlib>
#include <ctime>
#include <iostream>

using namespace std;

bool Toeplitz(int **tab, int height, int width)
{
	for (int h = 0; h < height - 1; ++h)
	{
		for (int w = 0; w < width - 1; ++w)
		{
			if (tab[h][w] != tab[h+1][w+1])
			{
				return false;
			}
		}
	}

	return true;
}

int main()
{
	const int height = 5;
	const int width = 5;

	int **tab = new int *[height];

	for (int i = 0; i < width; ++i)
	{
		tab[i] = new int[width];
	}

	for (int i = 0; i < width; ++i)
	{
		delete[] tab[i];
	}

	for (int h = 0; h < height; ++h)
	{
		for (int w = 0; w < width; ++w)
		{
			if (h >= w)
			{
				tab[h][w] = rand() % 10;
			}
			else
			{
				tab[h][w] = 0;
			}
		}
	}

	delete[] tab;
	return 0;
}
