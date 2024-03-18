#pragma once
class Enemy
{
private:
    int HP = 100;
public:
    int Get1() const;
    bool kick(int const damage);

};