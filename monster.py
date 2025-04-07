from character import Character
class Monster(Character):  
    # Monster class inherits from Character class
    def __init__(self, combat_strength, health_points):
        super().__init__(combat_strength, health_points)
        
    def monster_attacks(self, health_points):
        print("Monster's Claw! ({self.combat_strength}) points)")
        if self.combat_strength >= health_points:
            # Monster was strong enough to kill player in one blow
            health_points = 0
            print("Hero is dead")
        else:
            # Monster only damaged the player
            health_points -= self.combat_strength
        return health_points
    
    def __del__(self):
        print(f"The Monster object is being destroyed by the garbage collector")
        super().__del__()


