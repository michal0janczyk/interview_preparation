#include "InputHandler.hpp"
#include "OutputHandler.hpp"
#include "GameState.hpp"

#include <windows.h>

int main()
{
    // Init
    InputHandler *ih = new InputHandler();
    OutputHandler *oh = new OutputHandler();

    GameState *gs = new GameState();
    gs->init();

    while (true)
    {
        ih->read();
        gs->update(ih->getChoice());

        oh->dump(gs->getTab());

        Sleep(500); // ms
    }

    delete ih;
    delete oh;
    delete gs;
}
