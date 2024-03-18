#include "Bazooka.h"
#include <iostream>

void Bazooka::Shoot() const
{
    std::cout << "Базука" << std::endl;
    std::cout << "Вы лишили врага одной части тела" << std::endl;
}

int Bazooka::Get() const
{
	return this->damage;
}
