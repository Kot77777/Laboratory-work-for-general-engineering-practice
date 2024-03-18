#include "SubmachinGun.h"
#include <iostream>

void SubmachinGun::Shoot() const
{
	std::cout << "Пулемет" << std::endl;
	std::cout << "Вы продырявили врага" << std::endl;
}

int SubmachinGun::Get() const
{
	return this->damage;
}
