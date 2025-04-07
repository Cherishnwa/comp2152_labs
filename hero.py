from character import Character

class Hero(Character):
    def __init__(self, combat_strength, health_points, name = "Unknown Hero"):
        super().__init__(combat_strength, health_points)
        self.name = name


    def hero_attack(self, m_health_points):
        print(f"Hero's weapon ({self.combat_strength} points)")
        if self.combat_strength >= m_health_points:
            # Player was strong enough to kill monster in one blow
            m_health_points = 0
            print("You have killed the monster!")
        else:
            # Player only damaged the monster
            m_health_points -= self.combat_strength

            print("You have reduced the monster's health to: " + str(m_health_points))
        return m_health_points    
    
    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")
        super().__del__()

    # def hero_attack(self, m_health_points):
    #     print(f"Hero's weapon ({self.combat_strength} points)")
    #     monste
    #     if self.combat_strength >= m_health_points:
    #         # Player was strong enough to kill monster in one blow
    #         m_health_points = 0
    #         print("    |    You have killed the monster")
    #     else:
    #         # Player only damaged the monster
    #         m_health_points -= self.combat_strength

    #         print("    |    You have reduced the monster's health to: " + str(m_health_points))
    #     return m_health_points