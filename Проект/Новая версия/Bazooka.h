#pragma once
#include "Class_weapon.h"
class Bazooka: public Weapon
{
private:
	int damage = 40;
public:
	int Get() const override;
	void Shoot() const override;
};

