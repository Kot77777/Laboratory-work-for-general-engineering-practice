#pragma once
#include "Class_weapon.h"
class Grenade : public Weapon
{
private:
    int damage = 0;
public:
    int Get() const;
    void Shoot() const override;
};