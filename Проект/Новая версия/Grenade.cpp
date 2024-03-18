#include "Grenade.h"
#include <iostream>

int Grenade::Get() const
{
    return this->damage;
}

void Grenade::Shoot() const
{
    std::cout << "Граната" << std::endl;
    std::cout << "Вы зыбыли выдернуть чеку, поэтому не нанесли урон(" << std::endl;
}
