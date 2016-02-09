import argparse
from random import choice

# hello 
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


monster_table = [{'name': 'Bat', 'health': 18, 'attack': 5, 'location': 1},
				 {'name': 'Snake', 'health': 26, 'attack': 7, 'location': 1},
				 {'name': 'Eye', 'health': 35, 'attack': 9, 'location': 1},
				 {'name': 'Horse', 'health': 40, 'attack': 11, 'location': 2},
				 {'name': 'Caterpillar', 'health': 8, 'attack': 2, 'location': 2},
				 {'name': 'Crawler', 'health': 22, 'attack': 4, 'location': 2},
				 {'name': 'Damselfly', 'health': 26, 'attack': 5, 'location': 3},
				 {'name': 'Rat', 'health': 13, 'attack': 1, 'location': 3},
				 {'name': 'Snipper', 'health': 38, 'attack': 10, 'location': 3}]


player = Character("John", 20, 6)


def choose():
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


def fight_run(monster):	
	print "%s's health is %s and attack is %s" % (monster.name, monster.health, monster.attack) 
	print "Your health is %s and attack is %s" % (player.effective_health(), player.effective_attack())
	choice = raw_input("What do you choose? ")
	if choice in ['r', 'run']:
		main()
	elif choice in ['f', 'fight']:
		fight(monster)
	else:
		print "Invalid choice; choose 'fight' or 'run' "
		fight_run(monster)


class Monster(Character):

	def __init__(self, index):
		monster = monster_table[index]
		super(Monster, self).__init__(monster['name'], monster['health'], monster['attack'])

	def approach_player(self):
		print "A wild %s has appeared!!" % self.name
		print "[F]ight or [R]un?"
		fight_run(self)


def cavepick(cave):
	print type(cave)
	if cave in [1, 2, 3]:
		picks = {1: range(0, 3),
				 2: range(3, 6),
				 3: range(6, 9)}	
		monster = Monster(choice(picks[cave]))
		monster.approach_player()
	else:
		print "Invalid Cave; Choose 1, 2, or 3."
		main()


def main():
	if player.effective_health() >= 45:
		print "You're AN HERO!"
		exit(0)
	choose()
	chosen_cave = raw_input("What entrance do you choose? ")
	
	print "you chose '%s'" % chosen_cave
	
	try:
		chosen_cave = int(chosen_cave)
	except Exception as err:
		print err

	cavepick(chosen_cave)


if __name__ == '__main__':
	main()