#include <iostream>
#include <vector>

using namespace std;

struct Position
{
    int x, y;
};

class Map
{
public:
    //zeruje mape
    Map();
    ~Map();

    //Rysuje mape i postacie
    void draw();
    void reset();

    int getX() const { return MAP_X; }
    int getY() const { return MAP_Y; }

    //Umieszcza gracza na mapie
    void put_player(Position & player);

    //Umieszcza na mapie wrogow
    void put_enemie(vector<Position> & enemie);

private:
    static const int MAP_X = 50;
    static const int MAP_Y = 50;

    // Zalokowana mapa gry
    int **MAP = NULL;
};

class Game
{
public:
    Game();
    ~Game();

    //Start gry
    void start();

    bool fail_check();
    void fail();

    int getMapX() const { return map.getX(); }
    int getMapY() const { return map.getY(); }

    void create_enemies(int n);

    //Podnosi wynik
    void score_up();

    //Przesuwa gracza
    void move_player();

    //"ai" wrogow
    void enemie_ai();

private:
    Position player;
    vector <Position> enemie;

    Map map;

    int score = 0;
    int enemie_selected = 0;
    bool not_failed = true;
};
