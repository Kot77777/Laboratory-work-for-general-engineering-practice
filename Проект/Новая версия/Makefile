.PHONY: all clean install uninstall

all: fallout_7

clean:
	rm *.o fallout_7

install:
	install ./fallout_7 /usr/local/bin

uninstall:
	rm /usr/local/bin/fallout_7

Bazooka.o: ../multi-file_assembly/Bazooka.cpp ../multi-file_assembly/Bazooka.h
	g++ -c ../multi-file_assembly/Bazooka.cpp -o Bazooka.o

Class_weapon.o: Class_weapon.cpp Class_weapon.h
	g++ -c Class_weapon.cpp -o Class_weapon.o

Click.o: Click.cpp Click.h
	g++ -c Click.cpp -o Click.o

Enemy.o: Enemy.cpp Enemy.h
	g++ -c Enemy.cpp -o Enemy.o

Grenade.o: Grenade.cpp Grenade.h
	g++ -c Grenade.cpp -o Grenade.o

Gun.o: Gun.cpp Gun.h
	g++ -c Gun.cpp -o Gun.o

Heal.o: Heal.cpp Heal.h
	g++ -c Heal.cpp -o Heal.o

Knife.o: Knife.cpp Knife.h
	g++ -c Knife.cpp -o Knife.o

Player.o: Player.cpp Player.h
	g++ -c Player.cpp -o Player.o

Snaiper.o: Snaiper.cpp Snaiper.h
	g++ -c Snaiper.cpp -o Snaiper.o

SubmachinGun.o: SubmachinGun.cpp SubmachinGun.h
	g++ -c SubmachinGun.cpp -o SubmachinGun.o

fallout_7: multi-file_assembly.cpp Bazooka.o Class_weapon.o Click.o Enemy.o Grenade.o Gun.o Heal.o Knife.o Player.o Snaiper.o SubmachinGun.o Bazooka.h Class_weapon.h Click.h Enemy.h Grenade.h Gun.h Heal.h Knife.h Player.h Snaiper.h SubmachinGun.h
	g++ multi-file_assembly.cpp Bazooka.o Class_weapon.o Click.o Enemy.o Grenade.o Gun.o Heal.o Knife.o Player.o Snaiper.o SubmachinGun.o -o fallout_7	
