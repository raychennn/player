class Player:
	def __init__(self,name, ap, heal):
		self.hp = 100
		self.name = name
		self.ap = ap
		self.heal = heal
	def attack(self, target):
		print(self.name, '攻擊了' ,target.name)
		target.hp = target.hp - self.ap
	def recover(self):
		print(self.name, '恢復了',self.heal, '滴血')
		self.hp = self.hp + self.heal

	

p1 = Player('Player1', 10, 20)
p2 = Player('Player2', 5, 25)
p1.attack(p2)
print(p2.name,'剩下',p2.hp , '生命值')	

p2.recover()
print(p2.name, '增加了', p2.heal, '生命值')