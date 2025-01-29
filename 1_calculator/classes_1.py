class Enemy:
    atkl = 60
    atkh = 80
    hp = 200

    def __init__(self,atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print(self.atkl)
    
    def gethp(self):
        print("Hp is ",self.hp)

enemy1 = Enemy(40,50)
enemy1.getAtk()
enemy1.gethp()

enemy2 =Enemy(70,80)
enemy2.getAtk()
enemy2.gethp()