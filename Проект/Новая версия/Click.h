#pragma once
#include "Class_weapon.h"
class Click : public Weapon
{
private:
	int damage = 1;
public:
	int Get() const override;
	void Shoot() const override;
};
