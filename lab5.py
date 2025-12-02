"""laboratorna5"""

class Fish:
    """клас рибок"""
    def __init__(self, name="salmon", age=1, species="common", size=2,
                 preferred_food="sea grass", is_aggressive=False, needed_space=5):
        self.name = name
        self.age = age if age >= 0 else "undefined"
        self.species = species
        self.size = size
        self.preferred_food = preferred_food
        self.is_aggressive = is_aggressive
        self.needed_space = needed_space if needed_space > 0 else "undefined"

    def __str__(self):
        result = (
            f'Імя: {self.name}\nВік: {self.age}\nВид: {self.species}\nРозмір: {self.size}'
            f'\nПотрібна їжа: {self.preferred_food}\nАгресивна?: {self.is_aggressive}'
            f'\nПотрібно місця: {self.needed_space} м^3'
        )
        if "undefined" in result:
            result = "Введено некоректні данні!!!"
        return result

    def __repr__(self):
        result = (
            f'name: {self.name}\nage: {self.age}\nspecies: {self.species}\nsize: {self.size}'
            f'\npreferred_food: {self.preferred_food}\nis_aggressive: {self.is_aggressive}'
            f'\nneeded_space: {self.needed_space}'
        )
        if "undefined" in result:
            result = "Введено некоректні данні!!!"
        return result

    @property
    def info(self):
        return {
            "name": self.name,
            "age": self.age,
            "species": self.species,
            "size": self.size,
            "preferred_food": self.preferred_food,
            "is_aggressive": self.is_aggressive,
            "needed_space": self.needed_space
        }
    
    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        if age >= 0:
            self.age = age
        else:
            raise ValueError("вік не може бути меншим нуля!!!")
   
    def set_species(self, species):
        self.species = species

    def set_size(self, size):
        if type(size) in (int, float) and size > 0:
            self.size = size
        else:
            raise ValueError("Розмір має бути числом більше нуля!!!")
    
    def set_preferred_food(self, preferred_food):
        self.preferred_food = preferred_food

    def set_is_aggressive(self, is_aggressive):
        if is_aggressive in (True, False):
            self.is_aggressive = is_aggressive
        else:
            raise ValueError("Значення може бути тільки True або False!!!")
        
    def set_needed_space(self, needed_space):
        if needed_space > 0 and type(needed_space) in (int, float):
            self.needed_space = needed_space
        else:
            raise ValueError("Потрібне місце має бути більш ніж 0!!!")
        
    def __del__(self):
        print(f"{self.name} закінчила свій життєвий цикл")
    
class Aquarium:
    """клас акваріума для рибок"""
    def __init__(self, total_volume, free_space=None):
        self.total_volume = total_volume if total_volume > 0 else "undefined"
        if free_space is None:
            self.free_space = total_volume
        else:
            self.free_space = free_space
        self.fishes = []
        self.fishes_name = []
        self.is_aggressive = []
        

    def __str__(self):
        result = (
            f'Повний розмір: {self.total_volume}\n'
            f'Вільно місця: {self.free_space}\n'
            f'Риби: {self.fishes_name}'
        )
        if "undefined" in result:
            result = "Введено некоректні данні!!!"
        return result
    

    def add_fish(self, fish_class):
        if fish_class.needed_space <= self.free_space:
            if fish_class.is_aggressive and False in self.is_aggressive:
                raise ValueError("Агресивні рибки не дружать з неагресивними!")
            elif not fish_class.is_aggressive and True in self.is_aggressive:
                raise ValueError("Неагресивні рибки не дружать з агресивними!")
            
            self.fishes.append(fish_class)
            self.fishes_name.append(fish_class.name)
            self.is_aggressive.append(fish_class.is_aggressive)
            self.free_space -= fish_class.needed_space
            print(f'{self.fishes_name} Населяють акваріум')
        
        else:
            raise ValueError("В акваріумі замало місця!")
    
    def top3_by_size(self):
        return sorted(self.fishes, key=lambda f: f.size, reverse=True)[:3]
    
    def get_total_volume(self):
        return self.total_volume
    
    def get_free_space(self):
        return self.free_space
    
    def get_fishes(self):
        return self.fishes
    
    def __del__(self):
        print("акваріум зломано")

if __name__ == "__main__":
    print("ініціалізація...")
    
    fish1 = Fish()
    fish2 = Fish(name="tuna", age=2, species="tuna", size=3,
                 preferred_food="small fish", is_aggressive=False, needed_space=5)
    fish3 = Fish(name="goldie", age=2, species="goldfish", size=1,
                 preferred_food="flakes", is_aggressive=False, needed_space=1.5)
    fish4 = Fish(name="clown", age=3, species="clownfish", size=1,
                 preferred_food="plankton", is_aggressive=False, needed_space=1.5)
    fish5 = Fish(name="betta", age=1, species="betta", size=1,
                 preferred_food="flakes", is_aggressive=True, needed_space=1.8)
    fish6 = Fish(name="carp", age=4, species="carp", size=3,
                 preferred_food="plants", is_aggressive=False, needed_space=10)
    fish7 = Fish(name="piranha", age=2, species="piranha", size=2,
                 preferred_food="meat", is_aggressive=True, needed_space=2.5)
    fish8 = Fish(name="tiger", age=3, species="tiger fish", size=2.5,
                 preferred_food="small fish", is_aggressive=True, needed_space=3)
    aquarium1 = Aquarium(30, 25)
    aquarium2 = Aquarium(25, 20)
    
    print("\nІнформація про fish1:")
    fish1.set_needed_space(3.5)
    print(fish1)
    print(fish1.info["name"])

    print("\nДодавання риб до акваріума 1:")
    aquarium1.add_fish(fish3)
    aquarium1.add_fish(fish1)
    aquarium1.add_fish(fish6)
    aquarium1.add_fish(fish4)
    
    print("\nДодавання риб до акваріума 2:")
    aquarium2.add_fish(fish5)
    aquarium2.add_fish(fish7)
    aquarium2.add_fish(fish8)
    
    print("\nІнформація про акваріум 1:")
    print(aquarium1)
    
    print("\nІнформація про акваріум 2:")
    print(aquarium2)
    
    print("\nТоп 3 риби за розміром в акваріумі 1:")
    print(aquarium1.top3_by_size())
    