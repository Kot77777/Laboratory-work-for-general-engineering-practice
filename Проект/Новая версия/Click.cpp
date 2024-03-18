#include "Click.h"
#include <iostream>

int Click::Get() const
{
    return this->damage;
}

void Click::Shoot() const
{
    std::cout << "Щелбан" << std::endl;
    std::cout << "Вы выиграли врага в камень, ножницы, бумага" << std::endl;
}
