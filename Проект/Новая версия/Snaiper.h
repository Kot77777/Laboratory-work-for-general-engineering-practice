#pragma once
#include "Gun.h"
class Snaiper : public Gun
{
private:
    int damage = 20;
public:
    int Get() const override;
    void Shoot() const override;
};