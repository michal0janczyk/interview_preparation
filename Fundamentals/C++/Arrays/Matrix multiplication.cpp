#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

void printMat(int **mat, int h, int w)
{
    for (int iH = 0; iH < h; ++iH)
    {
        for (int iW = 0; iW < w; ++iW)
        {
            cout << mat[iH][iW] << " ";
        }

        cout << endl;
    }
}

int **multMat(int **mat_1, int h1, int w1, int **mat_2, int h2, int w2)
{
    //macierz wynikowa:
    int hRes = 2, wRes = 2;
    int **mat_Res = new int *[hRes];

    for (int iH = 0; iH < hRes; ++iH)
    {
        mat_Res[iH] = new int[wRes];
    }

    for (int iH = 0; iH < hRes; ++iH)
    {
        for (int iW = 0; iW < wRes; ++iW)
        {
            // mat_Res[iH][iW] = 0;

            for (int k = 0; k < wRes; ++k)
            {
                mat_Res[iH][iW] = mat_1[iW][k] * mat_2[k][iH];
            }
        }
    }

    return mat_Res;
}

int main()
{
  srand(time(NULL));
  int h1 = 2, w1 = 2;
	int **mat_1 = new int *[h1];

	for (int iH = 0; iH < h1; ++iH)
	{
		mat_1[iH] = new int[w1];
	}

	for (int iH = 0; iH < h1; ++iH)
	{
		for (int iW = 0; iW < w1; ++iW)
		{
			mat_1[iH][iW] = rand() % 11;
		}
	}

	printMat(mat_1, h1, w1);
	cout << endl;

	int h2 = 2, w2 = 2;
	int **mat_2 = new int *[h2];

	for (int iH = 0; iH < h2; ++iH)
	{
		mat_2[iH] = new int[w2];
	}

	for (int iH = 0; iH < h2; ++iH)
	{
		for (int iW = 0; iW < w2; ++iW)
		{
			mat_2[iH][iW] = rand() % 11;
		}
	}

	printMat(mat_2, h2, w2);
	cout << endl;

    int **res = multMat(mat_1, h1, w1, mat_2, h2, w2);
    printMat(res, h1, w1);

    for (int iH = 0; iH < h1; ++iH)
    {
        delete[] res[iH]; // mat_1[3][3]
    }

    delete[] res;

    for (int iH = 0; iH < h1; ++iH)
    {
        delete[] mat_1[iH]; // mat_1[3][3]
    }

    delete[] mat_1;

    for (int iH = 0; iH < h1; ++iH)
    {
        delete[] mat_2[iH];
    }

    delete[] mat_2;

    cin.get();
    return 0;
}
