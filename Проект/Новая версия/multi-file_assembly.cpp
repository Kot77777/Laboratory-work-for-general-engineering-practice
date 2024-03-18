#include <iostream>
#include <string>
#include "Class_weapon.h"
#include "Grenade.h"
#include "Click.h"
#include "Heal.h"
#include "Gun.h"
#include "Snaiper.h"
#include "SubmachinGun.h"
#include "Knife.h"
#include "Bazooka.h"
#include "Player.h"
#include "Enemy.h"
using namespace std;


int main()
{
    setlocale(LC_ALL, "Russian");
    Enemy enemy;
    Player player;
    Weapon* lists[8];
    lists[0] = new Gun;
    lists[1] = new SubmachinGun;
    lists[2] = new Snaiper;
    lists[3] = new Bazooka;
    lists[4] = new Knife;
    lists[5] = new Grenade;
    lists[6] = new Click;
    lists[7] = new heal;
    int k;
    while (true) {
        cout << "Пистолет(10) - 0, Пулемет(30) - 1, Винтовка(20) - 2, Базука(40) - 3, Нож(5) - 4, Граната(100) - 5, Щелбан(1) - 6" << endl;
        cout << "Введите номер оружия, которое хотите использовать" << endl;
        cin >> k;
        player.Shoot(lists[k]);
        if (enemy.kick(lists[k]->Get()))
        {
            cout << "Здоровье врага:" << enemy.Get1() << endl;
        }
        else
        {
            break;
        }
        if (enemy.Get1() <= 10)
        {
            player.Shoot(lists[7]);
            enemy.kick(lists[7]->Get());
            cout << "Здоровье врага:" << enemy.Get1() << endl;
        }
    }
    for (int i = 0; i < 8; i++) {
        delete lists[i];
    }
    return 0;
}
