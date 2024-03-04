#include <iostream>
#include <string>
using namespace std;

class Weapon
{
public:
    virtual void Shoot() = 0; //������ ������ �����������
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
        cout << "��������" << endl;
        cout << "�� �������� �� ����� ���� ������ �����" << endl;
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
        cout << "��������" << endl;
        cout << "�� �������� �� ����� ���� ������, �� ������ �����" << endl;
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
        cout << "�������" << endl;
        cout << "�� ����������� �����" << endl;
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
        cout << "������" << endl;
        cout << "�� ������ ����� ����� ����� ����" << endl;
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
        cout << "������" << endl;
        cout << "�� �������� ����� � ������, �������, ������" << endl;
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
        cout << "���" << endl;
        cout << "�� ������� �����" << endl;
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
        cout << "���� �������������� ��������" << endl;
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
        cout << "�������" << endl;
        cout << "�� ������ ��������� ����, ������� �� ������� ����(" << endl;
    }
};

int main()
{

    return 0;
}
