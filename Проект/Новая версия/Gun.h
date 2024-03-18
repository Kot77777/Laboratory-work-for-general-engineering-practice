#pragma once
#include "Class_weapon.h"

class Gun: public Weapon
{
private:
	int damage = 10;
public:
	int Get() const override;
	void Shoot() const override;
};

