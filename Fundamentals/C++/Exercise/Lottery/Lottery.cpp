#include <algorithm>
#include <cassert>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <vector>

using namespace std;

const int nNumbers = 6;
const int maxNumber = 49;

vector <int> getNumbers()
{
	// Generujemy 6 liczb -- bez powtórzeń.

	// 0 -> nie ma liczby, 1 -> liczba wylosowana
	vector <int> temp(maxNumber, 0);
	vector <int> draw;
	int number;

	while (draw.size() < nNumbers)
	{
		number = (rand() % maxNumber) + 1; // [1, 49]

		if (temp[number - 1] == 0)
		{
			draw.push_back(number);
			temp[number - 1] = 1;
		}
	}

	// sort(draw.begin(), draw.begin() + draw.size());
	sort(draw.begin(), draw.end());
	return draw;
}

vector <int> readInput()
{
	// Sczytujemy po kolei 6 liczb, dodajemy do wektora.

	vector <int> input;
	vector <int> temp(maxNumber, 0);
	int digit;

	while (input.size() < 6)
	{
		cout << "Podaj " << input.size() + 1 << " liczbe : ";
		cin >> digit;

		if (digit <= 0 or digit > maxNumber)
		{
			cout << "Zla liczba: " << digit << endl;
			continue;
		}

		if (temp[digit] == 0)
		{
			input.push_back(digit);
			temp[digit - 1] = 1;
		}
		else
		{
			cout << "Liczby nie moga sie powtarzac !" << endl;
		}
	}
	
	sort(input.begin(), input.end());
	return input;
}

vector <int> check(const vector <int> *nums, const vector <int> *input)
{
	vector <int> res;

	for (int i = 0; i < 6; ++i)
	{
		for (int j = 0; j < 6; ++j)
		{
			if ((*nums)[i] == (*input)[j])
			{
				res.push_back((*nums)[i]);
			}
		}
	}
	return res;
}

void printVector(const vector<int> *v)
{
    for (unsigned i = 0; i < v->size(); ++i)
    {
        cout << (*v)[i] << " ";
    }
    cout << endl;
}

int main()
{
	srand(time(NULL));

	vector <int> input;
	int choose = 0;

	int nDraws;

	cout << "Podaj liczbe losowan: " << endl;
	cin >> nDraws;

	cout << " Duzy lotek !" << endl;
	cout << " 1. Wybierz wasne liczby. " << endl << " 2. Chybil trafil. " << endl;
	cin >> choose;

	cout << "C: " << choose << endl;

	switch (choose)
	{
	case 1:
		input = readInput();
		break;
	case 2:
		input = getNumbers();
		break;
	default:
		cout << "Blad, wybierz ponownie. " << endl;
		return 0;
	}

	cout << "Wybrane:";
	printVector(&input);

	for (int i = 0; i < nDraws; ++i)
	{
		vector<int> nums = getNumbers();

		cout << "Liczby wylosowane: ";
	    printVector(&nums);

	    assert(input.size() == nums.size());

	    vector<int> match = check(&nums, &input);

	    cout << "Trafienia:";
	    printVector(&match);
	}

	cin.get();
	return 0;
}

/*int drawNumber = 0;
	int allDraw = 0;
	int lottery = 0;

	cout << "Podaj liczbe losowan: ";
	cin >> lottery;

	vector <int> win(lottery, 0)

	while (allDraw < lottery)
	{
		numbers = getNumbers();
		for (int i = 0; i < 6; ++i)
		{
			for (int j = 0; j < 6; ++j)
			{
				input[i] == numbers[j]
				{
					hit += 1;
					win[allDraw].push_back(input[i]);
				}
			}
		}
		check.push_back(hit);
		allDraw += 1;
	}*/
