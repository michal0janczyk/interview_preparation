/*
  Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats.
  You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat.
  He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?
  Vos Savant's response was that the contestant should switch to the other door. Under the standard assumptions, contestants who switch have a 2/3
  chance of winning the car, while contestants who stick to their initial choice have only a 1/3 chance.
*/

#include <cassert>
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

// Returns true if we win.
bool monty(int gate, bool change);
bool getOther(int n1, int n2);

int main()
{
    for (int iGames = 10000000; iGames < 100000000; iGames += 10000000)
    {
        int nWinsChange = 0, nWinsNoChange = 0;

        double ratio;
        srand(time(NULL));

        // int i = 0;
        // while (i < nGames)

        for (int i = 0; i < iGames; ++i)
        {
            int gate = rand() % 3;

            // Games without changes -- 33%
            if (monty(gate, false))
            {
                nWinsNoChange += 1;
            }
            // Games without changes -- 66%
            if (monty(gate, true))
            {
                nWinsChange += 1;
            }
            // i += 1;
        }

        ratio = 100.0 * nWinsNoChange / iGames;
        cout << "ratio = " << ratio << endl;

        ratio = 100.0 * nWinsChange / iGames;
        // cout << "ratio = " << ratio << endl;
    }
}

bool getOther(int n1, int n2)
{
    assert(n1 != n2);

    if ((n1 == 0 && n2 == 1) || (n1 == 1 && n2 == 0))
        return 2;

    if ((n1 == 1 && n2 == 2) || (n1 == 2 && n2 == 1))
        return 0;

    if ((n1 == 0 && n2 == 2) || (n1 == 2 && n2 == 0))
        return 1;

    return -1;
}

bool monty(int gate, bool change)
{
    int goodGate = rand() % 3; // a car

    // We don't change the gate.
    if (change == false)
    {
        if (gate == goodGate)
            return true; // we win
        else
            return false; // we lose
    }
    // We do change the gate (change == true).
    else
    {
        if (gate == goodGate)
        {
            // We open any of the other two gates.
            return false;
        }
        else // gate != goodGate
        {
            // We open the gate which is not a car.
            // int openGate = getOther(gate, goodGate);
            return true;
        }
    }
    return false;
}
