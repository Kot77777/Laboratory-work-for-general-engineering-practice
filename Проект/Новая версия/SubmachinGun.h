#pragma once
#include "Gun.h"
class SubmachinGun: public Gun
{
private:
    int damage = 30;
public:
    int Get() const override;
    void Shoot() const override;
};

