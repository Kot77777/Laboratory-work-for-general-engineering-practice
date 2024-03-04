#include <iostream>
#include <string>
using namespace std;

class Weapon
{
public:
    virtual void Shoot() = 0; //делаем читсто виртуальной
    virtual int Get() = 0;
};

class Gun: public Weapon
{
private:
    int damage = 10;
public:
    int Get()
    {
        return this->damage;
    }
    void Shoot() override
    {
        cout << "Пистолет" << endl;
        cout << "Вы сделалаи во враге одну жалкую дырку" << endl;
    }
};

class Snaiper: public Gun
{
private:
    int damage = 20;
public:
    int Get()
    {
        return damage;
    }
    void Shoot() override
    {
        cout << "Винтовка" << endl;
        cout << "Вы сделалаи во враге одну жалкую, но точную дырку" << endl;
    }
};

class SubmachinGun: public Gun
{
private:
    int damage = 30;
public:
    int Get()
    {
        return damage;
    }
    void Shoot() override
    {
        cout << "Пулемет" << endl;
        cout << "Вы продырявили врага" << endl;
    }
};

class Bazooka: public Weapon
{
private:
    int damage = 40;
public:
    int Get()
    {
        return damage;
    }
    void Shoot() override
    {
        cout << "Базука" << endl;
        cout << "Вы лишили врага одной части тела" << endl;
    }
};

class Click: public Weapon
{
private:
    int damage = 1;
public:
    int Get()
    {
        return damage;
    }
    void Shoot() override
    {
        cout << "Щелбан" << endl;
        cout << "Вы выиграли врага в камень, ножницы, бумага" << endl;
    }
};

class Knife: public Weapon
{
private:
    int damage = 5;
public:
    int Get()
    {
        return damage;
    }
    void Shoot() override
    {
        cout << "Нож" << endl;
        cout << "Вы пырнули врага" << endl;
    }
};

class heal: public Weapon
{
private:
    int damage = -10;
public:
    int Get()
    {
        return this->damage;
    }
    void Shoot() override
    {
        cout << "Враг воспоьлзовался аптечкой" << endl;
    }
};

class Grenade: public Weapon
{
private:
    int damage = 0;
public:
    int Get()
    {
        return damage;
    }

    void Shoot() override
    {
        cout << "Граната" << endl;
        cout << "Вы зыбыли выдернуть чеку, поэтому не нанесли урон(" << endl;
    }
};

int main()
{

    return 0;
}
