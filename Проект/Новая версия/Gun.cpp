#include "Gun.h"
#include <iostream>

int Gun::Get() const
{
    return this->damage;
}

void Gun::Shoot() const
{
	std::cout << "Пистолет" << std::endl;
	std::cout << "Вы сделалаи во враге одну жалкую дырку" << std::endl;
}
