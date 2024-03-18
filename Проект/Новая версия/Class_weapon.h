#pragma once
class Weapon
{
public:
    virtual void Shoot() const = 0; //делаем читсто виртуальной
    virtual int Get() const = 0;
};