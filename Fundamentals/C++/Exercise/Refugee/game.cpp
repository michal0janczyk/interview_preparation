#include <cstdlib>
#include <iostream>
#include <vector>
#include <conio.h>

#include "gamenew.hpp"

using namespace std;

Game::Game()
{
    player.x = 25;
    player.y = 25;
}

Game::~Game()
{

}

//Start gry
void Game::start()
{
    system ("title TIME TO PLAY THE GAME");
    char menu = 'z';
    cout << "=======================================" << endl;
    cout << "=========TIME TO PLAY THE GAME=========" << endl;
    cout << "=======================================" << endl;
    cout << "How many enemies do you want: " << endl;
    cout << "A) 1, B) 2, C) 3, D) 4 " << endl;
    cin >> menu;

    switch(menu)
    {
    case 'A' :
        create_enemies(1);
        enemie_selected = 1;
        break;
    case 'B' :
        create_enemies(2);
        enemie_selected = 2;
        break;
    case 'C' :
        create_enemies(3);
        enemie_selected = 3;
        break;
    case 'D' :
        create_enemies(4);
        enemie_selected = 4;
        break;
    }
    not_failed = true;
    system("cls");

    map.reset();
    map.put_player(player);
    map.put_enemie(enemie);
    map.draw();
}

bool Game::fail_check()
{
    return not_failed;
}

//Przegrana
void Game::fail()
{
    system ("cls");
    cout << "GAME OVER !" << endl;
    cout << "Monsters: " << enemie_selected << endl;
    cout << "Score: " << score * enemie_selected << endl;
    not_failed = false;
}

void Game::create_enemies(int n)
{
    //Tworzy wrogow
    Position enemies1 = {0, 0};
    Position enemies2 = {0, 49};
    Position enemies3 = {49, 0};
    Position enemies4 = {49, 49};

    //Dodaje wrogow do wektora
    switch (n)
    {
    case 1:
        enemie.push_back(enemies1);
        break;
    case 2:
        enemie.push_back(enemies1);
        enemie.push_back(enemies2);
        break;
    case 3:
        enemie.push_back(enemies1);
        enemie.push_back(enemies2);
        enemie.push_back(enemies3);
        break;
    case 4:
        enemie.push_back(enemies1);
        enemie.push_back(enemies2);
        enemie.push_back(enemies3);
        enemie.push_back(enemies4);
        break;
    }
}

//Podnosi wynik
void Game::score_up()
{
    ++score;
}

//Przesuwa gracza
void Game::move_player()
{
    // klawisz do procedury move
    char move = getch();

    switch(move)
    {
    case 'w' :
        if(player.x-1 == -1)
            break;
        else
            player.x++;
        break;
    case 's' :
        if(player.x+1 == map.getX())
            break;
        else
            player.x--;
        break;
    case 'a' :
        if(player.y-1 == -1)
            break;
        else
            player.y--;
        break;
    case 'd' :
        if(player.x+1 == map.getY())
            break;
        else
            player.y++;
        break;
    }
}

//"ai" wrogow
void Game::enemie_ai()
{
    //Algorytm godniacego AI
    for (size_t i = 0; i < enemie.size(); ++i)
    {
        if(enemie[i].x < player.x)
        {
            enemie[i].x++;
        }
        if(enemie[i].x > player.x)
        {
            enemie[i].x--;
        }
        if(enemie[i].y < player.x)
        {
            enemie[i].y++;
        }
        if(enemie[i].y > player.x)
        {
            enemie[i].y--;
        }

        //Jezeli wrog ma takie same pozycje jak gracz to znaczy ze go zlapa wiec koniec gry
        if ((enemie[i].y == player.y) && (enemie[i].x == player.x))
        {
            cout << "HAHAHAHA Got you !!!" << endl;
            fail();
        }
    }
}

//zeruje mape
Map::Map()
{
    for (int i = 0; i < MAP_X; ++i)
    {
        MAP[i] = new int [MAP_Y];
    }

    for (int i = 0; i < MAP_X; ++i)
    {
        for (int j = 0; j < MAP_Y; ++j)
        {
            MAP[i][j] = 0;
        }
    }
}

Map::~Map()
{
    // dealokujemy MAP
}

//Rysuje mape i postacie
void Map::draw()
{
    for (int i = 0; i < MAP_X; i++)
    {
        for (int j = 0; j < MAP_Y; j++)
        {
            //Zamienia liczby na postacie
            switch(MAP[i][j])
            {
            case 0:
                cout << ".";
                break;
            case 1:
                cout << "E";
                break;
            case 2:
                cout << "#";
                break;
            }
        }
    }
    //Kolejny wiersz mapy
    cout << endl;
}

void Map::reset()
{
    for (int i = 0; i < MAP_X; ++i)
    {
        MAP[i] = new int [MAP_Y];
    }

    for (int i = 0; i < MAP_X; ++i)
    {
        for (int j = 0; j < MAP_Y; ++j)
        {
            MAP[i][j] = 0;
        }
    }
}

//Umieszcza gracza na mapie
void Map::put_player(Position & player)
{
    MAP[player.x][player.y] = 2;
}
//Umieszcza na mapie potwory
void Map::put_enemie(vector<Position> & enemie)
{
    for (int i = 0; i < enemie.size(); i++)
    {
        MAP[enemie[i].x][enemie[i].y] = 1;
    }
}

