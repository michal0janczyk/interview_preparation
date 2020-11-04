#include <iostream>

using namespace std;

struct Cell
{
    int x;
    Cell *next;
};

void addX(Cell **headPtr, int x)
{
    Cell *newCell = new Cell;

    newCell->x = x;
    newCell->next = NULL;

    if (*headPtr == NULL)
    {
        *headPtr = newCell;
    }
    else
    {
        Cell *it = *headPtr;

        while (it->next) // nie samo "it", bo chcemy ostatni element a nie ostatni next
        {
            it = it->next;
        }

        it->next = newCell;
    }
}

void addXBeginning(Cell **headPtr, int x)
{
    Cell *newCell = new Cell;

    if (newCell != NULL)
    {
        newCell->x = x;
        newCell->next = *headPtr;
        *headPtr = newCell;
    }
}

// index == 0, to dodajemy na pocz¹tku, 1 -> "drugi na liœcie"
void addXMid(Cell **headPtr, int x, int index)
{
    Cell *newCell = new Cell;
    newCell->x = x;

    int i = 0;
    Cell *it = *headPtr;
    Cell *prev = NULL;
    
    while (it != NULL)
    {
        if (i == index)
        {
            // Dodajemy nowy element przed aktualny.
            newCell->next = it;

            if (prev)
            {
                prev->next = newCell;
            }

            if (i == 0)
            {
                *headPtr = newCell;
            }

            return;
        }

        i++;
        prev = it;
        it = it->next;
    }
}

// Liczymy sumê elementów na liœcie.
int calcSum(Cell *head)
{
    int sum = 0;
    Cell *it = head;

    while (it != NULL)
    {
        sum += it->x;
        it = it->next;
    }

    cout << sum << endl;
    return sum;
}

void printList(const Cell *head)
{
    const Cell *it = head;

    // while(it) <-> while(it != NULL);
    while (it != NULL)
    {
        cout << it->x << ' ';
        it = it->next;
    }
}

// Usuwamy listê i pamiêæ
void delList(Cell *head)
{
    Cell *it = head;

    while (it != NULL)
    {
        Cell *tmp = it->next;
        delete it;
        it = tmp;
    }
}

void delElemBeginning(Cell **headPtr)
{
    Cell *tmp = (*headPtr)->next;

    delete *headPtr;
    *headPtr = tmp;
}

void delElemEnd(Cell **headPtr)
{
    Cell *tmp = (*headPtr)->next;

    // Iterujemy do koñca
    while (tmp != NULL)
    {
        // Usuwamy pamiêæ
        delete *headPtr;
        *headPtr = tmp;
    }

    // Ustawiæ przedostatni->next NULL
    tmp->next = NULL;
}

void delElem(Cell **headPtr, int x)
{
    // Specjalny przypadek -- g³owa
    if ((*headPtr)->x == x)
    {
        delElemBeginning(headPtr);
        return;
    }

    // Iterujemy a¿ znajdziemy x.
    Cell *it = *headPtr;

    while (it != NULL)
    {
        // if (it->next->x == x)
        if (it->next->x == x)
        {
            // Usuwamy pamiêæ.
            // Ustawiamy poprzedni na nastêpny.
            delete it;
            *headPtr = it->next;
        }
    }
}


int main()
{
    Cell *head = NULL;

    addX(&head, 5);
    addX(&head, 10);
    addX(&head, 15);

    //addXMid(&head, 12);

    addXBeginning(&head, 2);
    addXBeginning(&head, 3);
    addXBeginning(&head, 12);

    delElemBeginning(&head);
    delElemEnd(&head);

    delElem(&head, 3);

    calcSum(head);

    printList(head);
    delList(head);

    cin.get();
}
