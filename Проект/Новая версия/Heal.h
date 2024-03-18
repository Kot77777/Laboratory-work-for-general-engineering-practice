#pragma once
#include "Class_weapon.h"
class heal: public Weapon
{
private:
    int damage = -10;
public:
    int Get() const;
    void Shoot() const override;
};