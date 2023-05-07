from src.entity.Player import Player

class EntityManager():
    # Liste de tous les Projectiles
    projectiles = []

    # Liste de tous les Aliens
    aliens = []

    def get_projectiles(self):
        return self.projectiles

    def get_aliens(self):
        return self.aliens

    def create_player(self):
        return Player()