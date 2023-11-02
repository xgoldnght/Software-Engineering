class Tomato:
    # Статическое свойство с стадиями созревания помидора
    states = {"отсутствует": 0, "цветение": 1, "зеленый": 2, "красный": 3}
    def __init__(self, index):
        # Динамические свойства
        self._index = index
        self._state = Tomato.states["отсутствует"]
    def grow(self):
        if self._state < Tomato.states["красный"]:
            self._state += 1
    def is_ripe(self):
        return self._state == Tomato.states["красный"]
class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)
    def give_away_all(self):
        self.tomatoes = []
class Gardener:
    def __init__(self, name, plant):
        # Динамические свойства
        self.name = name
        self._plant = plant
    def work(self):
        self._plant.grow_all()
    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
        else:
            print("Пока не все помидоры созрели. Продолжайте ухаживать за ними.")
    @staticmethod
    def knowledge_base():
        print("Справка по садоводству: ...")
# Тесты
if __name__ == "__main__":
    Gardener.knowledge_base()
    tomato_bush = TomatoBush(5)
    gardener = Gardener("John", tomato_bush)
    # Рост томатов
    gardener.work()  
    # Собрать урожай (не все созрели)
    gardener.harvest()  
    # Продолжение ухода
    gardener.work()  
    # Продолжение ухода
    gardener.work()  
    # Продолжение ухода
    gardener.work()  
    # Собрать урожай (все созрели)
    gardener.harvest()  