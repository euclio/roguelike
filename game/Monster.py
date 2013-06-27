class Food(object):
    def __init__(self, hp, damage, reward, speed):
	self.hp = hp
        self.damage = damage
	self.reward = reward
	self.speed = speed
	
    def kill(self, target, damage):
        target.hp -= damage

class Apple(Food):
    hp = 1
    damage = 0
    reward = 2
    speed = 1
    def __init__(self):
        Food.__init__(self, self.hp, self.damage, self.reward, self.speed)
    def kill(self, target):
	return Food.kill(self, target, self.damage)

class Banana(Food):
    hp = 1
    damage = 1
    reward = 2
    speed = 2
    def __init__(self):
        Food.__init__(self, self.hp, self.damage, self.reward, self.speed)
    def kill(self, target):
	return Food.kill(self, target, self.damage)

class Brocolli(Food):
    hp = 5
    damage = 5
    reward = -5
    speed = 3
    def __init__(self):
        Food.__init__(self, self.hp, self.damage, self.reward, self.speed)
    def kill(self, target):
	return Food.kill(self, target, self.damage)

class InstantNoodle(Food):
    hp = 10
    damage = 2
    reward = 1
    speed = 0
    def __init__(self):
        Food.__init__(self, self.hp, self.damage, self.reward, self.speed)
    def kill(self, target):
	return Food.kill(self, target, self.damage)

class BehemothBurger(Food):
    hp = 10
    damage = 10
    reward = 20
    speed = 0
    def __init__(self):
        Food.__init__(self, self.hp, self.damage, self.reward, self.speed)
    def kill(self, target):
	return Food.kill(self, target, self.damage)

class Watermelon(Food):
    hp = 10
    damage = 10
    reward = 20
    speed = 0
    def __init__(self):
        Food.__init__(self, self.hp, self.damage, self.reward, self.speed)
    def kill(self, target):
	return Food.kill(self, target, self.damage)

class Peach(Food):
    hp = 0 
    damage = 0
    reward = 2
    speed = 0
    def __init__(self):
        Food.__init__(self, self.hp, self.damage, self.reward, self.speed)
    def kill(self, target):
	return Food.kill(self, target, self.damage)


