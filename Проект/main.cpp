class Enemy
{
private:
    int HP = 100;
public:
    int Get1()
    {
        return this->HP;
    }
    bool kick(int damage)
    {
        this->HP -= damage;
        if (this->HP <= 0)
        {
            cout << "Враг повержен" << endl;
            return false;
        }
        return true;
    }

};

class Player
{
public:
    void Shoot(Weapon* weapon)
    {
        weapon->Shoot();
    }
};
