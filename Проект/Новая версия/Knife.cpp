#include "Knife.h"
#include <iostream>

void Knife::Shoot() const
{
    std::cout << "Нож" << std::endl;
    std::cout << "Вы пырнули врага" << std::endl;
}

int Knife::Get() const
{
	return this->damage;
}
