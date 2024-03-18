#include "Enemy.h"
#include <iostream>

int Enemy::Get1() const
{
    return this->HP;
}

bool Enemy::kick(int const damage)
{
    this->HP -= damage;
    if (this->HP <= 0)
    {
        std::cout << "Враг повержен" << std::endl;
        return false;
    }
    return true;
}