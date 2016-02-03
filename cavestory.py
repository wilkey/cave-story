import argparse
import random

# some comment here
class Character(object):

  def __init__(self, name, health, damage):
    self.name = name
    self.health = health
    self.damage = damage

  def attack_opponent(self, opponent):
    opponent.take_damage(self.damage)

  def take_damage(self, damage):
    self.health -= damage

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

player = {
	'health': 20,
	'dmg': 6
}


def choice():
	print "****Choose a cave****\n"
	print " Cave Entrance[1]"
	print " Cave Entrance[2]"
	print " Cave Entrance[3]"

def fight(mob):
	print "You engage the %s !!" % mob['mob']
	mob_health = mob['health']
	mob_dmg = mob['dmg']
	player_health = player['health']
	player_dmg = player['dmg']

	while True:
		mob_health = mob_health - player_dmg
		player_health = player_health - mob_dmg
		if mob_health <= 0:
			print "You win!"
			player['health'] += 5
			player['dmg'] += 1
			break
		if player_health <= 0:
			print "You suck balls and died"
			player['health'] = 20
			player['dmg'] = 6
			break
	main()		



def fight_run(mob):	
	print "%s's health is %s and damage is %s" % (mob['mob'], mob['health'], mob['dmg']) 
	print "Your health is %s and damage is %s" % (player['health'], player['dmg'])
	choice = raw_input("What do you choose? ")
	if choice == "run":
		main()
	elif choice == "fight":
		fight(mob)
	else:
		print "Invalid choice; choose 'fight' or 'run' "
		fight_run(mob)


def cave1():
	random_number = random.randint(0, 2)
	mob = monsters[1][random_number]
	print "A wild %s has appeared!!" % mob['mob']
	print "Fight or Run?"
	fight_run(mob)


def cave2():
	random_number = random.randint(0, 2)
	mob = monsters[2][random_number]
	print "A wild %s has appeared!!" % mob['mob']
	print "Fight or Run?"
	fight_run(mob)


def cave3():
	random_number = random.randint(0, 2)
	mob = monsters[3][random_number]
	print "A wild %s has appeared!!" % mob['mob']
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
	if player['health'] >= 45:
		print "You're AN HERO!"
		exit(0)
	choice()
	chosen_cave = raw_input("What entrance do you choose? ")
	print "you chose '%s'" % chosen_cave
	cavepick(chosen_cave)


if __name__ == '__main__':
	main()