#pragma once
#include "Class_weapon.h"
class Knife: public Weapon
{
private:
	int damage = 5;
public:
	void Shoot() const override;
	int Get() const override;
};

