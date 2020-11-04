#include <iostream>

using namespace std;

struct Cell
{
    int x;

    Cell *next;
    Cell *prev;
};

void addXEnd(Cell **headPtr, Cell **tailPtr, int x)
{
    Cell *newCell = new Cell;
    newCell->x = x;

    // Pusta lista
    if (*headPtr == NULL && *tailPtr == NULL)
    {
        *headPtr = newCell;
        *tailPtr = newCell;

        newCell->next = NULL;
        newCell->prev = NULL;

        return;
    }

    (*tailPtr)->next = newCell;

    newCell->prev = *tailPtr;
    newCell->next = NULL;

    *tailPtr = newCell;
}

void addXBeginning(Cell **headPtr, Cell **tailPtr, int x)
{
    Cell *newCell = new Cell;
    newCell->x = x;

    if (*headPtr == NULL && *tailPtr == NULL)
    {
        *headPtr = newCell;
        *tailPtr = newCell;

        newCell->next = NULL;
        newCell->prev = NULL;

        return;
    }

    (*headPtr)->prev = newCell;

    newCell->next = *headPtr;
    newCell->prev = NULL;

    *headPtr = newCell;
}

int main()
{
    Cell *head = NULL;
    Cell *tail = NULL;

    addXEnd(&head, &tail, 5);
    addXEnd(&head, &tail, 10);
    addXEnd(&head, &tail, 15);

    addXBeginning(&head, &tail, 111111111111111);

    cin.get();
}
