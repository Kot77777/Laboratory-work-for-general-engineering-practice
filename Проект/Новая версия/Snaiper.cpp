#include "Snaiper.h"
#include <iostream>

int Snaiper::Get() const
{
    return damage;
}
void Snaiper::Shoot() const
{
    std::cout << "Винтовка" << std::endl;
    std::cout << "Вы сделалаи во враге одну жалкую, но точную дырку" << std::endl;
}