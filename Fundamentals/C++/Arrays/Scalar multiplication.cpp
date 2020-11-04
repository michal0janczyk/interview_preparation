#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

void printMat(int mat[2][2])
    {
    	for (int iH = 0; iH < 2; ++iH)
    	{
    		for (int iW = 0; iW < 2; ++iW)
    		{
    			cout << mat[iH][iW] << " ";
    		}
    		cout << endl;
    	}
    }

int main()
{
    const int h = 2 , w = 2;
    int scalar;
    int mat_1[h][w], mat_Res[h][w];

    srand(time(NULL));

    const int minR = -50, maxR = 25;

    for (int iH = 0; iH < h; ++iH)
    {
    	for (int iW = 0; iW < w; ++iW)
    	{
            mat_1[iH][iW] = minR + rand() % (maxR - minR + 1);
    	}
    }

    printMat(mat_1);

    cout << endl;

    cout <<"Podaj wartosc skalara: ";
    cin >> scalar;

    cout << endl;

    for (int iH = 0; iH < h; ++iH)
    {
    	for (int iW = 0; iW < w; ++iW)
    	{
    		mat_Res[iH][iW] = mat_1[iH][iW] * scalar;
    	}
    }

    printMat(mat_Res);

    cin.get();
    return 0;
}
