import argparse
import random


class Character(object):

  def __init__(self, name, health, attack):
    self.name = name
    self.health = health
    self.attack = attack
    self.health_bonus = 0
    self.attack_bonus = 0
    self.damage_taken = 0


  def attack_opponent(self, opponent):
    opponent.take_damage(self.effective_attack())

  def take_damage(self, attack):
    self.damage_taken += attack

  def effective_health(self):
  	return self.health + self.health_bonus - self.damage_taken

  def effective_attack(self):
  	return self.attack + self.attack_bonus




monsters = {}

monsters[1] = [{'mob': 'Bat', 'health': 18, 'dmg': 5},
				 {'mob': 'Snake', 'health': 26, 'dmg': 7},
				 {'mob': 'Eye', 'health': 35, 'dmg': 9}]
monsters[2] = [{'mob': 'Horse', 'health': 40, 'dmg': 11},
				 {'mob': 'Caterpillar', 'health': 8, 'dmg': 2},
				 {'mob': 'Crawler', 'health': 22, 'dmg': 4}]
monsters[3] = [{'mob': 'Damselfly', 'health': 26, 'dmg': 5},
				 {'mob': 'Rat', 'health': 13, 'dmg': 1},
				 {'mob': 'Snipper', 'health': 38, 'dmg': 10}]


player = Character("John", 20, 6)

def choice():
	print "****Choose a cave****\n"
	print " Cave Entrance[1]"
	print " Cave Entrance[2]"
	print " Cave Entrance[3]"

def fight(mob):
	print "You engage the %s !!" % mob.name

	while True:
		player.attack_opponent(mob)
		if mob.effective_health() <= 0:
			print "You win!"
			player.health_bonus += 5
			player.attack_bonus += 1
			player.damage_taken = 0
			break
		mob.attack_opponent(player)
		if player.effective_health() <= 0:
			print "You suck balls and died"
			player.health_bonus = 0
			player.attack_bonus = 0
			player.damage_taken = 0
			break
	main()		



def fight_run(mob):	
	print "%s's health is %s and attack is %s" % (mob.name, mob.health, mob.attack) 
	print "Your health is %s and attack is %s" % (player.effective_health(), player.effective_attack())
	choice = raw_input("What do you choose? ")
	if choice in ['r', 'run']:
		main()
	elif choice in ['f', 'fight']:
		fight(mob)
	else:
		print "Invalid choice; choose 'fight' or 'run' "
		fight_run(mob)


def cave1():
	random_number = random.randint(0, 2)
	mob = Character(monsters[1][random_number]['mob'], monsters[1][random_number]['health'], monsters[1][random_number]['dmg'])
	print "A wild %s has appeared!!" % mob.name
	print "[F]ight or [R]un?"
	fight_run(mob)


def cave2():
	random_number = random.randint(0, 2)
	mob = Character(monsters[2][random_number]['mob'], monsters[2][random_number]['health'], monsters[2][random_number]['dmg'])
	print "A wild %s has appeared!!" % mob.name
	print "[F]ight or [R]un?"
	fight_run(mob)


def cave3():
	random_number = random.randint(0, 2)
	mob = Character(monsters[3][random_number]['mob'], monsters[3][random_number]['health'], monsters[3][random_number]['dmg'])
	print "A wild %s has appeared!!" % mob.name
	print "Fight or Run?"
	fight_run(mob)



def cavepick(cave):
	if cave == '1':
		cave1()	
	elif cave == '2':
		cave2()	
	elif cave == '3':
		cave3()	
	else:
		print "Invalid Cave; Choose 1, 2, or 3."
		main()



def main():
	if player.effective_health() >= 45:
		print "You're AN HERO!"
		exit(0)
	choice()
	chosen_cave = raw_input("What entrance do you choose? ")
	print "you chose '%s'" % chosen_cave
	cavepick(chosen_cave)


if __name__ == '__main__':
	main()